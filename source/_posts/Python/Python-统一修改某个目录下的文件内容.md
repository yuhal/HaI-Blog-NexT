---
title: Python-统一修改某个目录下的文件内容
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-719743347b40468a?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
# !/usr/bin/python
#  -*- coding: UTF-8 -*-

import os

#  目录路径
path = "_posts/"
#  返回path指定的目录包含的文件或文件夹的名字的列表
articles = os.listdir( path )

#  输出所有文件和文件夹
for article in articles:

	#  分割文件名，获取文件名称及后缀
	articleInfo = article.partition(".") 
	#  拼接文件路径
	articlepath = "_posts/"+article 
	#  打开文件
	fp = file(articlepath) 
	#  读取文件内容
	s = fp.read() 
	#  拼接所要插入的内容
	s = "---\ntitle: "+articleInfo[0]+"\n---\n" + s
	#  打开文件,用于写入
	fp = file(articlepath, 'w')
	#  将所要插入的内容,写入文件
	fp.write(s)
	#  关闭文件
	fp.close()
```
