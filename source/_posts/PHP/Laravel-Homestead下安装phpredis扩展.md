---
title: Laravel-Homestead下安装phpredis扩展
categories: Laravel
---
![WechatIMG44.jpeg](https://upload-images.jianshu.io/upload_images/15325592-1a3c5d149c44a33a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- Homestead 0.6.0

> Homestead 安装参照 [Laravel Homestead下的环境配置和安装](https://www.jianshu.com/p/1ff606c17464 "Laravel Homestead下的环境配置和安装")。

#  安装phpredis

- 登录到 Homestead

```
$ vagrant ssh
```

- 下载 phpredis

```
$ git clone https://github.com/phpredis/phpredis.git
```

- 进入 phpredis 目录

```
$ cd phpredis
```

- 编译安装

```
$ /usr/bin/phpize7.0
$ ./configure --with-php-config=/usr/bin/php-config7.0
$ make && make install
```

> 这里的 php 版本是 7.0，所以 phpize 和 php-config 的版本也需要保持一致。编译安装完成后，redis 的 php 扩展在 modules 目录中，文件名是 redis.so。

- 查看 php 的扩展目录

```
$ php -i | grep extension_dir
extension_dir => /usr/lib/php/20151012 => /usr/lib/php/20151012
```

> 这里的扩展目录是`/usr/lib/php/20151012`。

- 复制 redis.so 到 php 的扩展目录

```
$ sudo cp ./modules/redis.so /usr/lib/php/20151012
```

#  web模式下配置扩展

- 创建 /etc/php/7.0/fpm/conf.d/20-redis.ini，代码如下：

```
extension=redis.so
```

- 查看 phpinfo

![Screen Shot 2020-08-10 at 1.23.32 PM.png](https://upload-images.jianshu.io/upload_images/15325592-22802c98c6763048.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 如上图所示，成功在 web 模式下配置 redis 扩展。

#  cli模式下配置扩展

- 创建 /etc/php/7.0/cli/conf.d/20-redis.ini，代码如下：

```
extension=redis.so
```

- 查看 php 扩展

```
$ php -m | grep redis
redis
```

> 如上所示，成功在 cli 模式下配置 redis 扩展。
