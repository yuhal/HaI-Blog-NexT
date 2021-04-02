---
title: Mysql-数据库同步实现双机互备
categories: Mysql
---
![WechatIMG636.jpeg](https://upload-images.jianshu.io/upload_images/15325592-befa7afbadee9088.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

| 角色  |  服务器配置 | 操作系统版本 |公网IP |
| ------------ | ------------ |------------ |------------ |
| 即作为 slave<br/>也作为 master |  阿里云ECS实例<br/>server1 | Ubuntu 14.04<br/>mysql 5.5.44|47.101.70.109  |
| 即作为 slave<br/>也作为 master   | 阿里云ECS实例<br/>server2  | Ubuntu 14.04<br/>mysql 5.5.44 | 106.14.151.244 |

#  修改配置文件

> 先从 server1 开始配置，server2 做同样配置。

- 修改 /etc/mysql/my.cnf

```
#  不指定远程访问的IP
#  bind-address = 127.0.01
#  唯一标示ID，server1设置为1，server2设置为2
server-id = 1
#  忽略同步的数据库
replicate-ignore-db = mysql
replicate-ignore-db = information_schema
replicate-ignore-db = performance_schema
#  需要同步的库，如果有多个数据库需要同步，设置多行
binlog-do-db = shjyzxk
#  开启二进制日志，slave端可以通过该日志来确定执行操作
log_bin = master_01，server1设置为master_01，server2设置为master_01
```

- 重启本机 mysql

```
$ service mysql restart
```

#  开启远程访问

> 登录 **server1**->mysql，server2 做同样配置。

```
#  操作数据库mysql
mysql> use mysql;
#  查询root用户开放的host
mysql> select user,host from user where user='root';
+------+--------------+
| user | host         |
+------+--------------+
| root | 127.0.0.1    |
+------+--------------+
#  如果没有"%"这个host值，就进行修改:
mysql> update user set host='%' where user='root' and host='127.0.0.1';
#  刷新生效
mysql> flush privileges;
#  授权可以远程访问
grant all privileges on *.* to root@'%'identified by 'passwd';
```

#  配置同步的Master

- 登录 **server1**->mysql

```
#  查看master状态
mysql> show master status;
+------------------+----------+--------------+------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| master_01.000006 |      107 | test         |                  |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)
```

- 登录 **server2**->mysql

```
#  查看 master 状态
mysql> show master status;
+------------------+----------+--------------+------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| master_02.000015 |      107 | test         |                  |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)
```

- 切换 **server1**->mysql

```
#  创建数据库test
mysql> create database test;
#  配置master
mysql> CHANGE MASTER TO MASTER_HOST='106.14.151.244 ',MASTER_USER='root',MASTER_PASSWORD='123456',MASTER_PORT=3306, MASTER_LOG_FILE='master_02.000015',MASTER_LOG_POS=107,MASTER_CONNECT_RETRY=2;
Query OK, 0 rows affected (0.01 sec)
#  启动slave
mysql> start slave;
#  查看slave状态
mysql> show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 106.14.151.244
                  Master_User: root
                  Master_Port: 3306
                Connect_Retry: 2
              Master_Log_File: master_02.000016
          Read_Master_Log_Pos: 107
               Relay_Log_File: mysqld-relay-bin.000003
                Relay_Log_Pos: 253
        Relay_Master_Log_File: master_02.000016
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 107
              Relay_Log_Space: 556
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 2
1 row in set (0.00 sec)
```

- 切换 **server2**->mysql

```
#  配置master
$ CHANGE MASTER TO MASTER_HOST='47.101.70.109 ',MASTER_USER='root',MASTER_PASSWORD='123456',MASTER_PORT=3306, MASTER_LOG_FILE='master_01.000006',MASTER_LOG_POS=107,MASTER_CONNECT_RETRY=1;
Query OK, 0 rows affected (0.01 sec)
#  启动slave
mysql> start slave;
#  查看slave状态
mysql> show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 47.101.70.109
                  Master_User: root
                  Master_Port: 3306
                Connect_Retry: 1
              Master_Log_File: master_01.000007
          Read_Master_Log_Pos: 190
               Relay_Log_File: mysqld-relay-bin.000003
                Relay_Log_Pos: 336
        Relay_Master_Log_File: master_01.000007
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 190
              Relay_Log_Space: 1898
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
1 row in set (0.00 sec)
```

> 上面返回的状态中，查看 Slave_IO_Running 和 Slave_SQL_Running 的状态是否为 Yes 。只有两个参数均显示 Yes，表示配置成功，完成主从同步功能。否则，请根据报错信息，定位错误原因，并进行修改。

- 参数说明

> 以下使用 server1 的参数配置来进行说明

|参数名|参数值|说明|
|------------|------------|
|MASTER_HOST|106.14.151.244|同步的服务器IP，这里为 server2 的公网IP|
|MASTER_USER|root|同步服务器的 mysql 用户名|
|MASTER_PASSWORD|123456|同步服务器的 mysql 密码|
|MASTER_PORT|3306|数据库端口|
|MASTER_LOG_FILE|master_02.000015|对应 server2 的 File 名|
|MASTER_LOG_POS|107|对应 server2 的 Position|
|MASTER_CONNECT_RETRY|2|对应 server2 的 server-id|
|Slave_IO_Running |Yes |slave 与 master 的IO通信状态|
|Slave_SQL_Running |Yes |slave 与 master 的 mysql 进程状态|

#  测试数据双向同步

- 登录 **server1**->mysql

```
#  操作数据库test
mysql> use test;
#  创建表table
CREATE TABLE `table1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#  向表table插入记录
INSERT INTO `test`.`table1`(`id`) VALUES (1);
```

- 登录 **server2**->mysql

```
#  查看数据库
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
5 rows in set (0.00 sec)
#  操作数据库test
mysql> use test;
Database changed
#  查看表table1
mysql> select * from table1;
+----+
| id |
+----+
|  1 |
+----+
2 rows in set (0.00 sec)
#  向表table插入记录
INSERT INTO `test`.`table1`(`id`) VALUES (2);
```

- 切换 **server1**->mysql

```
#  查看表table1
mysql> select * from table1;
+----+
| id |
+----+
|  1 |
|  2 |
+----+
```

> 可以看到，数据双向同步成功。
