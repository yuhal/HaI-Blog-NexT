---
title: PHP-全局ID生成方案
categories: PHP
---
![image](https://upload-images.jianshu.io/upload_images/15325592-6a8b0907aad6e0a4?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 1：使用CAS（compare and swap）
其实这里并不是严格的CAS，而是使用了比较交换原子操作的思想。
生成思路如下：每次生成全局id时，先从sequence表中获取当前的全局最大id。然后在获取的全局id上做加1操作。把加1后的值更新到数据库。更新时是关键。
如加1后的值为203,表名是users，数据表结构如下：
```
CREATE TABLE `SEQUENCE` (
  `name` varchar(30) NOT NULL COMMENT '分表的表名',
  `gid` bigint(20) NOT NULL COMMENT '最大全局id',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
那么更新语句是。
update sequence set gid = 203 where name = 'users' and gid < 203;
sql语句的 and gid < 203 是为了保证并发环境下gid的值只增不减。
如果update语句的影响记录条数为0说明，已经有其他进程提前生成了203这个值，并写入了数据库。需要重复以上步骤从新生成。
代码实现如下：
```
//$name 表名
function next_id_db($name){
    //获取数据库全局sequence对象
    $seq_dao = Wk_Sequence_Dao_Sequence::getInstance();
    $threshold = 100; //最大尝试次数
    for($i = 0; $i < $threshold; $i++){
        $last_id = $seq_dao->get_seq_id($name);//从数据库获取全局id
        $id = $last_id +1;
        $ret = $seq_dao->set_seq_id($name, $id);
        if($ret){
            return $id;
            break;
        }
    }
    return false;
}
```
# 2：使用全局锁
在进行并发编程时，一般都会使用锁机制。其实，全局id的生成也是解决并发问题。
生成思路如下：
在使用redis的setnx方法和memcace的add方法时，如果指定的key已经存在，则返回false。利用这个特性，实现全局锁。
每次生成全局id前，先检测指定的key是否存在。
如果不存在则使用redis的incr方法或者memcache的increment进行加1操作。这两个方法的返回值是加1后的值。
如果存在，则程序进入循环等待状态。循环过程中不断检测key是否还存在，如果key不存在就执行上面的操作。
代码如下：
```
//使用redis实现
//$name 为 逻辑表名
function next_id_redis($name){
    $redis = Wk_Redis_Util::getRedis();//获取redis对象
    $seq_dao = Wk_Sequence_Dao_Sequence::getInstance();//获取存储全局id数据表对象
    if(!is_object($redis)){
        throw new Exception("fail to create redis object");
    }
    $max_times = 10; //最大执行次数 避免redis不可用的时候 进入死循环
    while(1){
        $i++;
        //检测key是否存在，相当于检测锁是否存在
        $ret = $redis->setnx("sequence_{$name}_flag",time());
        if($ret){
            break;
        }
        if($i > $max_times){
            break;
        }
        $time = $redis->get("sequence_{$name}_flag");
        if(is_numeric($time) && time() - $time > 1){//如果循环等待时间大于1秒，则不再等待。
            break;
        }
    }
    $id = $redis->incr("sequence_{$name}");
    //如果操作失败，则从sequence表中获取全局id并加载到redis
    if (intval($id) === 1 or $id === false) {
        $last_id = $seq_dao->get_seq_id($name);//从数据库获取全局id
        if(!is_numeric($last_id)){
            throw new Exception("fail to get id from db");
        }
        $ret = $redis->set("sequence_{$name}",$last_id);
        if($ret == false){
            throw new Exception("fail to set redis key [ sequence_{$name} ]");
        }
        $id = $redis->incr("sequence_{$name}");
        if(!is_numeric($id)){
            throw new Exception("fail to incr redis key [ sequence_{$name} ]");
        }
    }
    $seq_dao->set_seq_id($name, $id);//把生成的全局id写入数据表sequence
    $redis->delete("sequence_{$name}_flag");//删除key，相当于释放锁
    $db = null;
    return $id;
}
```
# 3：redis和db结合
使用redis直接操作内存，可能性能会好些。但是如果redis死掉后，如何处理呢？把以上两种方案结合，提供更好的稳定性。
代码如下：
```
function next_id($name){
    try{
        return $this->next_id_redis($name);
    }
    catch(Exception $e){
        return $this->next_id_db($name);
    }
}
```
