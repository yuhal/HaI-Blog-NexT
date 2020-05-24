---
title: python-cannot-import-name-'sysconfig'-from-'distutils'
categories: python
---

![image](https://upload-images.jianshu.io/upload_images/15325592-a092ef8b166424bb.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境
- Ubuntu 18.04
- Python 3.8.2

#  错误
![2020-03-25_5e7b2231a391a.png](https://upload-images.jianshu.io/upload_images/15325592-b9d309e369b1a103.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 查看pip版本的时候，执行`pip -V`
> 报错`cannot import name 'sysconfig' from 'distutils'`

#  解决
- 添加源（原有基础上）
```
sudo vim /etc/apt/sources.list
```

- 把下面的内容插入到sources.list中去
```
deb http://cn.archive.ubuntu.com/ubuntu bionic main multiverse restricted universe
deb http://cn.archive.ubuntu.com/ubuntu bionic-updates main multiverse restricted universe
deb http://cn.archive.ubuntu.com/ubuntu bionic-security main multiverse restricted universe
deb http://cn.archive.ubuntu.com/ubuntu bionic-proposed main multiverse restricted universe
```

- update更新命令
```
sudo apt-get update
```

- 安装pip3
```
sudo apt-get install python3-pip
```

#  成功
![2020-03-25_5e7b274f316b9.png](https://upload-images.jianshu.io/upload_images/15325592-38f31fbe014fa6ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 再次查看pip版本，可以看到正常返回pip版本信息
