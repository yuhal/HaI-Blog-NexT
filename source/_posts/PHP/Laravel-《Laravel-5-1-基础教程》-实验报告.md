---
title: Laravel-《Laravel-5-1-基础教程》-实验报告
categories: Laravel
---

![WechatIMG23.jpeg](https://upload-images.jianshu.io/upload_images/15325592-3e8d9eaefaf2e260.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Laravel 5.1 基础教程.jpg](https://upload-images.jianshu.io/upload_images/15325592-2829e46d9243d0c3.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 根目录文件夹

```
├── app
#  网站的业务逻辑代码，例如：控制器/模型/路由等
├── bootstrap
#  框架启动与自动加载设置相关的文件
├── config
#  网站的各种配置文件
├── database
#  数据库操作相关的文件
├── public
#  网站的对外文件夹，入口文件和静态资源（CSS，JS，图片等）
├── resources
#  前端视图文件和原始资源（CSS，JS，图片等）
├── storage
#  编译后的视图、基于会话、文件缓存和其它框架生成的文件
├── tests
#  自动化测试文件
└── vendor
#  Composer 依赖文件
```

- 根目录常用文件

```
├── .env	
#  环境配置文件
├── .env.example	
#  .env 文件的一个示例
├── .gitignore	
#  git 的设置文件，制定哪些文件会被 git 忽略，不纳入文件管理
├── composer.json	
#  网站所需的 composer 扩展包
├── composer.lock	
#  扩展包列表，确保这个网站的副本使用相同版本的扩展包
├── gulpfile.js	
#  GULP 配置文件
├── package.json	
#  网站所需的 npm 包
└── readme.md	
#  网站代码说明文件
```

- artisan 常用命令

| 命令  | 说明  |
| ------------ | ------------ |
|php artisan key:generate    |生成 App Key|
|php artisan make:controller |生成控制器|
|php artisan make:model  |生成模型|
|php artisan make:policy |生成授权策略|
|php artisan make:seeder |生成 Seeder 文件|
|php artisan migrate |执行迁移|
|php artisan migrate:rollback    |回滚迁移|
|php artisan migrate:refresh |重置数据库|
|php artisan db:seed |填充数据库|
|php artisan tinker  |进入 tinker 环境|
|php artisan route:list  |查看路由列表|
