---
title: MySql-阿里云RDS与本机MySql主从同步
categories: MySql
---

![WechatIMG576.jpeg](https://upload-images.jianshu.io/upload_images/15325592-46bf5f4b84d9fd97.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 入手一台阿里云 RDS，想用它与本机 Mysql 实现主从同步。阿里云 RDS 作为`主实例`，本机 MySql 作为`从实例`，两者版本都是 Mysql 5.7。在此分享下实现的方案，部分参照 https://developer.aliyun.com/article/57731

#  本机Mysql配置

- 修改 /etc/my.cnf 

```
#  主从同步模式
binlog_format = row
#  主从标示ID
server-id = 2
#  忽略同步的数据库
replicate-ignore-db = mysql
replicate-ignore-db = information_schema
replicate-ignore-db = performance_schema
#  开启gtid模式
gtid_mode=on
#  保证GTID安全的参数
enforce_gtid_consistency=on
#  让从机接收到bin_log后也同步到自己的bin_log上
log-slave-updates=1
```

> 如果指定某个需要同步的数据库，需增加参数 replicate-do-db ，并赋值指定的 RDS 数据库名称，例如：replicate-do-db = test。

- 重启本机 mysql

```
$ service mysql restart
```

#  配置同步的RDS

- 登录本机 mysql

```
$ mysql -u -p
```

- 配置主实例

```
mysql> change master to master_host = 'rds外网地址', master_port = 3306, master_user = '账号', master_password='密码', master_auto_position = 1;
Query OK, 0 rows affected, 2 warnings (0.02 sec)
```

- 启动从实例

```
mysql> start slave;
Query OK, 0 rows affected (0.00 sec)
```

- 查看本机 mysql 同步状态

```
mysql> show slave status \G;
*************************** 1. row ***************************
Slave_IO_State: Waiting for master to send event
Master_Host: rm-uf6l85e9tmq2rh5duco.mysql.rds.aliyuncs.com
Master_User: zhangyuhai
Master_Port: 3306
Connect_Retry: 60
Master_Log_File: mysql-bin.000003
Read_Master_Log_Pos: 74263
Relay_Log_File: iZbp1ipfxx237fclphlj7wZ-relay-bin.000002
Relay_Log_Pos: 74476
Relay_Master_Log_File: mysql-bin.000003
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
Replicate_Do_DB:
Replicate_Ignore_DB: mysql,information_schema,performance_schema
Replicate_Do_Table:
Replicate_Ignore_Table:
Replicate_Wild_Do_Table:
Replicate_Wild_Ignore_Table:
Last_Errno: 0
Last_Error:
Skip_Counter: 0
Exec_Master_Log_Pos: 74263
Relay_Log_Space: 74701
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
Master_Server_Id: 1065104776
Master_UUID: 4a60e33e-7fd5-11eb-838e-506b4bc2c2b2
Master_Info_File: /usr/local/mysql/var/master.info
SQL_Delay: 0
SQL_Remaining_Delay: NULL
Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
Master_Retry_Count: 86400
Master_Bind:
Last_IO_Error_Timestamp:
Last_SQL_Error_Timestamp:
Master_SSL_Crl:
Master_SSL_Crlpath:
Retrieved_Gtid_Set: 4a60e33e-7fd5-11eb-838e-506b4bc2c2b2:1-263
Executed_Gtid_Set: 4a60e33e-7fd5-11eb-838e-506b4bc2c2b2:1-263,
b14b6af5-1d8f-11ea-8a7c-00163e11c9bc:1
Auto_Position: 1
Replicate_Rewrite_DB:
Channel_Name:
Master_TLS_Version:
1 row in set (0.00 sec)
ERROR:
No query specified
```

> 上面返回的状态中，查看 Slave_IO_Running 和 Slave_SQL_Running 的状态是否为 Yes 。只有两个参数均显示 Yes，表示配置成功，完成主从同步功能。否则，请根据报错信息，定位错误原因，并进行修改。

#  测试主从同步

> 目前为止，已经完成 RDS 实例作为主实例，通过主从同步的方式，同步到本机 MySQL。

- 登录主实例 RDS

```
#  创建数据库test
mysql> create database test;
Query OK, 1 row affected (0.01 sec)
#  操作数据库test
mysql> use test;
Database changed
#  创建表table
CREATE TABLE `table1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.03 sec)
#  向表table插入记录
INSERT INTO `test`.`table1`(`id`) VALUES (1);
```

- 登录本机 Mysql

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
mysql> select * from table1;
+----+
| id |
+----+
|  1 |
|  2 |
+----+
2 rows in set (0.00 sec
```

#  一主多从架构图

![一主多从.jpg](https://upload-images.jianshu.io/upload_images/15325592-59f92d08a1fbd05e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

