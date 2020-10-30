---
title: 杂项-Windows安装WSL
categories: 杂项
---
![WechatIMG188.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e3251bf39f554aa3.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  安装WSL

- 检查

```
> wsl
适用于 Linux 的 Windows 子系统没有已安装的分发版。
可以通过访问 Microsoft Store 来安装分发版:
https://aka.ms/wslstore
```

> `cmd`下执行`wsl`查看 windows 中是否已经安装过 wsl，如上所示，表示没有安装。

- 安装

![2020-09-11_5f5ad3c333631.png](https://upload-images.jianshu.io/upload_images/15325592-332bd33e30c75a25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 https://aka.ms/wslstore 来安装，这里选择`Ubuntu`进行下载安装。

- 启动

![2020-09-11_5f5ad563ba478.png](https://upload-images.jianshu.io/upload_images/15325592-9147c30333cb685e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



> 下载完之后启动，设置用户名密码（适用于 root 用户）。

- 登录

```
> wsl
$ su root
Password:
```

> `cmd`下执行`wsl`登录刚刚设置的用户。若需使用 root 身份，执行`su root`并输入刚刚设置的密码。

#  更新WSL

- 下载

![2020-09-11_5f5b086b95527.png](https://upload-images.jianshu.io/upload_images/15325592-cde75c3c61451a7c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 访问 https://docs.microsoft.com/zh-cn/windows/wsl/wsl2-kernel ，点击`下载适用于 x64 计算机的最新 WSL2 Linux 内核`进行下载。

- 安装

![2020-09-11_5f5b0baca9dbd.png](https://upload-images.jianshu.io/upload_images/15325592-cbe9dd6125a12383.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 安装完后点击`Finish`。


