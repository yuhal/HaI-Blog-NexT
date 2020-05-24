---
title: PHP-Cli模式连接Redis
categories: PHP
---

![WechatIMG6.jpeg](https://upload-images.jianshu.io/upload_images/15325592-5d8acef91f201211.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  PHP Cli模式连接Redis

#  环境
- PHP 7.2.24
- Ubuntu 18.04.3

#  testRedis.php
```
<?php
$redis = new Redis();  
$redis->connect('redis', 6379);
var_dump('<pre>',$redis);exit;
```

#  错误
```
$ php testRedis.php
Fatal error: Class 'Redis' not found
```
> 在执行 php 文件的时候，报了上述错误。原因是没有安装 [phpredis](https://github.com/phpredis/phpredis "phpredis") 

#  解决
- 下载 phpredis 源码
`git clone git://github.com/nicolasff/phpredis.git`

- 进入 phpredis 目录
`cd phpredis`

- 执行 phpize 生成 configure 文件
`phpize`

- 运行配置
`./configure --with-php-config=/usr/local/php/bin/php-config`

- 编译模块
`make && make install`

- 手动创建 redis.ini 文件并写入 extension=redis.so
`echo "extension=redis.so">/usr/local/php/conf.d/redis.ini`

- 再次执行
```
$ php testRedis.php
string(5) "<pre>"
object(Redis)# 1 (0) {
}
```
