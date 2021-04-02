---
title: Python-SJTU作业整合
categories: Python
---

![2020-11-10_5faa3d0d4d6e3.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e99ebc72dfe80abc.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

> Python 3

#  作业

```
while语句和do…while 语的区别在于____。
选择一项：
a. do…while语句编写程序较复杂。
b. while语句的执行效率较高。
c. do…while循环是先执行循环体，后判断条件表达式是否成立，而while语句是先判断条件表达式，再决定是否执行循环体。 正确
d. 无论条件是否成立，while语句都要执行一次循环体。
```

> 创建 homework.txt，内容如上。

#  代码

```
# !/usr/bin/python
#  -*- coding:utf-8 -*-
import re
import os
import sys

#  打开文件
file = open('homework.txt')
#  行列表
line_list = []
#  无用列表
useless_list = ['选择一项：\n','题干\n','\n']
#  结果列表
outcome_list = ['不正确','正确']
#  选项列表
option_list = ['a.','b.','c.','d.']

#  过滤一些干扰的数据
for line in file.readlines():
    for outcome in outcome_list:
        for option in option_list:
            if line.find(outcome) >= 0 and line.find(option) >= 0 :
                line = line.replace(outcome,'')
    if line not in useless_list:
        line_list.append(line)

#  关闭文件
file.close()

#  d. 选项后追加换行
for i in range(0,len(line_list)):
    if line_list[i].find("d. ") != -1:
        line_list[i] = line_list[i]+"\n"

file = open('homework.txt', 'w')

#  拼接文件内容
file_content = ''.join(line_list)
#  题列表
question_list = file_content.split('\n\n')
#  排序
question_list.sort()
#  添加序号
for i in range(0,len(question_list)):
    question_list[i] = str(i+1)+'、'+question_list[i]
#  写入文件 
file.write('\n\n'.join(question_list))
file.close()
```

> 创建 homework.py，代码如上。

#  执行

```
$ python3 homework.py
```

#  完成

```
1、while语句和do…while 语的区别在于____。
a. do…while语句编写程序较复杂。
b. while语句的执行效率较高。
c. do…while循环是先执行循环体，后判断条件表达式是否成立，而while语句是先判断条件表达式，再决定是否执行循环体。 
d. 无论条件是否成立，while语句都要执行一次循环体。
```

> 再次查看 homework.txt，内容如上。
