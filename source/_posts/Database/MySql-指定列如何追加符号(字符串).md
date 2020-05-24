---
title: MySql-指定列如何追加符号(字符串)
categories: MySql
---
![image](https://upload-images.jianshu.io/upload_images/15325592-82cb5c71f50b08f4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
MySQL追加字符串不能使用加号(+)，而是使用concat。
比方在aa表的name字段前加字符'x'，使用：
```
update aa set name=concat('x',name)
```
