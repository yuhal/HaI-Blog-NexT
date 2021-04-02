---
title: Python-拷贝文件及文件夹到远程主机目录
categories: Python
---
![WechatIMG484.jpeg](https://upload-images.jianshu.io/upload_images/15325592-1ae08fb73edb4153.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 创建 scp.py，代码如下。

```
import os

import re

import time

import sys

import subprocess

import logging

from logging import handlers

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
        #  self.logger.addHandler(sh) #  把对象加到logger里
        self.logger.addHandler(th)

class Host:
    def __init__(self):
        #  服务器ip地址
        self.host = "111.222.333.444"
        #  端口号
        self.port = 22
        #  ssh 用户名
        self.username = "root"
        #  密码
        self.password = "1234"
        #  获取当前日期
        date = time.strftime("%Y%m%d")
        #  记录当天的日志
        self.error_log = Logger('log/' + date + 'error.txt',level='error',fmt='')
        self.info_log = Logger('log/' + date + 'info.txt',level='info',fmt='')

    def scpFileToRemoteNode(self, local_path, remote_path):
        """
        将指定目录的文件及文件夹上传到服务器指定目录
        local_path: 本机目录
        remote_path: 远程服务器目录
        """
        SCP_CMD_BASE = r"""
          expect -c "
          set timeout 300 ;
          spawn scp -P {port} -r {local_path} {username}@{host}:{remote_path} ;
          expect *assword* {{{{ send {password}\r }}}} ;
          expect *\r ;
          expect \r ;
          expect eof
          "
        """.format(
            username=self.username,
            password=self.password,
            host=self.host,
            local_path=local_path,
            remote_path=remote_path,
            port=self.port
        )
        SCP_CMD = SCP_CMD_BASE.format(local_path = local_path)
        p = subprocess.Popen( SCP_CMD , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        lines = p.stdout.readlines()
        for line in lines:
            #  只取有效的信息
            line = str(line.strip()).replace('b\'','')
            if line.find(self.host) < 0:
                if line.find("100%") > 0:
                    self.info_log.logger.info(line)
                else:
                    self.error_log.logger.error(line)
        p.communicate()
        os.system(SCP_CMD)
  
if __name__ == '__main__':
    h = Host()
    #  本机目录
    local_path = '/private/var/Uploads'
    #  远程服务器目录
    remote_path = '/home'
    h.scpFileToRemoteNode(local_path,remote_path)
```

- 本机执行

```
$ python3 scp.py
spawn scp -P 22 -r /private/var/HaI/2021/feb03/Uploads root@111.222.333.444:/home
root@111.222.333.444's password:
5ff41c96a4433.jpg                          100%   34KB 211.2KB/s   00:00
5f2bc8e2435eb.jpg                          100%   70KB 492.1KB/s   00:00
5ffbe8b529b70.png                          100%   10KB  13.0KB/s   00:00
600f8dbe4735d.png                          100%  193KB  96.0KB/s   00:02
```

- 登录远程服务器查看

```
$ ls /home
Uploads
```
