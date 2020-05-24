---
title: TP5-mkdir()-Permission-denied问题
categories: TP5
---

![image](https://upload-images.jianshu.io/upload_images/15325592-487cb66bba2a2ea8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

最近一直在用tp5写项目，在此遇到的问题也比较多。今天来谈谈“mkdir() Permission denied”错误。
你如果不仅仅写代码，还得部署到线上，那么这个tp5的这个错误，你有很大概率会遇见它。
因为这跟文件的权限有关系，特别是自动生成的文件或者目录类的权限，linux服务器出于安全因素对于用户的权限有着严格的控制。
对于tp框架而言，自动生成的文件或者目录应该是runtime目录，所以在线部署代码的时候，开放此类目录的权限。
所以解决mkdir() premission denied 的问题最直接的方式，把runtime权限放开，让所有用户都可以创建它。
```
chmod -R 777 runtime
```
在liunx中进入项目目录执行以上命令，就能解决这个问题，简单，高效。
如果你对文件的安全要求比较苛刻，那么以上的答案并不能令你满意，简单，高效的方法背后一般需要牺牲一些安全因素为代价。
但以下提供的方法或许是一个不错的选择。
更改runtime目录的所有者，也就是runtime这个目录权限只针对所有者开放。
以我的项目为例，服务器是nginx，nginx中设置的访问用户为www用户，那么我只需要把runtime目录有root用户改为www用户就能解决此问题。
```
ps aux|grep nginx 
//查看当前的nginx进程，能够找到nginx用户是哪个（可能是www,user或者其他的）
chown -R www runtime 
//chown -R <nginx 用户> runtime,改变runtime所有者为nginx用户
```
ok，进入项目目录去执行上面的命令吧，是否有效一试便知。
