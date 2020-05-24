---
title: Linux-crontab启动关闭重启操作
categories: Linux
---
![image](https://upload-images.jianshu.io/upload_images/15325592-0c9be744b1e7b5b6?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 1.在系统中有service这个命令时：
```
# 这个命令在red hat当中常用,有的linux发行版本中没有这个命令.
service crond start //启动服务
service crond stop //关闭服务
service crond restart //重启服务
```
 
# 2.linux发行版本没有service这个命令时：
```
/etc/init.d/cron stop
/etc/init.d/cron start
```
 
# 3.执行出现 /bin/systemctl 。。。。说明是新版的可用以下命令操作
```
/bin/systemctl restart crond.service  # 启动服务
/bin/systemctl reload  crond.service  # 重新载入配置
/bin/systemctl status  crond.service  # 查看crontab服务状态
```

转载[https://blog.csdn.net/qq_24909089/article/details/80020800](https://blog.csdn.net/qq_24909089/article/details/80020800)
