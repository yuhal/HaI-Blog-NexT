---
title: Django-virtualenv下的环境配置和安装
categories: Django
---
![WechatIMG13.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e3045549f716501f.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  环境

- Python 3.7.7

- Django 2.2.9

> Django 是 Python 的网络应用程序框架，能以最小的代价构建和维护高质量的 Web 应用。

- virtualenv 20.0.18

> virtualenv 是用来为一个应用创建一套虚拟的 Python 运行环境。安装 virtualenv 的步骤参照 [Flask virtualenv下的环境配置和安装](https://www.jianshu.com/p/190aa6e5f8d7 "Flask virtualenv下的环境配置和安装")

- ipython 7.16.1

> wiki:ipython 是一种基于 Python 的交互式解释器。相较于原生的 Python Shell，ipython 提供了更为强大的编辑和交互功能。

- PyMySQL 0.9.3

> PyMySQL 是一个纯 Python 实现的 MySQL 客户端操作库。

#  安装Django


- 安装 


> 在已经启动 virtualenv，并安装过 Python 3 和 pip 的前提下，执行`pip3 install django==2.2.9`，这里安装的 Django 版本是 2.2.9。

- 查看版本

```
$ pip3 freeze | grep Django
Django==2.2.9
(virenv)
```

#  安装ipython

- 安装 

```
pip3 install ipython
```

- 查看版本

```
$ pip3 freeze | grep ipython
ipython==7.16.1
ipython-genutils==0.2.0
(virenv)
```

#  安装PyMySQL

- 安装 

```
pip3 install pymysql
```

- 查看版本

```
$ pip3 freeze | grep PyMySQL
PyMySQL==0.9.3
(virenv)
```

#  创建项目

- 初始化 Django 项目

> 执行`django-admin startproject myProject`会在此目录下生成一个 myProject 文件夹，myProject 就是项目目录名称，可以自定义。

- 查看目录结构

```
$ cd myProject
$ tree
.
|____myProject
| |______init__.py
| |____settings.py
| |____urls.py
| |____wsgi.py
|____manage.py
(virenv)
```

- 创建应用目录

> 在 myProject 目录下执行`python3 manage.py startapp myApp`会在此目录下生成一个 myApp 文件夹，myApp 就是应用目录名称，可以自定义。

- 再次查看目录结构

```
$ tree
.
|____myProject
| |______init__.py
| |____settings.py
| |____urls.py
| |____wsgi.py
|____db.sqlite3
|____myApp
| |____migrations
| | |______init__.py
| |____models.py
| |______init__.py
| |____apps.py
| |____admin.py
| |____tests.py
| |____views.py
|____manage.py
(virenv)
```

- 修改 myProject/myProject/settings.py，内容如下：

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
]
```

> 找到 INSTALLED_APPS 项，添加 myApp，对应刚刚创建的应用名称。

- 访问

![127.0.0.1_8080_.png](https://upload-images.jianshu.io/upload_images/15325592-8d384e4783f9a80f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 在 myProject 目录下执行`python3 manage.py runserver 127.0.0.1:8080`，浏览器打开 [http://127.0.0.1:8080](http://127.0.0.1:8080)，如上图所示，成功访问。
