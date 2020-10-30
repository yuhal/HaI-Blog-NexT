---
title: MySQL-查询不重复的记录
categories: MySQL
---
![1957C40DB512B1C6E93CCDD5F0D616D8.png](https://upload-images.jianshu.io/upload_images/15325592-63c3c5d09f360217.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 场景

> 查询最近上课的同学信息，包括同学姓名、最近一次的上课时间、上课记录ID。

- 表结构

|字段|类型|空|默认|注释|
|------|------|------|------|------|
|id    |int(10)     |否 |NULL  |    上课记录ID         |
|name  |char(10) |否 |   NULL |   同学姓名  |
|time |int(11)     |否   |NULL  |   上课时间  |

>class_record 上课记录表

- 表数据

|上课记录ID|同学姓名|上课时间|
|------|------|------|
|1	|柯南	|1558368000
|2	|柯南	|1579536000
|3	|元太	|1558368000
|4	|元太	|1582214400
|5	|步美	|1558368000
|6	|步美	|1584720000
|7	|小哀	|1558368000
|8	|小哀	|1587398400
|9	|光彦	|1558368000
|10|	光彦	|1589990400

- 查询语句

```
SELECT
	max( class_record.time ) AS maxtime,
	from_unixtime( max( class_record.time ), '%Y-%m-%d' ) AS maxdate,
	class_record.name,
	class_record.id 
FROM
	class_record 
WHERE
	NOT EXISTS (  
		SELECT
			1 
		FROM
			class_record AS class_record_2 
		WHERE
			class_record_2.name = class_record.name 
			AND class_record.time < class_record_2.time
	) 
GROUP BY
	class_record.name 
ORDER BY
	maxtime ASC
```

- 查询结果

|最近上课时间(时间戳)|最近上课时间(日期)|同学姓名|上课记录ID|
|------|------|------|------|
|1579536000	|2020-01-21	|柯南	|2
|1582214400	|2020-02-21	|元太	|4
|1584720000	|2020-03-21	|步美	|6
|1587398400	|2020-04-21	|小哀	|8
|1589990400	|2020-05-21	|光彦	|10
