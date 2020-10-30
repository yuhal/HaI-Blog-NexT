---
title: Python-抓取微信文章图片
categories: Python
---
![WechatIMG194.jpeg](https://upload-images.jianshu.io/upload_images/15325592-49fed539dab3dd7a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  Python 抓取微信文章图片

- 创建 crawl_image.py，代码如下。

```
#  -*- coding: utf-8 -*-
#  !python3
import re
import os
import ssl
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    '''
    Get page information
    '''
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getimgURL(html):
    '''
    Parse the webpage and get all the image urls
    '''
    soup = BeautifulSoup(html , "html.parser")
    adlist = []
    for i in soup.find_all("img"):
        try:
            ad = re.findall(r'.*src="(.*?)?" .*',str(i))
            if ad :
                adlist.append(ad)
        except:
            continue
    del adlist[-1]
    return adlist

# 
def download(adlist):
    '''
    Create a new folder pic,download and 
    save the crawled picture information
    '''
    root = "pic/"
    for i in range(len(adlist)):
        path = root+str(i)+"."+'png'
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(adlist[i][0])
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://mp.weixin.qq.com/s/5A8ooI15XtS6FR3yo4AHpg'
html = getHTMLText(url)
list = getimgURL(html)
download(list)
```

- 执行

```
$ python3 crawl_image.py
```

- 查看 pic 目录

```
$ ls pic
0.png 1.png 2.png 3.png 4.png 5.png 6.png 7.png
```
