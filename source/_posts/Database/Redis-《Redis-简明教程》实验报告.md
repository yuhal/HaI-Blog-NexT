---
title: Redis-《Redis-简明教程》实验报告
categories: Redis
---

![2e22ce50f815a56eb874c48abcd85bcede7d5fae.jpg](https://upload-images.jianshu.io/upload_images/15325592-4d41a64db0f5671d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Redis 简明教程 免费.jpg](https://upload-images.jianshu.io/upload_images/15325592-6c6d02423f9956be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  字符串

- set

```
#  格式
> set key value
#  例如
> set name Leo
```

> set 适用于单个 key-value 的对应关系。

- get

```
#  格式
> get key
#  例如
> get name
```

> get 查询单个 key 的值。

- 加减运算

```
#  自加+1
> incr height
#  自定义加
> incrby height 10
#  自减-1
> decr  weight
#  自定义减
> decrby weight 10
```

- mset

```
#  格式
> mset key [key ...]
#  例如
> mset name1 Leo name2 Raph
```

> mset 适用于多个 key-value 的对应关系。

- mget

```
#  格式
> mget key [key ...]
#  例如
> mset name1 name2
```

> mget 查询多个 key 的值。

#  列表

- lpush

```
#  格式
> lpush key element [element ...]
#  例如
> lpush list Leo Raph
```

> lpush 添加一个或多个元素到列表的左边，或称为头部。

- rpush

```
#  格式
> rpush key element [element ...]
#  例如
> rpush list Donnie Mikey
```

> rpush 添加一个或多个元素到列表的有边，或称为尾部。

- lrange 

```
#  格式
> lrange key start stop
#  例如
> lrange list 0 -1
```

> lrange 可以按索引查询列表，`0 -1`表示查询全部。

- brpop 

```
#  格式
> brpop key [key ...] timeout
#  例如
> brpop list 1
```

> brpop 移出并获取列表的最后一个元素, 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。

- blpop 

```
#  格式
> blpop key [key ...] timeout
#  例如
> blpop list 1
```

> blpop 移出并获取列表的头一个元素, 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。

#  哈希

- hmset

```
#  格式
> hmset key field value [field value ...]
#  例如
> hmset id:1 nickname Leo weapon 双刀 height 170
```

> hmset 设置一个多域的 hash 表。

- hget

```
#  格式
> hget key field
#  例如
> hget id:1 nickname
```

> hget 获取指定的单域。

- hgetall 

```
#  格式
> hgetall key
#  例如
> hget id:1
```

> hgetall 命令获取指定 key 的所有信息。

- hmget

```
#  格式
> hmget key field [field ...]
#  例如
> hmget id:1 nickname weapon
```

- hincrby

```
#  格式
> hincrby key field increment
#  例如
> hincrby id:1 height 10
```

> hincrby 用于为哈希表中的字段值加上指定增量值。


#  集合

- sadd

```
#  格式
> sadd key member [member ...]
#  例如
> sadd list Leo Raph Donnie Mikey
```

> sadd 产生一个无序集合。

- smembers

```
#  格式
> smembers key
#  例如
> smembers list
```

> smembers 查看一个集合。

- sismember 

```
#  格式
> sismember key member
#  例如
> sismember list Leo
```

> sismember 查看该元素是否是集合的成员。

- zadd

```
#  格式
> zadd key [NX|XX] [CH] [INCR] score member [score member ...]
#  例如
> zadd list 1 Leo
```

> zadd 产生一个有序集合。

- zrange 

```
#  格式
> zrange key start stop [WITHSCORES]
#  例如
> zrange list 0 -1
```

> zrange 查看正序的集合。

- zrevrange  

```
#  格式
> zrevrange key start stop [WITHSCORES]
#  例如
> zrevrange list 0 -1 withscores 
```

> zrevrange 查看倒序的集合，使用 withscores 参数返回权重值。

#  常用命令

- exists  

```
#  格式
> exists key [key ...]
#  例如
> exists list
```

> exists 判断一个 key 是否存在。

- del 

```
#  格式
> del key [key ...]
#  例如
> del list
```

> del 删除一个或多个 key。

- type 

```
#  格式
> type key
#  例如
> type list
```

> type 返回某个 key 的数据类型。

-  keys 

```
#  格式
> keys pattern
#  例如
> keys l*
```

> keys 返回匹配的 key 列表。

- rename 

```
#  格式
> rename key newkey
#  例如
> rename list team
```

> rename 更改 key 的名称。

- expire

```
#  格式
> expire key seconds
#  例如
> expire countdown 20
```

> expire 设置某个 key 的过期时间。

- ttl

```
#  格式
> ttl key
#  例如
> ttl countdown
```

> expire 查询 key 距过期剩余时间。

#  其他命令

```
#  清除界面
> clear 
#  查询 Redis 服务器的配置参数
> config get
#  修改 Redis 服务器的配置参数
> config get
#  重置数据统计报告
> config resetstat
#  查询当前数据库的 key 的总数
> dbsize 
#  清空当前数据库中的所有 key（慎用）
> flushdb 
#  清空所有数据库中的所有 key（慎用）
> flushall 
> 查询 Redis 服务器相关信息
> info 
#  随机获得一个已经存在的 key
> randomkey
```

#  设置密码


- 方式一（使用命令设置）

```
#  格式
> config set requirepass password
#  例如
> config set requirepass 123456
```

- 方式二（配置 redis.conf）

```
#  requirepass foobared
修改为
requirepass 123456
```

#  密码认证

- 方式一（登录时认证）

```
#  格式
$ redis-cli -a password
#  例如
$ redis-cli -a 123456
```

- 方式一（登录后认证）

```
#  格式
> auth password
#  例如
> auth 123456
```

#  事务处理

```
#  格式
> multi
> ...
> ...
> exec
#  例如
> multi
> mset name1 Leo name2 Raph
> mset name3 Donnie  name4 Mikey 
> exec
```

