---
title: MySql-查询表信息
categories: MySql
---

![image](https://upload-images.jianshu.io/upload_images/15325592-1be1b3a9889908d5?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
 
# 查看所有表信息
```
SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'pcms-zgh20190327'
```
# 查看各个表数据量
```
SELECT table_name,table_rows FROM information_schema.tables
WHERE TABLE_SCHEMA = 'pcms-zgh20190327' ORDER BY table_rows DESC;
```
# 查询数据库中包含某字段（列名）的所有表
```
SELECT   TABLE_NAME '表名',TABLE_SCHEMA '数据库名',ORDINAL_POSITION '顺序',COLUMN_NAME '字段',DATA_TYPE '类型' 
,CHARACTER_OCTET_LENGTH '字节长',IF(COLUMN_KEY='PRI',"√","") '主键',IF(EXTRA='auto_increment',"√","") '自增长' 
,IF(IS_NULLABLE='YES',"√","") '空',CHARACTER_SET_NAME '编码',COLUMN_DEFAULT '默认值',COLUMN_COMMENT '说明' 
FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='dzbbs' AND COLUMN_NAME='username'
```
上述是查询数据库名为dzbbsdb的数据库中所有包含username列名的表信息。
# mysql查询表字段名称，字段类型
```
select column_name,column_comment,data_type 
from information_schema.columns 
where table_name='查询表名称' and table_schema='数据库名称'
```
# mysql 追加某列的值
```
 update xtable set xfiled =concat(xfiled,'-s1')
```
