---
title: Python-urllib3-({0})-or-chardet-({1})-doesn't-match-a-supported
categories: Python
---
![WechatIMG2.jpeg](https://upload-images.jianshu.io/upload_images/15325592-8e82c0f2ff595578.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境
- ubuntu 18.04
- python 3.8.2

#  错误
![2020-03-26_5e7c3b5eda82e.png](https://upload-images.jianshu.io/upload_images/15325592-9dff4e248ceb71d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 在执行 python 文件的时候，报错：`urllib3 ({0}) or chardet ({1}) doesn't match a supported`，原因是  python 库中 urllib3 (1.24.1) 或者 chardet (3.0.4) 的版本不兼容

#  解决
- 重新安装requests
`pip install request`

- 卸载urllib3与chardet
```
pip uninstall urllib3
pip uninstall chardet
```

#  成功
![2020-03-26_5e7c3b7c280f3.png](https://upload-images.jianshu.io/upload_images/15325592-8420d14d8a21a71d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 再次执行 python 无报错信息
