---
title: Python-No-module-named-'pip-_internal'
categories: Python
---

![WechatIMG3.jpeg](https://upload-images.jianshu.io/upload_images/15325592-f601e5dbfc13c5a7.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境
- ubuntu 18.04
- python 3.8.2

#  错误
![2020-03-26_5e7c0d8115c05.png](https://upload-images.jianshu.io/upload_images/15325592-8b09726b9e9e6a85.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 在执行`pip install python-pptx`的时候，报错：`No module named 'pip._internal'`

#  解决
- 找到相应报错的/bin/下的 pip，我这里的目录是`/home/yuhal/.local/bin/pip`
- 修改此文件`vim /home/yuhal/.local/bin/pip`

```
# !/usr/bin/python

#  -*- coding: utf-8 -*-
import re
import sys

from pip._internal.cli.main import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

- 将`from pip._internal import main`注释掉,改成`from pip import main`保存退出

```
# !/usr/bin/python

#  -*- coding: utf-8 -*-
import re
import sys

#  from pip._internal.cli.main import main
from pip import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

#  成功
![image.png](https://upload-images.jianshu.io/upload_images/15325592-efeaa1fc2dd3ebd4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 执行`which pip`检查一下是否是正确路径
