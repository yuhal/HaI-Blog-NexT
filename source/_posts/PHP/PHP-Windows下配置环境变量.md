---
title: PHP-Windows下配置环境变量
categories: PHP
---
![WechatIMG2.jpeg](https://upload-images.jianshu.io/upload_images/15325592-2416244a421f9533.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 配置

![2020-06-15_5ee71102225f8.png](https://upload-images.jianshu.io/upload_images/15325592-5ee9c0ba82fa0c40.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 按照流程`我的电脑`->`属性`->`高级系统设置`->`环境变量`打开配置环境变量的窗口，如上图所示。然后选中`Path`一栏，点击`编辑`。

![2020-06-15_5ee7132b79b63.png](https://upload-images.jianshu.io/upload_images/15325592-5d059bee63ef44ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 在`编辑环境变量`的窗口中，点击`新建`，然后把对应`php`版本的`php.exe`所在的目录路径粘贴进去，点击`确定`。

- 测试

```
C:\Users\86157>php -v
PHP 7.0.12 (cli) (built: Oct 13 2016 11:04:07) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
```

> 使用`Win+R`快捷键，输入`cmd`打开 dos 命令窗口。再执行`php -v`检测环境变量是否配置成功，若成功输出 php 版本信息，表示配置成功。
