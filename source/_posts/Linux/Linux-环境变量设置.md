---
title: Linux-环境变量设置
categories: Linux
---

![image](https://upload-images.jianshu.io/upload_images/15325592-7d419af058f0d2be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 执行vim /etc/profile，添加如下：
```
PATH=$PATH:路径# 多个用冒号':'分割
export PATH

# 例如PHP环境变量设置如下
PATH=$PATH:/usr/local/php/bin
export PATH
```
- 保存退出

- 执行source /etc/myprofile

