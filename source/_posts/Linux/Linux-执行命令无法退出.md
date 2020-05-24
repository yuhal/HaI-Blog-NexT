---
title: Linux-执行命令无法退出
categories: Linux
---

![WechatIMG8.jpeg](https://upload-images.jianshu.io/upload_images/15325592-45d5aa926d1c1e3c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# Linux 执行命令无法退出

# 问题
```
HaI:~ root#  ls -l'
>
>
>
```
>在执行命令的时候，因为手误打了 单引号 或 双引号 后回车，导致无法退出

# 解决
```
HaI:~ root#  ls -l'
>
>
>'
HaI:~ root# 
```
>再次输入 单引号 或 双引号 回车就可以了
