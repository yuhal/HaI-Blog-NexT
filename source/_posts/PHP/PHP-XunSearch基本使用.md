---
title: PHP-XunSearch基本使用
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-e54db993f6980d82?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 基本实践
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

// 创建对象
$xs = new XS('demo');

// 查询
$docs = $xs->search->search('测试');

// 输出
print_r($docs);
```
# 异常捕获
```
try
{
    $xs = new XS('demo');
    $docs = $xs->search->setQuery('测试')->setLimit(5)->search();
    foreach ($docs as $doc)
    {
        echo $doc->rank() . ". " . $doc->subject . " [" . $doc->percent() . "%]\n";
        echo $doc->message . "\n";
    }
}
catch (XSException $e)
{
    echo $e;               // 直接输出异常描述
    if (defined('DEBUG'))  // 如果是 DEBUG 模式，则输出堆栈情况
        echo "\n" . $e->getTraceAsString() . "\n";
}
```
# XSDocument 文档
docid() 取得搜索结果文档的 docid 值 (实际数据库内的 id，一般用不到)
rank() 取得搜索结果文档的序号值 (第X条结果)
percent() 取得搜索结果文档的匹配百分比 (结果匹配度, 1~100)
weight() 取得搜索结果文档的权重值 (浮点数)
ccount() 取得搜索结果折叠的数量 (按字段折叠搜索时才有效)
# 添加操作
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

try
{
    $xs = new XS('demo');
    $doc = new XSDocument();
    $doc->pid = 4;
    $doc->subject = "Hello,XS";
    $doc->message = "Hello,XS内容";
    $xs->index->add($doc);
}
catch (XSException $e)
{
    echo $e;               // 直接输出异常描述
    if (defined('DEBUG'))  // 如果是 DEBUG 模式，则输出堆栈情况
        echo "\n" . $e->getTraceAsString() . "\n";
}
```
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

try
{
    $xs = new XS('demo');
    $doc = new XSDocument();
    $doc['pid'] = 5;
    $doc['subject'] = "Hello,XS";
    $doc['message'] = "Hello,XS内容";
    $xs->index->add($doc);
}
catch (XSException $e)
{
    echo $e;               // 直接输出异常描述
    if (defined('DEBUG'))  // 如果是 DEBUG 模式，则输出堆栈情况
        echo "\n" . $e->getTraceAsString() . "\n";
}
```
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

try
{
    $xs = new XS('demo');
    $doc = new XSDocument();
    $doc ->setFields([
        'pid' => 6,
        'subject' => "Hello,XS",
        'message' => "Hello,XS内容"
    ]);

    $xs->index->add($doc);
}
catch (XSException $e)
{
    echo $e;               // 直接输出异常描述
    if (defined('DEBUG'))  // 如果是 DEBUG 模式，则输出堆栈情况
        echo "\n" . $e->getTraceAsString() . "\n";
}
```
建立索引的过程会有点延迟！
```
$index->add($doc)->flushIndex()
```
可以临时处理成同步的。
# ini
string 字符型，适用多数情况，也是默认值
numeric 数值型，包含整型和浮点数，仅当字段需用于以排序或区间检索时才设为该类型，否则请使用 string　即可
date 日期型，形式为 YYYYmmdd 这样固定的 8 字节，如果没有区间检索或排序需求不建议使用
id 主键型，确保每条数据具备唯一值，是索引更新和删除的凭据，每个搜索项目必须有且仅有一个 id 字段，该字段的值不区分大小写
title 标题型，标题或名称字段，至多有一个该类型的字段
body 内容型，主内容字段, 即本搜索项目中内容最长的字段，至多只有一个该类型字段，本字段不支持字段检索
```
type = string
project.name = sample
project.default_charset = GBK
;server.index = 8383
;server.search = 8384

[pid]
type = id

[subject]
type = title

[message]
type = body

[dateline]
type = numeric

[author]
index = both

[authorid]

[tid]
index = self
tokenizer = full

[fid]
index = self
tokenizer = full

[flag]
```
# 更新、修改文档
如果索引数据库中已存在主键值相同的文档，那么相当于先删除原有的文档，再用当前文档替换它。 如果未存在主键值相同的文档，则效果和添加文档完全一致。
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

$xs = new XS('my');
$data = array(
    'pid' => 2, // 此字段为主键，是进行文档替换的唯一标识
    'subject' => '测试文档的标题',
    'message' => '测试文档的内容部分',
    'chrono' => time()
);

// 创建文档对象
$doc = new XSDocument;
$doc->setFields($data);

// 更新到索引数据库中
$xs->index->update($doc)->flushIndex();
```
# 删除文档
1.按主键删除
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

// 创建xs
$xs = new XS('my');
// 创建index
$index = $xs->index;
// 删除
$index->del('1')->flushIndex();

// 删除
$index->del(['4','5'])->flushIndex();
```
2.按内容删除
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';


$xs = new XS('my');

// 创建xs
$xs = new XS('my');
// 创建index
$index = $xs->index;
// 删除
$index->del('测试','subject')->flushIndex();
```
此外删除操作和添加文档一样，也是一个异步行为。
# 清空索引
```
// 创建xs
$xs = new XS('my');
// 创建index
$index = $xs->index;
// 删除
$index->clean();
```
# 平滑重建索引
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

// 创建xs
$xs = new XS('my');
// 创建index
$index = $xs->index;
// 宣布开始重建索引
$index->beginRebuild();

// 然后在此开始添加数据
$data = array(
    'pid' => 2, // 此字段为主键，是进行文档替换的唯一标识
    'subject' => '测试文档的标题',
    'message' => '测试文档的内容部分',
    'chrono' => time()
);

// 创建文档对象
$doc = new XSDocument;
$doc->setFields($data);

$index->add($doc);


// 告诉服务器重建完比
$index->endRebuild();
```
# 使用索引缓冲区
一次性提交服务操作
```
<?php
// 引入
require_once './sdk/xs/lib/XS.php';

// 创建xs
$xs = new XS('my');
// 创建index
$index = $xs->index;

// 开启缓冲区，默认 4MB，如 $index->openBuffer(8) 则表示 8MB
$index->openBuffer();

// 然后在此开始添加数据
$data = array(
    'pid' => 2, // 此字段为主键，是进行文档替换的唯一标识
    'subject' => '测试文档的标题',
    'message' => '测试文档的内容部分',
    'chrono' => time()
);

// 创建文档对象
$doc = new XSDocument;
$doc->setFields($data);
// 在此进行批量的文档添加、修改、删除操作
$index->add($doc);
$index->add($doc);
$index->add($doc);
$index->add($doc);
$index->add($doc);
$index->add($doc);


$index->closeBuffer(); // 关闭缓冲区，必须和 openBuffer 成对使用
```
# 自定义 SCWS 词库
1.全局自定义词库
```
$prefix/etc/dict_user.txt
```
```
#  Custom dictionary for scws (UTF-8 encoding)
#  每行一条记录，以 #  开头的号表示注释忽略
#  每行最多包含 4 个字段，依次代表 "词条" "TF" "IDF" "词性"
#  字段之间用空格或制表符分开，特殊词性 "!" 用于表示删除该词
#  参见 scws 自定义词典帮助：
#  http://bbs.xunsearch.com/showthread.php?tid=1303
#  $Id$
# 
#  WORD      TF      IDF     ATTR
#  ------------------------------------------------------
```
2.项目自定义词库（这个貌似更好的读取）
```
$prefix/data/项目名称/dict_user.txt
```

转载[https://www.cnblogs.com/jiqing9006/p/9254726.html](https://www.cnblogs.com/jiqing9006/p/9254726.html)
手册https://api.yuhal.com/file/xs_php_manual.chm
