---
title: Linux-convert：memory-allocation-failed
categories: Linux
---
![image](https://upload-images.jianshu.io/upload_images/15325592-35e88577d6508da1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 执行convert命令将pdf文件转换为png
```
convert -density 300 -quality 100 xxx.pdf xxx.png
```
- 转换失败，返回如下错误信息
```
convert: DistributedPixelCache '127.0.0.1' @ error/distribute-cache.c/ConnectPixelCacheServer/217.
convert: cache resources exhausted `xxx.png' @ error/cache.c/OpenPixelCache/3657.
convert: memory allocation failed `xxx.png' @ error/png.c/WriteOnePNGImage/8899.
```
- 解决办法，找到policy.xml文件位置
```
locate policy.xml
//返回如下
/etc/ImageMagick-6/policy.xml
```
- 更改以下几项配置信息的value值并保存
```
//修改前
<policy domain="resource" name="memory" value="10MiB"/>
<policy domain="resource" name="map" value="10MiB"/>
<policy domain="resource" name="width" value="32KP"/>
<policy domain="resource" name="height" value="32KP"/>
<policy domain="resource" name="area" value="10MB"/>
//修改后（根据使用情况进行修改）
<policy domain="resource" name="memory" value="1024MiB"/>
<policy domain="resource" name="map" value="1024MiB"/>
<policy domain="resource" name="width" value="256KP"/>
<policy domain="resource" name="height" value="256KP"/>
<policy domain="resource" name="area" value="256MB"/>
```
- 再次执行convert命令将pdf文件转换为png，转换成功


