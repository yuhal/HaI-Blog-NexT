---
title: SQLAlchemy-《SQLAlchemy-基础教程》实验报告
categories: SQLAlchemy
---
![WechatIMG21.jpeg](https://upload-images.jianshu.io/upload_images/15325592-9ee2e525830d13a1.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![SQLAlchemy 基础教程.jpg](https://upload-images.jianshu.io/upload_images/15325592-f92712dc1c7cb914.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 常用的定义列参数列表

| 参数  | 说明  |
| ------------ | ------------ |
|primary_key	|如果设为 True，这列就是表的主键
|unique	|默认值为 False，如果设为 True，这列不允许出现重复的值
|index	|如果设为 True，为这列创建索引，提升查询效率
|nullable	|默认值为 True，这列允许使用空值；如果设为 False，这列不允许使用空值
|default	|为这列定义默认值

- 常用的查询关系选项

| 选项  | 说明  |
| ------------ | ------------ |
|backref	|在关系的另一个映射类中添加反向引用|
|lazy	|指定如何加载查询记录|
|cascade	|设置级联删除的方式|
|uselist	|如果设为 False ，查询结果不使用列表，而使用映射类实例|
|order_by	|指定查询记录的排序方式|
|secondary	|指定多对多关系中关系表的名字|


