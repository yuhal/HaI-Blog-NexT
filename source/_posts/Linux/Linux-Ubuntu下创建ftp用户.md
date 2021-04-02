---
title: Linux-Ubuntu下创建ftp用户
categories: Linux
---
![2020-12-03_5fc85f02ec11e.jpeg](https://upload-images.jianshu.io/upload_images/15325592-12a225a0241f761c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- Ubuntu 18.04 64位

- vsftp

#  安装vsftp

- 安装

```
$ apt-get install vsftpd
```

> 若没有安装 vsftpd，先执行上述命令安装，安装后默认启动。

- 查看状态

```
$ service vsftpd status
```

- 查看 vsftpd 端口占用情况

```
$ netstat -tunlp | grep 'vsftpd'
tcp6       0      0 :::21                   :::*                    LISTEN      1798/vsftpd
```


#  创建ftp用户

- 新增用户

```
$ useradd -d /mnt/ftp01 ftp01
```

> 新增用户 ftp01，并设置 ftp01 用户的主目录为 /home/ftp01。

- 修改用户的主目录(可跳过)

```
$ usermod -d /home/ftp01 ftp01
```

- 设置密码

```
$ passwd
```

- 更改用户登录权限

```
$  usermod -s /bin/bash ftp01
```

| 权限设置  | ftp 连接  | sftp 连接  |ssh 连接  |
| ------------ | ------------ | ------------ |------------ |
|  usermod -s /sbin/nologin | 可以| 不可以|不可以|
|  usermod -s /bin/bash |  可以| 可以|可以|
|  usermod -s /sbin/bash |  可以| 可以|不可以|

> 到目前为止，ftp01 用户已经创建完成了，可以使用 ftp01 进行 ftp、sftp、ssh 的连接。

#  ftp限制访问目录

> 设置 ftp01 在进行 ftp 连接的时候，只能访问主目录。

- 修改 /etc/vsftpd.conf

```
chroot_list_enable=YES
#  设置是否启用chroot_list_file配置项指定的用户列表文件，如果启动这项功能，则所有列在chroot_list_file之中的使用者不能更改根目录，默认值为YES。
chroot_list_file=/etc/vsftpd.chroot_list
#  指定被限制访问目录的用户列表文件。
```

- 修改 /etc/vsftpd.chroot_list

```
ftp01
```

> 若没有该文件，手动创建。把被限制访问目录的用户添加进去，一个用户单独占一行。

- 重启 vsftp

```
$ service vsftpd restart
```

#  测试连接

- ftp 连接

![2020-12-02_5fc73615d90f3.png](https://upload-images.jianshu.io/upload_images/15325592-4efb3fd1a395ce5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![2020-12-02_5fc73631af202.png](https://upload-images.jianshu.io/upload_images/15325592-bfe048f1c00b404e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> ftp连接，设置连接模式为主动。使用 ftp01 用户连接后只能访问主目录，无法切换其他目录。

| 连接失败情况  | 解决方案  |
| ------------ | ------------ |
|  “尝试连接“ETIMEDOUT | 检查是否向所有IP开放21端口  |
|  331 Please specify the password | 删除 /etc/pam.d/vsftpd  |


- sftp 连接

![2020-12-02_5fc73b03cd3f0.png](https://upload-images.jianshu.io/upload_images/15325592-17d2e590969cc941.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> sftp 连接，使用 ftp01 用户连接后默认访问主目录，可以切换其他目录。

- ssh 连接

```
$ ssh ftp01@192.168.0.1
```

>  ssh 连接，使用 ftp01 用户连接默认访问主目录，可以切换其他目录。
