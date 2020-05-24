---
title: Python-数组和字符串互相转换
categories: Python
---

![image](https://upload-images.jianshu.io/upload_images/15325592-2d0c62e5b4aa5439.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 字符串转数组
```
str = '1,2,3'
arr = str.split(',')
```

- 数组转字符串
```
arr = ['a','b']
str = ','.join(arr)

arr = [1,2,3]
str = ','.join(str(i) for i in b)
```
