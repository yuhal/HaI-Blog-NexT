---
title: Go-Mac下的环境配置和安装
categories: Go
---

![2020-11-03_5fa0d5ce19ae4.jpeg](https://upload-images.jianshu.io/upload_images/15325592-7aa47290b7c26789.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- 查看 Mac 版本

```
$ sw_vers
ProductName:    Mac OS X
ProductVersion: 10.14.6
BuildVersion:   18G103
```

- 查看 Homebrew 版本

```
$ brew -v
Homebrew 2.4.10-8-gb447f57-dirty
Homebrew/homebrew-core (git revision 3a70e32; last commit 2020-08-11)
Homebrew/homebrew-cask (git revision 9e987; last commit 2020-08-11)
```

#  安装

- 使用 Homebrew 安装

```
$ brew install go
```

- 查看版本

```
$ go version
go version go1.14.6 darwin/amd6
```

