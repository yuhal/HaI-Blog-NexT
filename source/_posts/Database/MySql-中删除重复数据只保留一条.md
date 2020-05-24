---
title: MySql-中删除重复数据只保留一条
categories: MySql
---
 ![image](https://upload-images.jianshu.io/upload_images/15325592-5f9414e0c90e40c5?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

用SQL语句,删除掉重复项只保留一条

在几千条记录里,存在着些相同的记录,如何能用SQL语句,删除掉重复的呢 
1、查找表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断
```
SELECT
    *
FROM
    people
WHERE
    peopleId IN (
        SELECT
            peopleId
        FROM
            people
        GROUP BY
            peopleId
        HAVING
            count(peopleId) > 1
    )
```
2、删除表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断，只留有rowid最小的记录
```
DELETE
FROM
    people
WHERE
    peopleName IN (
        SELECT
            peopleName
        FROM
            people
        GROUP BY
            peopleName
        HAVING
            count(peopleName) > 1
    )
AND peopleId NOT IN (
    SELECT
        min(peopleId)
    FROM
        people
    GROUP BY
        peopleName
    HAVING
        count(peopleName) > 1
)
```
3、查找表中多余的重复记录（多个字段）
```
SELECT
    *
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
```
4、删除表中多余的重复记录（多个字段），只留有rowid最小的记录
```
DELETE
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
AND rowid NOT IN (
    SELECT
        min(rowid)
    FROM
        vitae
    GROUP BY
        peopleId,
        seq
    HAVING
        count(*) > 1
)
```
5、查找表中多余的重复记录（多个字段），不包含rowid最小的记录
```
SELECT
    *
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
AND rowid NOT IN (
    SELECT
        min(rowid)
    FROM
        vitae
    GROUP BY
        peopleId,
        seq
    HAVING
        count(*) > 1
)
```
6.消除一个字段的左边的第一位：
```
UPDATE tableName
SET [ Title ]= RIGHT ([ Title ],(len([ Title ]) - 1))
WHERE
    Title LIKE '村%'

```
7.消除一个字段的右边的第一位：
```
UPDATE tableName
SET [ Title ]= LEFT ([ Title ],(len([ Title ]) - 1))
WHERE
    Title LIKE '%村'
```
8.假删除表中多余的重复记录（多个字段），不包含rowid最小的记录
```
UPDATE vitae
SET ispass =- 1
WHERE
    peopleId IN (
        SELECT
            peopleId
        FROM
            vitae
        GROUP BY
            peopleId
```

转载[https://www.cnblogs.com/jiangxiaobo/p/6589541.html](https://www.cnblogs.com/jiangxiaobo/p/6589541.html)
