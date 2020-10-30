---
title: MySQL-中删除重复数据只保留一条
categories: MySQL
---
![WechatIMG256.jpeg](https://upload-images.jianshu.io/upload_images/15325592-4e84af7e8d0771f0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  场景

> 在许多条记录里，存在着些相同的记录，使用SQL语句，删除掉重复项只保留一条。

#  数据模型

- half_demon 半妖表

|id|name|weapon|skill|
|------|------|------|------|
|1	|永远	|菊十文字|苍龙破|
|2	|诸叶	|弓箭|苍穹箭雨|
|3	|诸叶	|俱利伽罗丸|红龙破|
|4	|刹那	|兼光之巴|旋风阵|
|5	|刹那	|兼光之巴|宿蛾之月|

#  单字段示例

- 查询语句

```
SELECT
	id,name 
FROM
	half_demon 
WHERE
	name IN ( SELECT name FROM half_demon GROUP BY name HAVING count( name ) > 1 )
```

> 查找表中多余的重复记录，重复记录是根据单个字段`name`来判断。

- 查询结果

|id|name|weapon|skill|
|------|------|------|------|
|2	|诸叶	|弓箭|苍穹箭雨|
|3	|诸叶	|俱利伽罗丸|红龙破|
|4	|刹那	|兼光之巴|旋风阵|
|5	|刹那	|兼光之巴|宿蛾之月|

- 删除语句

```
DELETE 
FROM
	half_demon 
WHERE
	id NOT IN ( SELECT hd.minid FROM ( SELECT MIN( id ) AS minid FROM half_demon GROUP BY name ) hd )
```

> 删除表中多余的重复记录，重复记录是根据单个字段`name`来判断，只留有`id`最小的记录。

- 删除结果

|id|name|weapon|skill|
|------|------|------|------|
|1	|永远	|菊十文字|苍龙破|
|2	|诸叶	|弓箭|苍穹箭雨|
|4	|刹那	|兼光之巴|旋风阵|

#  多字段示例

- 查询语句

```
SELECT
    id,
    name,
    weapon 
FROM
    half_demon a 
WHERE
    ( a.name, a.weapon ) IN ( SELECT name, weapon FROM half_demon GROUP BY name, weapon HAVING count( * ) > 1 )
```

> 查找表中多余的重复记录，重复记录是根据多个字段`name、weapon`来判断。

- 查询结果

|id|name|weapon|skill|
|------|------|------|------|
|4	|刹那	|兼光之巴|旋风阵|
|5	|刹那	|兼光之巴|宿蛾之月|


- 删除语句

```
DELETE 
FROM
    half_demon 
WHERE
    ( name, weapon ) IN (
SELECT
    t.name,
    t.weapon 
FROM
    ( SELECT name, weapon FROM half_demon GROUP BY name, weapon HAVING count( 1 ) > 1 ) t 
    ) 
    AND id NOT IN ( SELECT hd.minid FROM ( SELECT min( id ) AS minid FROM half_demon GROUP BY name, weapon HAVING count( 1 ) > 1 ) hd )
```

>删除表中多余的重复记录，重复记录是根据多个字段`name、weapon`来判断，只留有`id`最小的记录。

- 删除结果

|id|name|weapon|skill|
|------|------|------|------|
|1	|永远	|菊十文字|苍龙破|
|2	|诸叶	|弓箭|苍穹箭雨|
|3	|诸叶	|俱利伽罗丸|红龙破|
|4	|刹那	|兼光之巴|旋风阵|
