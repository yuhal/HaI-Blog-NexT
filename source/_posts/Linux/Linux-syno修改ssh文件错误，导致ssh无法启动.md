---
title: Linux-syno修改ssh文件错误，导致ssh无法启动
categories: Linux
---
![WechatIMG492.jpeg](https://upload-images.jianshu.io/upload_images/15325592-79507e8aab07398d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 最近在操作 syno，尝试修改 sshd_config 文件实现 ftp 链接。可能由于操作不当，重启后 ssh 无法启动，由此记录下当时的解决方案。

- telnet 登录服务器

```
> telnet 192.168.50.37
DS218play login:输入用户名
Password:输入密码
```

> 首先确保 windows 的 telnet 功能是开启的状态，在 windows 下打开 cmd 命令行，使用 telnet 命令登录服务器。

- 修复 sshd_config

```
$ vi /etc/ssh/sshd_config
```

> 把刚刚改动的部分恢复原状，有备份的话直接替换备份的 sshd_config 文件。

- 启动 ssh

![2021-02-07_601fa5d2d94d2.png](https://upload-images.jianshu.io/upload_images/15325592-9f76d11f28712edb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 如图所示，启动成功。

- ssh 登录服务器

```
$ ssh root@192.168.50.1
root@192.168.50.1's password:输入密码
```

> ssh 启动后，可以成功访问。
