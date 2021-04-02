---
title: MySQL-实用查询语句
categories: MySQL
---

![WechatIMG255.jpeg](https://upload-images.jianshu.io/upload_images/15325592-36b6a3a84c459642.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 查看所有表信息

```
SELECT
	* 
FROM
	information_schema.TABLES 
WHERE
	TABLE_SCHEMA = '数据库名'
```

- 查看各个表数据量

```
SELECT
	table_name,
	table_rows 
FROM
	information_schema.TABLES 
WHERE
	TABLE_SCHEMA = '数据库名' 
ORDER BY
	table_rows DESC;
```

- 查询数据库中包含某字段的所有表

```
SELECT
	TABLE_NAME,
	TABLE_SCHEMA,
	ORDINAL_POSITION,
	COLUMN_NAME,
	DATA_TYPE,
	CHARACTER_OCTET_LENGTH,
	COLUMN_KEY,
	EXTRA,
	IS_NULLABLE,
	CHARACTER_SET_NAME,
	COLUMN_DEFAULT,
	COLUMN_COMMENT 
FROM
	information_schema.COLUMNS 
WHERE
	TABLE_SCHEMA = '数据库名' 
	AND COLUMN_NAME = '字段名'
```

- 查询表字段名称和类型

```
SELECT
	column_name,
	column_comment,
	data_type 
FROM
	information_schema.COLUMNS 
WHERE
	table_name = '表名' 
	AND table_schema = '数据库名'
```
