---
title: Python-操作MongoDB
categories: Python
---

![image](https://upload-images.jianshu.io/upload_images/15325592-fcf16e974944f6d1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  安装pymongo
```
pip install pymongo
```
> pymongo是python中MongoDB的驱动程序

#  连接mongodb

```
# !/usr/bin/env python
#  -*- coding:utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('192.168.0.112', 27017)
db = conn.mydb   # 连接mydb数据库，没有则自动创建
my_set = db.test_set  # 使用test_set集合，没有则自动创建
```

#  插入数据

```
my_set.insert({"name":"jhon","age":18})
# 或
my_set.save({"name":"jhon","age":18})
# 添加多条数据到集合中
users=[{"name":"lily","age":18},{"name":"jhon","age":20}]  
my_set.insert(users) 
# 或
my_set.save(users) 
```
>insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入

#  查询数据
```
# 查询全部
for i in my_set.find():
    print(i)
# 查询name=lily的
for i in my_set.find({"name":"lily"}):
    print(i)
print(my_set.find_one({"name":"lily"}))
```

#  更新数据
```
my_set.update(
   <query>,    # 查询条件
   <update>,    # update的对象和一些更新的操作符
   {
     upsert: <boolean>,    # 如果不存在update的记录，是否插入
     multi: <boolean>,        # 可选，mongodb 默认是false,只更新找到的第一条记录
     writeConcern: <document>    # 可选，抛出异常的级别。
   }
)
# 把lily的age改为20
my_set.update({"name":"lily"},{'$set':{"age":20}})
```

#  删除数据

```
my_set.remove(
   <query>,    # （可选）删除的文档的条件
   {
     justOne: <boolean>,    # （可选）如果设为 true 或 1，则只删除一个文档
     writeConcern: <document>    # （可选）抛出异常的级别
   }
)
# 删除age=20的全部记录
my_set.remove({'age': '20'})

# 删除name=lily的某个id的记录
id = my_set.find_one({"name":"lily"})["_id"]
my_set.remove(id)

# 删除集合里的所有记录
db.users.remove()
```

#  mongodb的条件操作符
```
#     (>)  大于 - $gt
#     (<)  小于 - $lt
#     (>=)  大于等于 - $gte
#     (<= )  小于等于 - $lte
# 例：查询集合中age大于25的所有记录
for i in my_set.find({"age":{"$gt":25}}):
    print(i)
```

#  type(判断类型)
```
# 查询name的类型是String的
for i in my_set.find({'name':{'$type':2}}):
    print(i)
```
- 类型队对照列表

|  Type | Number  | Alias  | Notes  | 
| ------------ | ------------ |------------ |------------ |
| Double | 1 | double |  
| String | 2 | string |  
| Object | 3 | object |  
| Array | 4 | array |  
| Binary data | 5 | binData |  
| Undefined | 6 | undefined | Deprecated.|
| ObjectId | 7 | objectId |  
| Boolean | 8 | bool |  
| Date | 9 | date |  
| Null | 10 | null |  
| Regular Expression | 11 | regex |  
| DBPointer | 12 | dbPointer | Deprecated.|
| JavaScript | 13 | javascript |  
| Symbol | 14 | symbol | Deprecated.|
| JavaScript (with scope) | 15 | javascriptWithScope |  
| 32-bit integer | 16 | int |  
| Timestamp | 17 | timestamp |  
| 64-bit integer | 18 | long |  
| Decimal128 | 19 | decimal | New in version 3.4.|
| Min key | -1 | minKey |  
| Max key | 127 | maxKey |  




#  排序
```
for i in my_set.find().sort([("age",1)]):
    print(i)
```
> 在MongoDB中使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序，-1为降序。

#  limit和skip
```
# limit()方法用来读取指定数量的数据
# skip()方法用来跳过指定数量的数据
# 下面表示跳过两条数据后读取6条
for i in my_set.find().skip(2).limit(6):
    print(i)
```

#  IN
```
# 查询age是20、30、35的数据
for i in my_set.find({"age":{"$in":(20,30,35)}}):
    print(i)
```
#  OR
```
# 查询age是20或35的记录
for i in my_set.find({"$or":[{"age":20},{"age":35}]}):
    print(i)
```

#  all
```
dic = {"name":"lily","age":18,"li":[1,2,3]}
dic2 = {"name":"jhon","age":18,"li":[1,2,3,4,5,6]}

my_set.insert(dic)
my_set.insert(dic2)'''
for i in my_set.find({'li':{'$all':[1,2,3,4]}}):
    print(i)
# 查看是否包含全部条件
# 输出：{'_id': ObjectId('58c503b94fc9d44624f7b108'), 'name': 'jhon', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}
```

#  push/pushAll
```
my_set.update({'name':"lily"}, {'$push':{'li':4}})
for i in my_set.find({'name':"lily"}):
    print(i)
# 输出：{'li': [1, 2, 3, 4], '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lily'}

my_set.update({'name':"lily"}, {'$pushAll':{'li':[4,5]}})
for i in my_set.find({'name':"lily"}):
    print(i)
# 输出：{'li': [1, 2, 3, 4, 4, 5], 'name': 'lily', 'age': 18, '_id': ObjectId('58c50d784fc9d44ad8f2e803')}
```

#  pop/pull/pullAll
```
# pop
# 移除最后一个元素(-1为移除第一个)
my_set.update({'name':"lily"}, {'$pop':{'li':1}})
for i in my_set.find({'name':"lily"}):
    print(i)
# 输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lily', 'li': [1, 2, 3, 4, 4]}

# pull （按值移除）
# 移除3
my_set.update({'name':"lily"}, {'$pop':{'li':3}})

# pullAll （移除全部符合条件的）
my_set.update({'name':"lily"}, {'$pullAll':{'li':[1,2,3]}})
for i in my_set.find({'name':"lily"}):
    print(i)
# 输出：{'name': 'lily', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}
```
