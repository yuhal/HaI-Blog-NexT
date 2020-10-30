---
title: Python-《Python-实现高德地图找房》实验报告
categories: Python
---
![WechatIMG45.jpeg](https://upload-images.jianshu.io/upload_images/15325592-46447907387b864c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  仓库地址

> [python-rent](https://yuhal.coding.net/public/python-rent/python-rent/git")

#  环境

- Python 3.7.7

- bs4 0.0.1

> Beautiful Soup是一个可以从 HTML 或 XML 文件中提取数据的 Python 库。

- lxml 4.5.2

> lxml XML 工具箱是C库 libxml2 和 libxslt 的 Python 绑定。

#  安装bs4

- 安装

```
$ pip3 install bs4
```

- 查看版本

```
$ python3 -m pip freeze | grep bs4
bs4 0.0.1
```

#  安装lxml

- 安装

```
$ pip3 install lxml
```

- 查看版本

```
$ python3 -m pip freeze | grep lxml
lxml 4.5.2
```

#  运行

- 下载 python-rent

```
$ git clone https://e.coding.net/yuhal/python-rent/python-rent.git
```

- 进入 python-rent 目录

```
$ cd python-rent
```

- 爬取房源信息

```
$ python3 crawl_rent.py
fetch:  https://sh.zu.ke.com/zufang/jinqiao/pg1rp3
fetch:  https://sh.zu.ke.com/zufang/jinqiao/pg2rp3
fetch:  https://sh.zu.ke.com/zufang/jinqiao/pg3rp3
fetch:  https://sh.zu.ke.com/zufang/jinqiao/pg4rp3
......
```

- 访问

```
$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
```

![0.0.0.0_8080_.png](https://upload-images.jianshu.io/upload_images/15325592-6a5bc9e3947c8f68.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 如上所示，成功访问。
