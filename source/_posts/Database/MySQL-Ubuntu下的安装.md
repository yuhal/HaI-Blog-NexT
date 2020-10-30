---
title: MySQL-Ubuntu下的安装
categories: MySQL
---
![WechatIMG5.jpeg](https://upload-images.jianshu.io/upload_images/15325592-14bff7e1f348c759.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 更新源

```
$ apt-get update
```

- 安装 MySQL 服务端、核心程序

```
$ apt-get install mysql-server
```

- 安装MySQL客户端

```
$ apt-get install mysql-client
```

- 查看版本

```
$ netstat -tap | grep mysql
mysql  Ver 14.14 Distrib 5.7.16, for Linux (x86_64) using  EditLine wrapper
```

