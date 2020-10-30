---
title: Laradock-Ubuntu下的环境配置和安装
categories: Laradock
---

![WechatIMG82.jpeg](https://upload-images.jianshu.io/upload_images/15325592-823c9dde9cf8837c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- 查看 Ubuntu 版本

```
$ lsb_release -a
LSB Version:    core-9.20170808ubuntu1-noarch:security-9.20170808ubuntu1-noarch
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:    18.04
Codename:   bionic
```

- 查看内核版本

```
$ uname -r
4.15.0-48-generic
```

- 查看系统位数

```
$ getconf LONG_BIT
64
```

#  卸载Docker

```
$ apt-get purge docker
$ apt-get purge docker-ce
$ apt-get remove -y docker-*
$ rm -rf /var/lib/docker
```

> 如果系统中存在旧版本的 docker，先进行卸载。

#  安装Docker

- 更新软件源

```
$ apt-get update
```

- 允许 apt 通过 https 使用 repository 安装软件包

```
$ apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

- 添加阿里云版 GPG key

```
$ curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | apt-key add -
OK
```

- 验证key的指纹

```
$ apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
```

- 添加阿里云版 repository

```
$ add-apt-repository \
   "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

- 安装最新版本的 docker-ce 和 containerd

```
$ apt-get install docker-ce docker-ce-cli containerd.io
```

- 查看版本

```
$ docker --version
Docker version 19.03.12, build 48a66213fe
```

#  安装Docker-compose

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

