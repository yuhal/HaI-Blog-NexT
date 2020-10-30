---
title: Python-《Python-识别登录验证码》实验报告
categories: Python
---
![WechatIMG16.jpeg](https://upload-images.jianshu.io/upload_images/15325592-279bd1e3a0aee4b7.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  仓库地址

> [python-captcha](https://yuhal.coding.net/public/python-captcha/python-captcha/git/files "python-captcha")

#  环境

- Python 3.5.2

- Pillow 7.2.0

> Pillow 是一个 Python 图像处理库。

#  安装Pillow

- 安装

```
pip3 install pillow
```

- 查看版本

```
$ python3 -m pip freeze | grep Pillow
Pillow==7.2.0
```

#  代码

```
#  -*- coding:utf8 -*-
from PIL import Image
import hashlib
import time
import os
import math
import string

class VectorCompare:
    '''
    向量空间类
    '''
    def magnitude(self, concordance):
        '''
        计算矢量大小
        '''
        total = 0
        for word, count in concordance.items():
            total += count ** 2 #  返回count的2次幂
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        '''
        计算矢量之间的cos值
        '''
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

def buildvector(image):
    '''
    将图片转换为矢量
    '''
    d1 = {}
    count = 0
    for i in image.getdata():
        d1[count] = i
        count += 1
    return d1

def letterIconset():
    '''
    字符图标集合
    '''
    #  需要训练的字符
    iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    #  字符训练集目录
    letterPath = 'iconset'
    #  加载训练集
    captchaList = []
    for letter in iconset:
        for img in os.listdir(letterPath+'%s/'%(letter)):
            temp = []
            if img.endswith(".gif"): #  过滤非gif格式的文件
                temp.append(buildvector(Image.open(letterPath+'%s/%s'%(letter, img))))
            captchaList.append({letter:temp})
    return captchaList

def pixelCollection(blackWhiteCaptcha):
    '''
    得到单个字符的像素集合
    '''
    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []
    for y in range(blackWhiteCaptcha.size[0]):
        for x in range(blackWhiteCaptcha.size[1]):
            pix = blackWhiteCaptcha.getpixel((y, x))
            if pix != 255:
                inletter = True

        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter=False
    return letters

def blackWhite(captcha):
    '''
    构造一张黑白二值图片
    '''
    blackWhiteCaptcha = Image.new("P", captcha.size, 255)
    #  将图片转换为8位像素模式
    captcha.convert("P")
    temp = {}
    for x in range(captcha.size[1]):
        for y in range(captcha.size[0]):
            pix = captcha.getpixel((y, x))
            temp[pix] = pix
            if pix == 220 or pix == 227: #  这些是要得到的数字
                blackWhiteCaptcha.putpixel((y, x), 0)
    return blackWhiteCaptcha

def identifyCaptcha(captcha):
    '''
    识别验证码
    '''
    #  黑白二值图片中字符的像素信息
    blackWhiteCaptcha = blackWhite(captcha)
    #  单个字符的像素集合
    letters = pixelCollection(blackWhiteCaptcha)
    #  字符图标集合
    captchaList = letterIconset()
    #  向量空间
    v = VectorCompare()
    #  识别字符个数
    count = 0
    #  识别验证码
    guessLetter = ''
    for letter in letters:
        m = hashlib.md5()
        image = blackWhiteCaptcha.crop((letter[0], 0, letter[1], blackWhiteCaptcha.size[1]))
        guess = []

        for captcha in captchaList:
            for x, y in captcha.items():
                if len(y) != 0:
                    guess.append((v.relation(y[0], buildvector(image)), x))

        guess.sort(reverse=True)
        guessLetter += guess[0][1]
        count += 1
    return count,guessLetter

#  打开一张验证码图
captcha = Image.open("captcha.gif")
#  识别验证码返回结果
result = identifyCaptcha(captcha)
print("识别出%d位验证码：%s"%(result))
```

> 创建 captcha.py，内容如上。

#  执行

- 验证码

![captcha.gif](https://upload-images.jianshu.io/upload_images/15325592-ceca2f38abbdefef.gif?imageMogr2/auto-orient/strip)


> 准备一张验证码图片，放在与 captcha.py 同级目录下。

- 执行

```
$ python3 captcha.py
识别出6位验证码：7s9t9j
```
