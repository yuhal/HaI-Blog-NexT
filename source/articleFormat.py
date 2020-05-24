#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

if __name__ == '__main__':
    # 目录路径
    path = "_posts/"
    # 返回path指定的目录包含的文件或文件夹的名字的列表
    categories = os.listdir(path)
    # 输出所有文件和文件夹
    for category in categories:
        # 目录路径
        categoryPath = "_posts/"+category+"/"
        if os.path.isdir(categoryPath) :
            # 返回path指定的目录包含的文件或文件夹的名字的列表
            articles = os.listdir(categoryPath)
            # 输出所有文章
            for article in articles:
                # 分割文件名，获取文件名称及后缀
                articleInfo = article.partition(".")
                # 分割文件名称，获取标题及分类
                articleNameInfo = articleInfo[0].partition("-") 
                # 拼接文件路径
                articlepath = categoryPath+article 
                # 打开文件
                fp = file(articlepath) 
                # 读取文件内容
                s = fp.read() 
                # 判断文件内容是否为空，为空则
                if len(s) == 0 :
                    os.remove(articlepath)
                else:
                    # 插入查看更多<!-- more -->
                    s = s.replace("?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)", 
                    "?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)\n<!-- more -->")
                    # 拼接所要插入的内容
                    s = "---\ntitle: "+articleInfo[0]+"\ncategories: "+articleNameInfo[0]+"\n---\n" + s
                    s = s.replace("###","3井")
                    s = s.replace("##","2井")
                    s = s.replace("#","# ")
                    s = s.replace("3井","### ")
                    s = s.replace("2井","## ")
                    # 打开文件,用于写入
                    fp = file(articlepath, 'w')
                    # 将所要插入的内容,写入文件
                    fp.write(s)
                    # 关闭文件
                    fp.close()
