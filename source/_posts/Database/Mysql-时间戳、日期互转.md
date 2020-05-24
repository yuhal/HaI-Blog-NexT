---
title: Mysql-时间戳、日期互转
categories: Mysql
---

![image](https://upload-images.jianshu.io/upload_images/15325592-f13ad2756074510d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 时间转字符串
```
select date_format(now(), '%Y-%m-%d');
#  结果：2016-01-05  
```

- 时间转时间戳

```
select unix_timestamp(now());  
#  结果：1452001082 
```

- 字符串转时间
```
select str_to_date('2016-01-02', '%Y-%m-%d %H');  
#  结果：2016-01-02 00:00:00  .
```
- 字符串转时间戳
```
select unix_timestamp('2016-01-02');  
#  结果：1451664000 
```
- 时间戳转时间
```
select from_unixtime(1451997924);  
#  结果：2016-01-05 20:45:24  
```
- 时间戳转字符串
```
select from_unixtime(1451997924,'%Y-%d');  
#  结果：2016-01-05 20:45:24  
```


