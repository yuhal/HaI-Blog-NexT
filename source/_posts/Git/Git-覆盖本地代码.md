---
title: Git-覆盖本地代码
categories: Git
---

![image](https://upload-images.jianshu.io/upload_images/15325592-f95542a1d92c68be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 执行命令
```
git fetch --all
git reset --hard origin/master
git pull
// 或者
git fetch --all && git reset --hard origin/master && git pull
```
