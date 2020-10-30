---
title: Laradock-CentOS下的环境配置和安装
categories: Laradock
---
![WechatIMG104.jpeg](https://upload-images.jianshu.io/upload_images/15325592-6564c0c848a5a010.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  环境

- 查看 CentOS 版本

```
$ lsb_release -a
LSB Version:	:core-4.1-amd64:core-4.1-noarch
Distributor ID:	CentOS
Description:	CentOS Linux release 7.3.1611 (Core)
Release:	7.3.1611
Codename:	Core
```

- 查看内核版本

```
$ uname -r
3.10.0-514.26.2.el7.x86_64
```

- 查看系统位数

```
$ getconf LONG_BIT
64
```

#  安装系统工具

- 安装 yum-utils

```
$ yum install -y yum-utils device-mapper-persistent-data lvm2 git
```

>  yum-util 提供yum-config-manager功能，管理 repository 及扩展包的工具。

- 安装 device-mapper-persistent-data 和 lvm2

```
$ yum install -y device-mapper-persistent-data lvm2 git
```

> device mapper 存储驱动程序需要 device-mapper-persistent-data 和 lvm2。

- 安装 git

```
$ yum install -y git
```

#  安装Docker

- 添加软件源信息

```
$ yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

- 更新并安装 Docker-CE

```
$ yum makecache fast && yum -y install docker-ce
```

- 开启 Docker 服务

```
$ service docker start
```

- 查看版本

```
$ docker --version
docker-compose version 1.24.0, build 0aa59064
```

#   安装Docker-compose

- 国内镜像下载

```
$ curl -L https://get.daocloud.io/docker/compose/releases/download/1.24.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
```

- 设置可运行

```
$ chmod +x /usr/local/bin/docker-compose
```

- 查看版本

```
$ docker-compose --version
docker-compose version 1.24.0, build 0aa59064
```

#  安装Laradock

- 克隆

```
$ git clone https://gitee.com/mirrors/Laradock.git
```

- 进入 Laradock 目录

```
$ cd Laradock
```

- 复制 env-example 配置文件，命名为 .env

```
$ cp env-example .env
```

- 修改 Laradock/.env

```
#  启用更改源
CHANGE_SOURCE=true
#  设置composer下载镜像
WORKSPACE_COMPOSER_REPO_PACKAGIST=https://mirrors.aliyun.com/composer
#  设置node下载镜像
WORKSPACE_NVM_NODEJS_ORG_MIRROR=https://npm.taobao.org/mirrors/node
#  关闭安装项
WORKSPACE_INSTALL_NPM_GULP=false
```

- 编译

```
$ docker-compose build nginx
$ docker-compose build php-fpm
$ docker-compose build workspace
```

> 因为编译过程是比较缓慢，这里建议同时开三个窗口分别执行。

- 启动

```
$ docker-compose up -d nginx mysql
```

#  安装Laravel

- 进入容器

```
$ docker-compose exec workspace bash
```

- composer 设置国内镜像

```
/var/www#  composer config -g repo.packagist composer https://mirrors.aliyun.com/composer
```

- composer 安装最新版本的 laravel

```
/var/www#  composer create-project --prefer-dist laravel/laravel
```

- 修改 laravel/storage 目录权限

```
/var/www#   chmod 777 -R laravel/storage
```

#  启动项目

- 进入 Laradock/nginx/sites 目录

```
$ cd Laradock/nginx/sites
```

- 复制 laravel.conf.example 配置文件，命名为 118.31.23.98.conf

```
$ cp laravel.conf.example 118.31.23.98.conf
```

> 这里命令的文件名称是该服务器的IP地址。

- 修改 118.31.23.98.conf 配置文件

```
#  设置服务器访问地址
server_name 118.31.23.98;
```

- 修改 /etc/hosts 文件，新加入一行`127.0.0.1 118.31.23.98`

- 进入 Laravel 目录

```
$ cd Laravel
```

- 复制 .env.example 配置文件，命名为 .env

```
$ cp .env.example .env
```

- 修改 Laravel/.env

```
#  项目地址
APP_URL=http://118.31.23.98
#  mysql数据库连接
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=root
```

- 重新构建 nginx 并重启

```
$ docker-compose build nginx && docker-compose restart nginx
```

- 访问

![laravel.test_.png](https://upload-images.jianshu.io/upload_images/15325592-62f358c1780161c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 浏览器打开 http://118.31.23.98 ，如上图所示，成功访问。
