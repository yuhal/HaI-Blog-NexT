---
title: PHP-TP5-使用MongoDb
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-f8ce742d0afd8717?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
首先安装官方的mongodb扩展：
找到对应的php版本的扩展
然后，配置应用的数据库配置文件database.php的type参数为：
```
'type' => '\think\mongo\connection',
```
即可正常使用mongodb，例如：
使用最新mongodb扩展
```
db::name('demo')
  ->find();
db::name('demo')
  ->field('id,name')
  ->limit(10)
  ->order('id','desc')
  ->select();
```
或者使用模型操作：
```
user::get(1);
user::all('1,2,3');
```
mongodb默认的主键是_id并且是一个objectid对象，如果需要和mysql一样使用id作为主键，可以如下参数：
```
// 强制把_id转换为id
'pk_convert_id' => true,
```
手册https://api.yuhal.com/file/ThinkPHP.chm
