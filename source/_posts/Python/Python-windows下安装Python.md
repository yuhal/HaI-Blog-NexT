---
title: Python-windows下安装Python
categories: Python
---
![image](https://upload-images.jianshu.io/upload_images/15325592-2b9add750386dc05.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  下载Python安装包
在Python的官网 [www.python.org](www.python.org) 中找到最新版本的Python安装包，点击进行下载，请注意，当你的电脑是32位的机器，请选择32位的安装包，如果是64位的，请选择64位的安装包。
#  安装
- 双击下载好的安装包，弹出如下界面：
![image](https://upload-images.jianshu.io/upload_images/15325592-61d8937479b44b4c?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 这里要注意的是，将python加入到windows的环境变量中，如果忘记打勾，则需要手工加到环境变量中；在这里我选择的是自定义安装，点击“自定义安装”进行下一步操作。
- 进入到下一步后，选择需要安装的组件，然后点击下一步:
![image](https://upload-images.jianshu.io/upload_images/15325592-2eb6b0da63154bde?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 在这里可以自定义路径选择安装：
![image](https://upload-images.jianshu.io/upload_images/15325592-2f6f1dc9e87c1985?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 点击下一步后，就开始真正安装了：
![image](https://upload-images.jianshu.io/upload_images/15325592-e99fcc966cf67e8e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 安装完成后，会有一个安装成功的提示界面：
![image](https://upload-images.jianshu.io/upload_images/15325592-77fc1ee84c4aa7d6?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  测试
> python安装好之后，我们要检测一下是否安装成功，用系统管理员打开命令行工具cmd，输入```python -V```,然后敲回车，如果出现如下界面，则表示我们安装成功了；
![image](https://upload-images.jianshu.io/upload_images/15325592-f34940428e42a014?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  写程序
> 还是打开cmd，输入“python”后敲回车， 进入到python程序中，可以直接在里面输入，然后敲回车执行程序，我们打印一个“hello world”看看，在里面输入 print("hello world")，敲回车；
![image](https://upload-images.jianshu.io/upload_images/15325592-fc7e91ba0093cf71?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  配置python环境变量
> 如果在刚才安装的时候，忘记将加入到环境变量的勾打上，那么就需要手工配置环境变量之后，才能使用python，配置的方法如下：
- 右键点击“我的电脑”，点击“属性”；
![image](https://upload-images.jianshu.io/upload_images/15325592-a429162238194bad?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 在弹出的界面中点击“高级系统设置”![image](https://upload-images.jianshu.io/upload_images/15325592-dc15775690435bf7?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 在弹出的界面中点击“环境变量”；
![image](https://upload-images.jianshu.io/upload_images/15325592-f791d9ccadd8e4e1?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 在弹出的页面中进行环境变量的配置； 
![image](https://upload-images.jianshu.io/upload_images/15325592-e9c2087f9ee46405?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
> 找到系统变量中“Path”一项，选中后点击“编辑”；将之前安装的phtyon的完整路径加到最后面，注意要在完整的路径前加一个“;”，然后点击“确定”，保存所做的修改，这样，环境变量就设置好了；
设置完成后，可以按照上面的方法进行测试，以确保环境变量设置正确；

[转载](https://baijiahao.baidu.com/s?id=1606573927720991570&wfr=spider&for=pc)



