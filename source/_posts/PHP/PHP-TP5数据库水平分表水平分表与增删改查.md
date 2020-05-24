---
title: PHP-TP5数据库水平分表水平分表与增删改查
categories: PHP
---
![image](https://upload-images.jianshu.io/upload_images/15325592-c58e62b4ae3d7662?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
 # 一、数据库分表：
## 1、我们首先创建数据表system_log。
```
CREATE TABLE `system_log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `member_id` int(10) NOT NULL DEFAULT '0',
  `history` int(10) DEFAULT NULL,
  `sex` smallint(1) DEFAULT NULL,
  `age` smallint(3) DEFAULT NULL,
  `type` smallint(1) DEFAULT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` smallint(1) DEFAULT '0' COMMENT '1已删0正常',
  PRIMARY KEY (`id`,`member_id`),
  KEY `member_id` (`member_id`),
  KEY `age` (`age`),
  KEY `sex` (`sex`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
/*!50100 PARTITION BY LINEAR KEY (member_id)
PARTITIONS 4 */
```
## 2、手动添加数据表system_log_1,system_log_2,system_log_3,system_log_4字段与数据类型与system_log保持一致。
# 二、数据库增删改查：
## 1、插入数据。
```
$rule = array('type' => 'LINEAR KEY','num' =>4);
$temparr = array('member_id'=>$uid);
$time = time();
Db::name("SystemHistory")->partition($temparr,'member_id',$rule)
    ->insert(array('member_id'=>$uid,'history'=>$view_id,'type'=>$type,'datetime'=>date("Y-m-d  H:i:s",$time)));
```
## 2、查询数据。
```
$rule = array('type' => 'LINEAR KEY','num' =>4);
$temparr = array('member_id'=>$uid);
$time = time();
$arr = Db::name("SystemHistory")->partition($temparr,"member_id",$rule)
    ->where(array('member_id'=>$uid,'history'=>$view_id,'type'=>$type))
    ->whereTime('datetime','today')->find();
```
## 3、修改数据。
```
$rule = array('type' => 'LINEAR KEY','num' =>4);
$temparr = array('member_id'=>$uid);
$time = time();
Db::name("SystemHistory")->partition($temparr,'member_id',$rule)
        ->where(array('member_id'=>$uid,'history'=>$view_id,'type'=>$type))
    ->whereTime('datetime','today')->update(array('datetime'=>date("Y-m-d  H:i:s",$time),'is_deleted'=>0));
```
## 4、删除数据。
删除数据与查询数据雷同，方法修改为delete()即可。
