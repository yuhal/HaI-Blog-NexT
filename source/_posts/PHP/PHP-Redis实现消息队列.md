---
title: PHP-Redis实现消息队列
categories: PHP
---

![4170383BEED5AA5AEFF839AE7B7FD04F.jpg](https://upload-images.jianshu.io/upload_images/15325592-6802dd8f4491e5ad.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- PHP 7.0

- Redis 5.3.1

#  代码

- 创建 inqueue.php，代码如下：

```
<?php
$queueName = 'CoCoQueue';
$redisConfig['host'] = '127.0.0.1';
$redisConfig['port'] = '6379';
$list = [
    ['name'=>'钢铁侠','item'=>'珍珠奶茶'],
    ['name'=>'蜘蛛侠','item'=>'珍珠奶茶'],
    ['name'=>'灭霸','item'=>'美式咖啡'],
];
if(!$list){
    exit("暂无内容");
}else{
    try {
        $redis = new Redis();  
        $redis->connect($redisConfig['host'], $redisConfig['port']);
        $redis->select(0);
    } catch (Exception $e) {
        exit('连接redis失败: '.$e->getMessage());
    }

    $exist = $redis->exists($queueName);
    if(!$exist){
        foreach($list as $value){
            $push = json_encode($value, JSON_UNESCAPED_UNICODE);
            $redis->rpush($queueName,$push);
            printf("入队的值%s\n", $push);
        }
        exit("入队完成");
    }else{
        exit("队列已存在");
    }
}
?>
```

- 创建 outqueue.php，代码如下：

```
<?php
$queueName = 'CoCoQueue';
$redisConfig['host'] = '127.0.0.1';
$redisConfig['port'] = '6379';
try {
    $redis = new Redis();  
    $redis->connect($redisConfig['host'], $redisConfig['port']);
    $redis->select(0);
} catch (Exception $e) {
    exit('连接redis失败: '.$e->getMessage());
}
$size = $redis->lLen($queueName);
if($size){
    for ($i=0; $i < $size; $i++) {
        $pop = $redis->lpop($queueName);
        printf("出队的值%s\n", $pop);
        sleep(1);
    }
    exit('出队完成');
}else{
    exit('队列不存在');
}
?>
```

#  执行

```
$ php inqueue.php
入队的值{"name":"钢铁侠","item":"珍珠奶茶"}
入队的值{"name":"蜘蛛侠","item":"珍珠奶茶"}
入队的值{"name":"灭霸","item":"美式咖啡"}
入队完成
$ php outqueue.php
出队的值{"name":"钢铁侠","item":"珍珠奶茶"}
出队的值{"name":"蜘蛛侠","item":"珍珠奶茶"}
出队的值{"name":"灭霸","item":"美式咖啡"}
```
