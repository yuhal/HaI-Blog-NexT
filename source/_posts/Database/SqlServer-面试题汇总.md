---
title: SqlServer-面试题汇总
categories: SqlServer
---
![WechatIMG264.jpeg](https://upload-images.jianshu.io/upload_images/15325592-a23ffc41803a7547.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


### 1.SqlServer2012系统数据类型有哪些？

| 数据类型 | 符号标识  |
| ------------ | ------------ |
| 数据类型 | bigint、int、smallint、tinyint |
| 整数型精确数值型 | decimal、numeric |
| 浮点型 | float、real |
| 货币型 | money、smallmoney |
| 位型 | bit |
| 字符型 | char、varchar、varchar(MAX) |
| Unicode字符型 | nchar、nvarchar、nvarchar(MAX) |
| 文本型 | text、ntext |
| 日期时间类型 | datetime、smalldatetime、date、time、datetime2、datetimeoffset |
| 时间截型 | timestamp |
| 图像型 | image |
| 其他 | cursor、sql_variant、table、uniqueidentifier、xml、hierarchyi |

### 2.写出创建产品销售数据厍cpxs中所有表的SQL语句。其所包含的表如下。

产品表:产品编号，产品名称，价格，库存量。
销售商表:客户编号，客户名称，地区，负责人，电话。
产品销售表:销售日期，产品编号，客户编号，数量，销售额。

```
CREATE TABLE [dbo].[product] (
	[产品编号] char(12) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[产品名称] char(20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[价格] money NULL DEFAULT ((0)),
	[库存量] smallint NULL DEFAULT ((0))
)
ON [PRIMARY]
GO
ALTER TABLE [dbo].[product] SET (LOCK_ESCALATION = TABLE)
GO
EXEC sp_addextendedproperty 'MS_Description', '产品表', 'SCHEMA', 'dbo', 'TABLE', 'product'

CREATE TABLE [dbo].[seller] (
	[客户编号] char(8) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[客户名称] char(4) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[地区] char(10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	[负责人] char(4) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	[电话] char(11) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
)
ON [PRIMARY]
GO
ALTER TABLE [dbo].[seller] SET (LOCK_ESCALATION = TABLE)
GO
EXEC sp_addextendedproperty 'MS_Description', '销售商表', 'SCHEMA', 'dbo', 'TABLE', 'seller'

CREATE TABLE [dbo].[product_sales] (
	[销售日期] datetime NOT NULL,
	[产品编号] char(12) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[客户编号] char(8) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	[数量] smallint NULL DEFAULT ((0)),
	[销售额] money NULL DEFAULT ((0))
)
ON [PRIMARY]
GO
ALTER TABLE [dbo].[product_sales] SET (LOCK_ESCALATION = TABLE)
GO
EXEC sp_addextendedproperty 'MS_Description', '产品销售表', 'SCHEMA', 'dbo', 'TABLE', 'product_sales'
```

### 3.在第2题中所创建的cpxs数据库的产品表中增加”产品简介“列，之后在删除该列。

```
ALTER TABLE [dbo].[product]
	ADD [产品简介] text

ALTER TABLE [dbo].[product]
    DROP COLUMN [产品简介]
```

### 4.写出SQL语句，对产品销售数据库产品表进行如下操作。

(1)插入如下记录。

| 产品编号 | 产品名称 | 价格 | 库存量 |
| ------------ | ------------ | ------------ | ------------ |
| 0001 | 空调 | 3000 | 200 |
| 0203 | 电冰箱 | 2500 | 100 |
| 0301 | 彩色电视机 | 2800 | 50 |
| 0421 | 微波炉 | 1500 | 50 |

```
insert into [dbo].[product] values 
( '0001', '空调', '3000', '20'),
( '0203', '电冰箱', '2500', '100'),
( '0301', '彩色电视机', '2800', '50')
( '0421', '微波炉', '1500', '50')
;
```

(2)将产品数据库的产品表中每种商品的价格打8折

```
UPDATE [dbo].[product] SET [价格]=[价格]*0.8
```

(3)将产品数据库的产品表中价格打8折后低于50元的商品删除

```
DELETE [dbo].[product] WHERE [价格]<50
```

(4)查找价格在2000~2900元之间的商品名。

```
SELECT [产品名称] FROM [dbo].[product] WHERE [价格] BETWEEN 2000 AND 2900
```

(5)计算所有商品的总价格。

```
SELECT SUM([价格]*[库存量]) FROM [dbo].[product] 
```

(6)在产品销售数据库上创建电冰箱产品表的视图bxcp。

```
CREATE VIEW [dbo].[bxcp] AS SELECT
dbo.product.*
FROM
dbo.product
WHERE
[产品名称]='电冰箱'
```

(7)在bxcp视图中查询库存量在100台以下的产品编号。

```
SELECT * FROM [dbo].[bxcp] WHERE [库存量]<100
```

### 5.使用EXISTS关键字引入的子查询与使用IN关键字引入的子查询在语法上有哪些不同？

```
// EXISTS 方式
SELECT * FROM A WHERE EXISTS(SELECT * FROM B WHERE B.id=A.uid); 
// in  方式
SELECT * FROM A WHERE id IN (SELECT id  FROM B);
``` 

### 6. WHERE子句与HAVING子句有何不同?

Where是一个约束声明，是在查询结果集返回之前约束来自数据库的数据，且Where中不能使用聚合函数。
Having是一个过滤声明，是在查询结果集返回以后对查询结果进行的过滤操作，在Having中可以使用聚合函数。

### 7.试说明游标的种类和用途。

种类：前端（客户端）游标、后端（服务器端）游标
用途：游标提供了对一个结果集进行逐行处理的能力，游标可看做一种特殊的指针，它与某个查询结果相联系，可以指向结果集的任意位置，以便对指定位置的数据进行处理。

### 8.举例说明游标的使用方法和步骤。

- 声明游标
- 打开游标
- 读取数据
- 关闭游标
- 删除游标

