---
title: Laradock-Windows下的环境配置和安装
categories: Laradock
---
![WechatIMG122.jpeg](https://upload-images.jianshu.io/upload_images/15325592-51be0564d8cb9fa0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  环境

- 查看 windows 系统信息

![D204EDD0-0843-4DB4-B885-17CF111A4A9D.png](https://upload-images.jianshu.io/upload_images/15325592-f48489da83904dac.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 按照流程`控制面板`->`系统和安全`->`系统`查看 windows 系统信息，如上图所示。

- 查看 windows 版本号

![2020-09-11_5f5ad11f3c54b.png](https://upload-images.jianshu.io/upload_images/15325592-092b819d03fdca5b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> `cmd`下执行`winver`查看 windows 版本号。windows10 家庭版安装 docker，版本号必须在`19018`以上。如需升级 windows10 版本请访问 https://www.microsoft.com/en-us/software-download/windows10 。

#  安装WSL

> 安装 WSL 的教程参照 [Windows 安装WSL](https://www.jianshu.com/p/be3acbf85460)

#  安装Git

> 安装 Git 的教程参照 [Git Windows下快速安装](https://www.jianshu.com/p/9a9b999c7d8b)

#  安装Docker

- 下载

![WechatIMG116.png](https://upload-images.jianshu.io/upload_images/15325592-a0c0eaf44ac9987c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 https://www.docker.com/products/docker-desktop ，选择 WINDOWS 下的 Stable 版本。

- 安装

![7A10FC13-50CE-490A-8CF9-A4791E7B6F02.png](https://upload-images.jianshu.io/upload_images/15325592-bf8f6c35dee22456.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![30B77401-2D56-42C1-9E41-8AF4FC6D243C.png](https://upload-images.jianshu.io/upload_images/15325592-9c937ee799ddafe0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 如上图所示，点击 OK 开始安装。安装完成后需要重启 Windows，点击 Close and restart。


- 配置镜像加速器

![035F42D3-5419-4969-84BB-F9E72B2B2DDF.png](https://upload-images.jianshu.io/upload_images/15325592-acbab6cc07b63158.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Screen Shot 2020-08-26 at 10.59.27 AM.png](https://upload-images.jianshu.io/upload_images/15325592-0596a5f50f4c0d3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 如上图所示，在系统右下角托盘图标内右键菜单选择 Settings，打开配置窗口后，在左侧导航菜单选择 Docker Engine，在右侧输入栏编辑`json`文件。将`阿里云镜像加速器地址`添加到`registry-mirrors`的数组里，点击 Apply & Restart 按钮，等待 Docker 重启并应用配置的镜像加速器。`阿里云镜像加速器地址`可以在阿里云控制台的`容器镜像服务`中获得。

- 查看 docker 版本

```
$ docker --version
Docker version 19.03.12, build 48a66213fe
```

- 查看 docker-compose 版本

```
$ docker-compose --version
docker-compose version 1.26.2, build eefe0d31
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

- 进入 Laradock/workspace 目录

```
$ cd workspace
```

- 使用 vim 修改 sources.sh 

![2020-09-11_5f5b0f3a47494.png](https://upload-images.jianshu.io/upload_images/15325592-9d11c099a93ca498.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 如上图所示，如果高亮区块显示的是`sources.sh[dos]`，则直接输入`:set ff=unix`回车，然后输入`:wq`回车保存。

- 再次修改 sources.sh 查看

![2020-09-11_5f5b0eb7f2edd.png](https://upload-images.jianshu.io/upload_images/15325592-51131d15dccce69b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 如上图所示，高亮区块显示已被修改为`sources.sh[unix]`。

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

> ![D25E7766-CA40-423B-A1F0-5A5E90CA3706.png](https://upload-images.jianshu.io/upload_images/15325592-15e4a9ecb9414e77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
如出现上图，点击 Share it。

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
