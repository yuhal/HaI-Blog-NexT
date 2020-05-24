---
title: Linux--dhpcd导致cpu飙升问题
categories: Linux
---

![image](https://upload-images.jianshu.io/upload_images/15325592-d4e76a075e0341d4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 系统```Ubuntu 16.04 64位```
> 项目部署在阿里云服务器上，阿里云后台报警有恶意程序在“挖矿”，登录阿里云后台喵下，cpu持续高达50%。
![image.png](https://upload-images.jianshu.io/upload_images/15325592-3bd3042866622bda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 查看资源情况```top```
```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  2628 test      20   0 2410400  81940  16176 S   384.3  0.5  46:02.78 .dhpcd
```
> 看到一个名为.dhpcd的进程，进程号为2628，cpu飙至384%，所属用户为test。
- 查看该服务的位置```ls -l /proc/2628/exe```
```
lrwxrwxrwx 1 test test 0 Dec 16 17:37 /proc/2628/exe -> /home/test/.dhpcd
```
- 删除此进程
```
kill -9 2595
```
- 删除.dhpcd文件
```
rm /home/test/.dhpcd
```
- 删除test用户
```
userdel -r test
```
> 黑客利用手段创建的test用户，通过test用户植入.dhpcd，导致cpu飙升，为避免下次在通过test植入挖矿、病毒、木马等程序，将test用户删除。



