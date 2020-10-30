---
title: Linux-添加开机启动脚本
categories: Linux
---
![image](https://upload-images.jianshu.io/upload_images/15325592-3753be6b8d8d06d7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 查看权限

- 执行命令```ll /etc/rc.local```

```
-rw-r--r-- 1 root root 319 Dec 19 15:51 /etc/rc.local*
```

>rc.local中的命令，会在启动时执行。rc.local文件默认没有执行权限，这样不会启动时运行，需要添加执行权限。

- 修改权限

```
chmod 775 /etc/rc.local
```

- 查看权限```ll /etc/rc.local```

```
-rwxrwxrwx 1 root root 319 Dec 19 15:51 /etc/rc.local*
```

# 查看文件

- 执行命令```cat /etc/rc.local```

```
# !/bin/sh -e
# 
#  rc.local
# 
#  This script is executed at the end of each multiuser runlevel.
#  Make sure that the script will "exit 0" on success or any other
#  value on error.
# 
#  In order to enable or disable this script just change the execution
#  bits.
# 
#  By default this script does nothing.

#  挂载磁盘
mount /dev/vdb1 /mnt

exit 0 
```

>把需要执行的命令或脚本写入文件，注意写在```exit 0```之前。相关的脚本，记得都添加执行权限



