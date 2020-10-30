---
title: Laradock-Mac下的环境配置和安装
categories: Laradock
---
![WechatIMG73.jpeg](https://upload-images.jianshu.io/upload_images/15325592-3daf5d54d7197622.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境


- 查看 Mac 版本

```
$ sw_vers
ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G103
```

- 查看内核版本

```
$ uname -r
18.7.0
```

- 查看系统位数

```
$ getconf LONG_BIT
64
```

#  安装Docker

- 下载并安装 [docker-for-mac](http://mirrors.aliyun.com/docker-toolbox/mac/docker-for-mac/stable/Docker.dmg "docker-for-mac")

- 配置镜像加速器

![Screen Shot 2020-08-24 at 11.57.10 AM.png](https://upload-images.jianshu.io/upload_images/15325592-3a8ffb3a5b5051b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 如上图所示，在任务栏点击 Docker Desktop 应用图标 -> Perferences，在左侧导航菜单选择 Docker Engine，在右侧输入栏编辑`json`文件。将`阿里云镜像加速器地址`添加到`registry-mirrors`的数组里，点击 Apply & Restart 按钮，等待 Docker 重启并应用配置的镜像加速器。

- 查看 docker 版本

```
$ docker --version
Docker version 19.03.12, build 48a66213fe
```

- 查看 docker-compose 版本

```
$ docker-compose --version
docker-compose version 1.24.1, build 4667896b
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

- composer 安装 laravel

```
/var/www#  composer create-project --prefer-dist laravel/laravel
```

#  启动项目

- 进入 Laradock/nginx/sites 目录

```
$ cd Laradock/nginx/sites
```

- 复制 laravel.conf.example 配置文件，命名为 laravel.conf

```
$ cp laravel.conf.example laravel.conf
```

- 修改 /etc/hosts 文件，新加入一行`127.0.0.1 laravel.test`

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
APP_URL=http://laravel.test
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

> 浏览器打开 http://laravel.test ，如上图所示，成功访问。
