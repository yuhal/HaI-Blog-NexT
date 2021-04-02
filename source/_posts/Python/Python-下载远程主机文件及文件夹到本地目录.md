---
title: Python-下载远程主机文件及文件夹到本地目录
categories: Python
---

![WechatIMG486.jpeg](https://upload-images.jianshu.io/upload_images/15325592-12ce4c0d3c9d9e81.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 创建 down.py，代码如下。

```
import os

import time

import logging

import paramiko

from logging import handlers

from stat import S_ISDIR as isdir

class Logger(object):
    #  日志级别关系映射
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(
    self,filename,level='info',when='D',backCount=3,fmt=
    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    ):
        check_local_dir('log')
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  #  设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  #  设置日志级别
        sh = logging.StreamHandler()  #  往屏幕上输出
        sh.setFormatter(format_str)  #  设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=filename,when=when,backupCount=backCount,
            encoding='utf-8')#  往文件里写入#  指定间隔时间自动生成文件的处理器
        #  实例化TimedRotatingFileHandler
        #  interval是时间间隔，backupCount是备份文件的个数，
        #  如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        #  S 秒
        #  M 分
        #  H 小时、
        #  D 天、
        #  W 每星期（interval==0时代表星期一）
        #  midnight 每天凌晨
        th.setFormatter(format_str)#  设置文件里写入的格式
        self.logger.addHandler(sh) #  把对象加到logger里
        self.logger.addHandler(th)

class Host:
    def __init__(self):
        #  服务器ip地址
        host = "111.222.333.444"
        #  端口号
        port = 22
        #  ssh 用户名
        username = "root"
        #  密码
        password = "1234"
        #  获取当前日期
        date = time.strftime("%Y%m%d")
        #  记录当天的日志
        self.error_log = Logger('log/' + date + 'error.txt',level='error',fmt='')
        self.info_log = Logger('log/' + date + 'info.txt',level='info',fmt='')
        #  连接远程服务器
        self.t = paramiko.Transport((host, port))
        self.t.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)

    def down_from_remote(self, remote_dir_name, local_dir_name):
        """
        远程下载文件及文件夹
        :remote_dir_name: 远程文件路径
        :local_dir_name: 本地文件存放路径
        """
        remote_file = self.sftp.stat(remote_dir_name)
        if isdir(remote_file.st_mode):
            #  文件夹，不能直接下载，需要继续循环
            if check_local_dir(local_dir_name)==True:
                self.info_log.logger.info('本地文件夹已存在：'+local_dir_name)
            else:
                self.info_log.logger.info('开始创建文件夹：'+remote_dir_name)
            for remote_file_name in self.sftp.listdir(remote_dir_name):
                sub_remote = os.path.join(remote_dir_name, remote_file_name)
                sub_remote = sub_remote.replace('\\', '/')
                sub_local = os.path.join(local_dir_name, remote_file_name)
                sub_local = sub_local.replace('\\', '/')
                self.down_from_remote(sub_remote, sub_local)
        else:
            #  文件，直接下载
            if check_local_file(local_dir_name)==True:
                self.info_log.logger.info('本地文件已存在：'+local_dir_name)
            else:
                self.info_log.logger.info('开始下载文件：'+remote_dir_name)
                try:
                    self.sftp.get(remote_dir_name, local_dir_name)
                except:
                    self.error_log.logger.error('下载文件失败：'+remote_dir_name)

    def __del__(self):
        #  关闭连接
        self.t.close()

def check_local_dir(local_dir_name):
    """
    本地文件夹是否存在，不存在则创建
    :local_dir_name: 本地文件存放路径
    """
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)
        return False
    else:
        return True

def check_local_file(local_dir_name):
    """
    本地文件是否存在，不存在则下载
    :local_dir_name: 本地文件存放路径
    """
    if not os.path.exists(local_dir_name):
        return False
    else:
        return True

if __name__ == "__main__":
    #  远程文件路径（需要绝对路径）
    remote_dir = '/home/Uploads/'
    #  本地文件存放路径
    local_dir = '/var/Uploads'
    h = Host()
    #  远程文件开始下载
    h.down_from_remote(remote_dir, local_dir)
    del h
```

- 执行

```
$ python3 down.py
开始创建文件夹：/home/Uploads/Image
开始下载文件：/home/Uploads/Image/video_49.png
开始下载文件：/home/Uploads/Image/video_13.png
```

- 查看

```
$ ls /home
Uploads 
```
