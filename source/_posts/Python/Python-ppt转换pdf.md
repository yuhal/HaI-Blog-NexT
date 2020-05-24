---
title: Python-ppt转换pdf
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-609a76220722d815.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境
- Windows Server  2016 数据中心版 64位中文版
- Python 3.8.1
- WPS 2019
#  安装python
[python下载地址](https://www.python.org/downloads/windows/)
![www.python.org_downloads_windows_.png](https://upload-images.jianshu.io/upload_images/15325592-83eac3ddee090c06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
![www.python.org_downloads_release_python-381_.png](https://upload-images.jianshu.io/upload_images/15325592-86addfa8b35a4512.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 点击最新的Python 3版本：Python 3.8.1，点击Windows x86-64 executable installer下载。详细安装转送[windows下安装Python](https://www.jianshu.com/p/542f32ec5c59)
#  安装pip
[pip下载地址](https://pypi.org/project/pip/# files)
![pypi.org_project_pip_.png](https://upload-images.jianshu.io/upload_images/15325592-f102d80b54163172.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 点击pip-10.0.1.tar.gz下载，解压后，在解压的根目录下执行以下命令。
```
python setup.py install
```
#  安装python包
```
pip install PyWin32 Pillow reportlab
```
#  下载ppt2pdf程序
```
git clone https://github.com/ernestyao/PPT2PDF.git
```
#  执行脚本
```
D:\PPT2PDF>python PPT2PDF.py test.pptx test.pdf 
test 
水印完成 
准备生成D:\PPT2PDF\test.pdf 
D:\PPT2PDF\test\幻灯片1.PNG 
D:\PPT2PDF\test\幻灯片2.PNG 
D:\PPT2PDF\test\幻灯片3.PNG 
D:\PPT2PDF\test\幻灯片4.PNG 
D:\PPT2PDF\test\幻灯片5.PNG 
D:\PPT2PDF\test\幻灯片6.PNG 
完成PDF合成
```














