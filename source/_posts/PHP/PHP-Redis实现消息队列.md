---
title: PHP-Redis实现消息队列
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-db1fb3adbc50b6bd?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 一、创建into.php

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1',6379);
$password = '123456';
$redis->auth($password);
$arr = array('h','e','l','l','o','w','o','r','l','d');
foreach($arr as $k=>$v){
  $redis->rpush("mylist",$v);
}
?>
```
# 二、创建out.php
```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1',6379);
$password = '123456';
$redis->auth($password);
//list类型出队操作
$value = $redis->lpop('mylist');
if($value){
  echo "出队的值".$value;
}else{
  echo "出队完成";
}
?>
```
# 三、建立定时任务
每10分钟入队列一次
*/10 * * * * root php /www/redis/into.php
每10分钟出队列一次
*/10 * * * * root php /www/redis/out.php
