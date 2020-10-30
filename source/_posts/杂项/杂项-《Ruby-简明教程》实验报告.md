---
title: 杂项-《Ruby-简明教程》实验报告
categories: 杂项
---
![WechatIMG4.jpeg](https://upload-images.jianshu.io/upload_images/15325592-0cfb753c6b82fb09.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Ruby 简明教程 (1).png](https://upload-images.jianshu.io/upload_images/15325592-40103552de9e403b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  转义字符

|  符号 | 描述  |
| ------------ | ------------ |
|\a	|报警符
|\b	|退格
|\f	|换页符
|\n	|换行符
|\r	|回车符
|\s	|空格符
|\t	|制表符
|\v	|垂直制表符符

#  String 内置方法

|  方法 | 说明  |
| ------------ | ------------ |
|reverse |倒序|
|delete |删除字符|
|sub |替换 |

#  Array 创建方式

|  Array 创建方式 |  说明  |  
| ------------ | ------------|  
|array_1 = Array.new     |创建一个数组
|array_2 = Array.new(10) | 创建一个有 10 个元素的数组
|array_3 = Array.new(4,"test") |4 个元素，每个元素都是 'test'
|array_4 = Array[1,2,3,4]  |4 个元素的数组，给每个元素赋值

#  Array 内置方法

|  方法 | 说明  |
| ------------ | ------------ |
|&  |数组交集|
|+ |数组连接|
|I|数组合并，去除重复|
|-| 数组相减 |
|delete_at |去除数组某个元素|
|insert |数组插入元素|
|sort|数组排序|

#  Hash 创建方式 

|  Hash 创建方式 |  说明  |  
| ------------ | ------------|  
|hash_1 = Hash.new     | 创建一个 Hash
|hash_2 = Hash.new("date") | 创建一个默认值是 date 的 Hash
|hash_3 = Hash[<br/>"y"=>"year", <br/>"m"=>"month"<br/>] | 第1对:key=y, value=year <br/> 第2对:key=m, value=month
