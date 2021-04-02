---
title: Git-常用命令
categories: Git
---

![WechatIMG265.jpeg](https://upload-images.jianshu.io/upload_images/15325592-b07a819d3648a252.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 下载一个项目和它的整个代码历史

```
$ git clone 远程仓库地址
```

- 添加当前目录的所有文件到暂存区

```
$ git add .
```

- 提交暂存区到仓库区

```
$ git commit -m 提交信息
```

- 上传到远程仓库

```
$ git push
```

- 本地代码回退到上一个版本

```
$ git reset --hard HEAD^
```

- 强制覆盖本地代码

```
git fetch --all && git reset --hard origin/master && git pull
```

> 以上是 Git 常用的几个命令，更多可以参照[《阮一峰的网络日志》
](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html "阮一峰的网络日志")
