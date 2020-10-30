---
title: Dnmp-链接Redis
categories: Dnmp
---

![WechatIMG7.jpeg](https://upload-images.jianshu.io/upload_images/15325592-b2e2584f38ce6ff9.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- [dnmp](https://github.com/yeszao/dnmp "dnmp")

#  代码

```
<?php
$redis = new Redis();  
$redis->connect('redis', 6379);
var_dump('<pre>',$redis);exit;
```

> 创建 test.php，代码如上。

#  错误

```
$ php56 test.php
Fatal error: Uncaught exception 'RedisException' with message 'Connection refused' in /www/test.php:3
Stack trace:
# 0 /www/test.php(3): Redis->connect('redis', 6379)
# 1 {main}
  thrown in /www/test.php on line 3
```

> 在执行 php 文件的时候，报了上述错误。原因是主机要连接 docker 中的 redis，要求容器必须经过 ports 把端口映射到主机，所以主机上访问 redis 的地址是 127.0.0.1:6379。

```
$ php56 test.php
Fatal error: Uncaught exception 'RedisException' with message 'Connection refused' in /www/test.php:3
Stack trace:
# 0 /www/test.php(3): Redis->connect('127.0.0.1', 6379)
# 1 {main}
  thrown in /www/test.php on line 3
```

> 把 host 地址改为`127.0.0.1`后再进行尝试，仍然报错。

```
$ php56 test.php
string(5) "<pre>"
object(Redis)# 1 (0) {
}
```

> 经各种尝试后，把 host 地址改为本机的 ip 地址，成功连接 redis。
