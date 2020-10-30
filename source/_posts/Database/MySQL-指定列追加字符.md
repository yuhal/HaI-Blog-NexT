---
title: MySQL-指定列追加字符
categories: MySQL
---
![WechatIMG257.jpeg](https://upload-images.jianshu.io/upload_images/15325592-3f4bf0e9bc671f6e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  场景

> 在一些已存在的记录中，追加相同的字符并修改。

#  数据模型

- pearl 珍珠表

|id|name|
|------|------|
|1	|红	|
|2	|金	|
|2	|银	|

#  示例

- 修改语句

```
update pearl set name=concat(name,"色珍珠")
```

- 修改结果

|id|name|
|------|------|
|1	|红色珍珠	|
|2	|金色珍珠	|
|3	|银色珍珠	|
