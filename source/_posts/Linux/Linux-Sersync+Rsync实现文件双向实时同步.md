---
title: Linux-Sersync+Rsync实现文件双向实时同步
categories: Linux
---
![WechatIMG634.jpeg](https://upload-images.jianshu.io/upload_images/15325592-2f9f68b72a858a6f.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  环境

| 角色  |  服务器配置 | 操作系统版本 |公网IP |
| ------------ | ------------ |------------ |------------ |
| 即作为 slave<br/>也作为 master |  阿里云ECS实例<br/>server1 | Ubuntu 14.04<br/>nginx 1.4.6|47.101.70.109  |
| 即作为 slave<br/>也作为 master   | 阿里云ECS实例<br/>server2  | Ubuntu 14.04<br/>nginx 1.4.6| 106.14.151.244 |

#  设置开机自启Rsync

> 先从 **server1** 开始配置，**server2** 稍后做同样配置。

- 修改 /etc/default/rsync

```
#  将false改为true
RSYNC_ENABLE=true
```

> Ubuntu 14.04 默认安装了 rsync，但 rsync 服务默认不是启动状态。

#  修改Rsync配置文件

- 复制配置文件到 etc 目录下

```
$ cp /usr/share/doc/rsync/examples/rsyncd.conf /etc
```

- 修改 /etc/rsyncd.conf

```
#  sample rsyncd.conf configuration file

#  GLOBAL OPTIONS

#  motd file=/etc/motd
#  日志文件的目录
log file=/var/log/rsyncd
#  for pid file, do not use /var/run/rsync.pid if
#  you are going to run rsync out of the init.d script.
#  The init.d script does its own pid file handling,
#  so omit the "pid file" line completely in that case.
#  pid文件的目录
pid file=/var/run/rsyncd.pid
#  syslog协议
syslog facility=daemon
#  socket options=

#  MODULE OPTIONS

#  认证的模块名，在slave端需要指定
[data]

    comment = public archive
    #  需要同步的目录，若不存在需要先创建
    path = /home/test/
    #  是否指定新的根目录，默认为yes，设置为no
    use chroot = no
#     max connections=10
    lock file = /var/lock/rsyncd
#  the default for read only is yes...
    #  是否只读，默认为yes，设置为no
    read only = no
    list = yes
    #  运行rsync守护进程的用户
    uid = root
    #  运行rsync守护进程的用户组
    gid = root
#     exclude = 
#     exclude from = 
#     include =
#     include from =
    #  设置认证的master的用户名
    auth users = hadoop 
    #  master的用户名密码校验文件
    secrets file = /etc/rsyncd-master.secrets
    strict modes = yes
    #  允许访问的IP
    hosts allow = 106.14.151.244
    #  禁止访问的IP
#     hosts deny =
    #  是否忽略一些无关的IO错误，默认为no，设置为yes
    ignore errors = yes
    ignore nonreadable = yes
    #  传输时是否记录日志，默认为no，设置为yes
    transfer logging = yes
#     log format = %t: host %h (%a) %o %f (%l bytes). Total %b bytes.
    timeout = 600
    refuse options = checksum dry-run
    dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz
```

#  创建Master密码文件

- 创建 /etc/rsyncd-master.secrets，内容如下

```
#  格式必须为，用户名:密码
hadoop:123456
```

> 注意：server1 作为 slave 端时，这个文件是 master 的用户名密码校验文件，建议命名为`rsyncd-master.secrets`。

- 给 /etc/rsyncd-master.secrets 赋权限

```
$ chmod 0600 /etc/rsyncd-master.secrets
```

#  创建Slave密码文件

- 创建 /etc/rsyncd.secrets，内容如下

```
#  只写入salve端的密码即可
123456
```

> 注意：server1 作为 master 端时，这个文件是 salve 端的密码校验文件，建议命名为`rsyncd.secrets`。

- 给 /etc/rsyncd.secrets 赋权限

```
$ chmod 0600 /etc/rsyncd.secrets
```

#  启动Rsync

```
$ /etc/init.d/rsync start
```

#  下载Sersync

- 使用`wget`下载

```
$ wget https://gitee.com/jhon_tao/sersync/raw/master/sersync2.5.4_64bit_binary_stable_final.tar.gz
```

- 解压到 /usr/local/ 目录

```
$ tar -zxf sersync2.5.4_64bit_binary_stable_final.tar.gz -C /usr/local/
```

- 进入 /usr/local/ 目录

```
$ cd /usr/local/
```

- 将 GNU-Linux-x86 文件更改命名为 sersync

```
$ mv GNU-Linux-x86 sersync
```

#  配置Sersync

- 进入 /usr/local/sersync 目录

```
$ cd /usr/local/sersync
```

- 备份 confxml.xml

```
$ cp confxml.xml confxml.xml-bak
```

- 修改 confxml.xml，内容如下

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<head version="2.5">
    <host hostip="localhost" port="8008"></host>
    <debug start="false"/>
    <fileSystem xfs="false"/>
    #  是否开启过滤规则，默认为false
    <filter start="false">
    #  使用正则匹配过滤的目录，过滤的目录将不会同步
    <exclude expression="(.*)\.svn"></exclude>
    <exclude expression="(.*)\.gz"></exclude>
    <exclude expression="^info/*"></exclude>
    <exclude expression="^static/*"></exclude>
    </filter>
    <inotify>
    <delete start="true"/>
    <createFolder start="true"/>
    <createFile start="false"/>
    <closeWrite start="true"/>
    <moveFrom start="true"/>
    <moveTo start="true"/>
    <attrib start="false"/>
    <modify start="false"/>
    </inotify>

    <sersync>
    #  需要同步的目录，若不存在需要先创建
    <localpath watch="/home/test/">
        #  server1作为master端时，slave端的IP及其rsync的模块名
        <remote ip="106.14.151.244" name="data"/>
        <!--<remote ip="192.168.8.39" name="tongbu"/>-->
        <!--<remote ip="192.168.8.40" name="tongbu"/>-->
    </localpath>
    <rsync>
        <commonParams params="-artuz"/>
        #  认证的用户名及密码文件
        <auth start="true" users="hadoop" passwordfile="/etc/rsyncd.secrets"/>
        #  开放的端口，默认为874
        <userDefinedPort start="false" port="874"/><!-- port=874 -->
        <timeout start="true" time="100"/><!-- timeout=100 -->
        <ssh start="false"/>
    </rsync>
    #  日志文件的目录
    <failLog path="/usr/local/sersync/logs/rsync_fail_log.sh" timeToExecute="60"/><!--default every 60mins execute once-->
    <crontab start="false" schedule="600"><!--600mins-->
        <crontabfilter start="false">
        <exclude expression="*.php"></exclude>
        <exclude expression="info/*"></exclude>
        </crontabfilter>
    </crontab>
    <plugin start="false" name="command"/>
    </sersync>

    <plugin name="command">
    <param prefix="/bin/sh" suffix="" ignoreError="true"/>  <!--prefix /opt/tongbu/mmm.sh suffix-->
    <filter start="false">
        <include expression="(.*)\.php"/>
        <include expression="(.*)\.sh"/>
    </filter>
    </plugin>

    <plugin name="socket">
    <localpath watch="/opt/tongbu">
        <deshost ip="192.168.138.20" port="8009"/>
    </localpath>
    </plugin>
    <plugin name="refreshCDN">
    <localpath watch="/data0/htdocs/cms.xoyo.com/site/">
        <cdninfo domainname="ccms.chinacache.com" port="80" username="xxxx" passwd="xxxx"/>
        <sendurl base="http://pic.xoyo.com/cms"/>
        <regexurl regex="false" match="cms.xoyo.com/site([/a-zA-Z0-9]*).xoyo.com/images"/>
    </localpath>
    </plugin>
</head>
```

> 注意：阿里云ECS实例的安全组中需要添加**874**端口

#  启动Sersync

```
$ /usr/local/sersync/sersync2  -d -r -o /usr/local/sersync/confxml.xml
set the system param
execute：echo 50000000 > /proc/sys/fs/inotify/max_user_watches
execute：echo 327679 > /proc/sys/fs/inotify/max_queued_events
parse the command param
option: -d  run as a daemon
option: -r  rsync all the local files to the remote servers before the sersync work
option: -o  config xml name：  /usr/local/sersync/confxml.xml
daemon thread num: 10
parse xml config file
host ip : localhost host port: 8008
now the filter work ,if you set the crontab,you have to set crontab filter
daemon start，sersync run behind the console
use rsync password-file :
user is hadoop
passwordfile is     /etc/rsyncd.secrets
config xml parse success
please set /etc/rsyncd.conf max connections=0 Manually
sersync working thread 12  = 1(primary thread) + 1(fail retry thread) + 10(daemon sub threads)
Max threads numbers is: 22 = 12(Thread pool nums) + 10(Sub threads)
please according your cpu ，use -n param to adjust the cpu rate
************************attention***********************************
you set the filter so the "-r " can not work
run the sersync:
watch path is: /home/hadoop/data
```

#  设置开机自启Sersync

> 将`/usr/local/sersync/sersync2 -d -r -o /usr/local/sersync/confxml.xml`写入到 rc.local 中，开机就能启动 sersync 守护进程同步数据。

#  测试文件双向实时同步

- 查看 sersync 进程

```
$ ps -eaf | grep -i sersync | grep -v grep
root       996     1  0 11:28 ?        00:00:00 /usr/local/sersync/sersync2 -d -r -o /usr/local/sersync/confxml.xml
root      1616   996  0 12:28 ?        00:00:00 sh -c /bin/sh /usr/local/sersync/logs/rsync_fail_log.sh
root      1617  1616  0 12:28 ?        00:00:00 /bin/sh /usr/local/sersync/logs/rsync_fail_log.sh
```

> server1 和 server2 分别查看，确保 sersync 进程都已经存在。

- 在 server1 中创建文件

```
$ echo server1 > /home/test/server1.txt
```

- 在 server2 中查看

```
$ cat /home/test/server1.txt
server1
```

- 在 server2 中创建文件

```
$ echo server2 > /home/test/server2.txt
```

- 在 server1 中查看

```
$  cat /home/test/server2.txt
server2
```

> 可以看到，文件双向实时同步成功。
