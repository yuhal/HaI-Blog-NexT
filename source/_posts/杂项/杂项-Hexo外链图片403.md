---
title: 杂项-Hexo外链图片403
categories: 杂项
---
![WechatIMG254.jpeg](https://upload-images.jianshu.io/upload_images/15325592-6b55ebcca23e6a15.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- hexo: 4.2.1

- hexo-cli: 4.2.0

#  问题

![2020-10-28_5f9910d74fdfc.png](https://upload-images.jianshu.io/upload_images/15325592-18b3b333e8bafa97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 http://localhost:4000/ ，发现访问图片都是403，原因是引入了外链图片，hexo 无法访问。

#  解决

- 修改 themes/next/layout/_layout.swig 文件

```
<meta name="referrer" content="no-referrer"/>
```

> 在 <head></head> 中加入上述代码。

- 重新生成网站静态文件

```
$ hexo g
```

> 再次访问后，图片正常显示。
