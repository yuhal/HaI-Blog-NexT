---
title: Yaf-Windows下的环境配置和安装
categories: Yaf
---

![QQ图片20200615154444.png](https://upload-images.jianshu.io/upload_images/15325592-88cf4ae404a2c6b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

![QQ截图20200615104437.png](https://upload-images.jianshu.io/upload_images/15325592-8bfbd51b6e330b1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


| 参数  |值| 说明  |
| ------------ | ------------ |------------ |
|  Compiler |  MSVC14 (Visual C++ 2015) |运行库的版本|
|  Architecture | 	x86  | 操作系统的版本 <br/>x86对应32位 <br/>x64对应64位 |
|Zend Extension Build	|API320151012,NTS,VC14| Zend 引擎对应的扩展的版本 |
|PHP Extension Build	|API20151012,NTS,VC14| PHP 引擎对应的扩展的版本|
|Thread Safety	|disabled|线程安全的开启与禁用|

> 输出 phpinfo，查看本地 php 的一些参数信息如上。

#  安装扩展

- 下载 

![QQ图片20200615112056.png](https://upload-images.jianshu.io/upload_images/15325592-a579a5e64aeebbec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 打开 http://pecl.php.net/package/yaf ，选择对应的 yaf 扩展的版本点击`DLL`，这里选择的版本是 `3.0.3 `

![QQ图片20200615113243.png](https://upload-images.jianshu.io/upload_images/15325592-81afdf6d52a6ba91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 再根据本地的 php 参数信息来选择对应的扩展包，这里下载的扩展包是`7.0 Non Thread Safe (NTS) x86`

- 安装

 将下载的压缩包进行解压，把里面的`php_yaf.dll`文件复制到对应 `php` 版本的 `ext` 目录下。

![QQ图片20200615114131.png](https://upload-images.jianshu.io/upload_images/15325592-e07400b6792c6c83.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 修改对应`php`版本的`php.ini`文件，找到`extension`这个位置，新添加一行`extension=php_yaf.dll`后保存。

![QQ图片20200615115544.png](https://upload-images.jianshu.io/upload_images/15325592-55b4d80f4e513610.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 重启 php 后，再次输出 phpinfo，查看已经存在 yaf 扩展信息。

#  安装源码

- 下载 

![QQ图片20200615131829.png](https://upload-images.jianshu.io/upload_images/15325592-c57bf656bfd6b425.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 打开 https://github.com/laruence/yaf ，下载压缩包。根据`README.md`描述，`php7`及以上的版本下载`master`分支，`php5.2`及以上的版本下载[php5分支](https://github.com/laruence/yaf/tree/php5 "php5分支")。这里下载的是 master 分支。

- 安装

![QQ图片20200615133547.png](https://upload-images.jianshu.io/upload_images/15325592-cd116caaa01d4e0c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 将下载的压缩包进行解压，进入解压后的`yaf-master\tools\cg`目录下。然后使用快捷键`Shift+鼠标右键`，在弹出的选项中点击`在此处打开 Powershell 窗口`。

![QQ图片20200615134255.png](https://upload-images.jianshu.io/upload_images/15325592-e03704efb2f78bc1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 如上图所示，成功使用 Powershell 窗口访问到`yaf-master\tools\cg`目录。

#  创建项目

- 环境变量

```
PS C:\HaI\2020\jun15\yaf-master\yaf-master\tools\cg> php -v
php : 无法将“php”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，
然后再试一次。
所在位置 行:1 字符: 1
+ php -v
+ ~~~
+ CategoryInfo          : ObjectNotFound: (php:String) [], CommandNotFoundException
+ FullyQualifiedErrorId : CommandNotFoundException
```

> 在创建项目前，先执行`php -v`检测下有没有配置`php环境变量`。若未成功输出 php 版本信息，表示没有配置环境变量或者环境变量配置错误，如何配置请参考[PHP Windows下配置环境变量](https://www.jianshu.com/p/146465b16b55 "PHP Windows下配置环境变量")。

```
PS C:\HaI\2020\jun15\yaf-master\yaf-master\tools\cg> php -v
PHP 7.0.12 (cli) (built: Oct 13 2016 11:04:07) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
```

> 若成功输出 php 版本信息，表示已经配置了环境变量。

- 生成项目

```
PS C:\HaI\2020\jun15\yaf-master\yaf-master\tools\cg> php yaf_cg -a test -d test
Outputing Yaf Skeleton to test
Generating done
```

> 执行`php yaf_cg -a test -d test`，成功在同级目录下生成了`test`文件夹，该文件夹就是项目目录。

- yaf_cg 参数介绍

| 参数  | 说明  |
| ------------ | ------------ |
| -a  |  项目名称，默认是 yaf_skeleton |
| -d  | 生成项目的路径，默认是同级目录路径  |

#  访问项目

![2020-06-15_5ee71ac756503.png](https://upload-images.jianshu.io/upload_images/15325592-5063d60dba9aa877.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 将`localhost`地址指向`test`根目录，浏览器打开 http://localhost/test ，如上图所示，成功访问。

