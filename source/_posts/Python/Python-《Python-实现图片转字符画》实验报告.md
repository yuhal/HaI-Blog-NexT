---
title: Python-《Python-实现图片转字符画》实验报告
categories: Python
---
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
#  -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
parser.add_argument('--width', type = int, default = 80) # 输出字符画宽
parser.add_argument('--height', type = int, default = 80) # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM# *oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#  将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
```
> 创建 ascii.py，内容如上。

#  执行

- 图片


![](https://upload-images.jianshu.io/upload_images/15325592-3684b10af709b4d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 准备一张图片，放在与 ascii.py 同级目录下。

- 执行

```
$ python3 ascii.py Rabbit.png --width=80 --height=50
```

![Screen Shot 2020-07-21 at 11.33.02 AM.png](https://upload-images.jianshu.io/upload_images/15325592-a13ae4fb385bfed2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

