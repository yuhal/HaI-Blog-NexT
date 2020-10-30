---
title: Django-《Django-基础入门》实验报告
categories: Django
---
![WechatIMG15.jpeg](https://upload-images.jianshu.io/upload_images/15325592-0ada61390fb661dd.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 目录结构

```
|____myProject
#  主目录名称
| |______init__.py
#  每个子目录都会包含这样一个 __init__.py 文件，它是一个空文件，在需要的时候会引入目录下的对象。
| |____settings.py
#  配置文件，里面包含对数据库的设置项、CSRF Token 的设置项、模板的设置项等全部设置。
| |____urls.py
#  路由控制文件，处理客户端请求，分发到对应的视图函数去处理。
| |____wsgi.py
#  处理请求和响应。
|____myApp
#  应用目录名称
| |____migrations
#  用于记录数据库变更信息的目录，Django 中自带的数据库版本控制功能就体现在这个目录。
| | |______init__.py
| |____models.py
#  创建映射类的文件。
| |______init__.py
| |____apps.py
#  用于管理应用本身的文件，包括应用的名字如何命名，默认就是它本身 。
| |____admin.py
#  用于控制后台管理的文件。
| |____tests.py
#  编写测试代码的文件。
| |____views.py
#  创建视图函数的文件，视图函数用于处理客户端发来的请求。
|____manage.py
#  项目的入口文件，用来创建应用、启动项目、控制数据表迁移等。
```

- MTV 模式

| 名称  |说明   |
| ------------ | ------------ |
| M   |  模型（Model）,负责业务对象和数据库的关系映射。 |
|  T |模板（Template）,负责如何把页面展示给用户。   |
|  V |   视图（View）,负责业务逻辑，并在适当时候调用模型和模板。|

- URL 分发器

> URL 分发器相当于一个路由器，其作用是定义相应的路由，将页面请求匹配路由分发给不同的视图 View 处理，视图再调用相应的模型 Model 和模板 Template。

- 流程图

![Django流程图.jpg](https://upload-images.jianshu.io/upload_images/15325592-ff869bd1d280892c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



