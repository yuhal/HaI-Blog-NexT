---
title: Python-UnicodeEncodeError--'ascii'-codec-can't-encode-characters
categories: Python
---
![WechatIMG9.jpeg](https://upload-images.jianshu.io/upload_images/15325592-30afd22211956045.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  环境

- ubuntu 16.04
- python 3.5.2

#  代码

```
if __name__ == '__main__':
    text = "阳光下的小海儿"
    print(text)
```

#  错误

```
$ python simple.py
Traceback (most recent call last):
  File "simple.py", line 3, in <module>
    print(text)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-6: ordinal not in range(128)
```

> 在执行 python 文件的时候，报错：`UnicodeEncodeError: 'ascii' codec can't encode characters`，原因是中文字符编码的问题。

#  解决方案一

```
$ PYTHONIOENCODING=utf-8 python simple.py
阳光下的小海儿
```

> 在所要执行的 python 文件前加上`PYTHONIOENCODING=utf-8`，如上可以正常输出。

#  解决方案二

- 更改 simple.py，内容如下：

```
import sys

import codecs

if __name__ == '__main__':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    text = "阳光下的小海儿"
    print(text)
```

- 执行

```
$ python simple.py
阳光下的小海儿
```
