---
title: PHP-TP5-使用MongoDb
categories: PHP
---

![f8c943926119dfdb1c6f91f7c0ef459a496392b3.jpg](https://upload-images.jianshu.io/upload_images/15325592-3c7032e0a9af7a41.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  插入文档

- 插入单条

```
Db::table('users')
->insert(
	[
		'name'=>'银太',
		'arm'=>'巴波',
		'height'=>160,
		'mp'=>5000,
	]
);
```

- 批量插入

```
Db::table('users')
->insertAll(
	[
		[
			'name'=>'阿尔维斯',
			'arm'=>'十三图腾锁链',
			'height'=>165,
			'mp'=>5000,
		],
		[
			'name'=>'杰克',
			'arm'=>'战斗银铲',
			'height'=>158,
			'mp'=>4000,
		]
	]
);
```

#  更新文档

```
Db::table('users')
->where('name', '银太')
->update(
	[
		'arm' => '果冻垫',
	]
);
```

#  删除文档

```
Db::table('users')
->where('name', '银太')
->delete();
```

#  查询文档

- 查询单个

```
Db::table('users')
->find();
```

- 查询所有

```
Db::table('users')
->select();
```

- AND 查询

```
Db::table('users')
->where('name', '阿尔维斯')
->where('arm', '十三图腾锁链')
->select();
```

- 条件查询

```
Db::table('users')
->where('height', '>=', 160)
->select();
```

- 模糊查询

```
Db::table('users')
->where('name', 'like', '阿尔')
->select();
```

- 限制查询

```
Db::table('users')
->limit(1)
->select();
```

- 跳过查询

```
Db::table('users')
->skip(5)
->select();
```

- 排序查询

```
#   asc表示升序
Db::table('users')
->order('height', 'asc')
->select();
#   desc表示降序
Db::table('users')
->order('height', 'desc')
->select();
```

- 聚合查询

```
#  单聚合查询
Db::table('users')
->aggregate('sum', 'mp');
#  多聚合查询
Db::table('users')
->multiAggregate(
	[
		'sum' => 'mp',
		'avg' => 'height',
	],
	['name']
);
```

- 去重查询

```
Db::table('users')->distinct('name');
```

- 统计查询

```
Db::table('users')
->where('mp', '>', 4000)
->count();
```

#  查询集合

```
Db::listcollections();
```

#  手册

- [ThinkPHP5.1完全开发手册](https://www.kancloud.cn/manual/thinkphp5_1/354135 "ThinkPHP5.1完全开发手册")

- [ThinkPHP手册](https://api.yuhal.com/file/ThinkPHP.chm "ThinkPHP手册")

