---
title: TP5-scandir()-has-been-disabled-for-security-reasons
categories: TP5
---

![image](https://upload-images.jianshu.io/upload_images/15325592-79aa14f08ba4dec2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 环境
- ThinkPHP 5.1.19
- nginx/1.12.2
- PHP 7.1.8
# 请求
![Screen Shot 2019-12-12 at 11.39.14 AM.png](https://upload-images.jianshu.io/upload_images/15325592-c61f4c0e3f4dc364.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 解决
- 修改 php.ini 中 disable_functions ，删除 scandir 函数并保存。
- 关闭 php 。
```
killall php-fpm 
```
- 重启 php 。
```
/usr/local/php/sbin/php-fpm &
```
- 请求成功
![Screen Shot 2019-12-12 at 11.51.00 AM.png](https://upload-images.jianshu.io/upload_images/15325592-d6298982ad3c6589.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

