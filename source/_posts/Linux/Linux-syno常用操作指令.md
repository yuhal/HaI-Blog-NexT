---
title: Linux-syno常用操作指令
categories: Linux
---
![WechatIMG491.jpeg](https://upload-images.jianshu.io/upload_images/15325592-158d8712923dd4b9.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 重启 sshd

```
$ synoservicectl --reload sshd
或者
$ synoservicectl --restart sshd
```

- 切换 root 账户

```
$ sudo -i
Password:输入当前登录用户的密码
```

- 查看当前群晖系统下所有运行的服务

```
$ synoservicecfg --list
```
