---
title: PHP-Cli模式下连接Docker容器中的Redis
categories: PHP
---

![WechatIMG7.jpeg](https://upload-images.jianshu.io/upload_images/15325592-b2e2584f38ce6ff9.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境
- macOS 10.14.6
- docker 19.03.8
- php 5.6.40
- redis 5.0.3 

#  插件
- [dnmp](https://github.com/yeszao/dnmp "dnmp")

#  cron1.php
```
<?php
$redis = new Redis();  
$redis->connect('redis', 6379);
var_dump('<pre>',$redis);exit;
```

#  错误
```
$ php56 cron1.php
Fatal error: Uncaught exception 'RedisException' with message 'Connection refused' in /www/cron1.php:3
Stack trace:
# 0 /www/cron1.php(3): Redis->connect('redis', 6379)
# 1 {main}
  thrown in /www/cron1.php on line 3
```
> 在执行 php 文件的时候，报了上述错误。原因是主机要连接 docker 中的 redis，要求容器必须经过 ports 把端口映射到主机，所以主机上访问 redis 的地址是 127.0.0.1:6379。

```
$ php56 cron1.php
Fatal error: Uncaught exception 'RedisException' with message 'Connection refused' in /www/cron1.php:3
Stack trace:
# 0 /www/cron1.php(3): Redis->connect('127.0.0.1', 6379)
# 1 {main}
  thrown in /www/cron1.php on line 3
```
> 把 host 地址改为 '127.0.0.1'后再进行尝试，仍然报错...

```
$ php56 cron1.php
string(5) "<pre>"
object(Redis)# 1 (0) {
}
```
> 经各种尝试后，把 host 地址改为本机的 ip 地址，成功连接 redis~
