---
title: PHP-MongoDB-封装-支持多库链接配置-简单易用
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-46633b701816216b?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
mongoDB封装 支持多库链接配置 简单 易用
示例代码中包含mongoDB的基本操作，增、删、改、查、索引、正则等。
请注意：mongoDB 支持版本 3.2+
因为操作方都是使用command来执行，使用规范请参见官方文档。
具体命令及参数等相关定义请参见：
https://docs.mongodb.com/manual/reference/command/

m_mgdb.php
```
<?php
/**
 * mongoDB 简单 封装
 * 请注意：mongoDB 支持版本 3.2+
 * 具体参数及相关定义请参见： https://docs.mongodb.com/manual/reference/command/
 * @author color_wind
 */
final class m_mgdb {
    //--------------  定义变量  --------------//
    private static $ins     = [];
    private static $def     = "default";
    private $_conn          = null;
    private $_db            = null;
    private static $_config = [
        "default" => ["url" => "mongodb://username:passwd@localhost:27017","dbname" => "mydb1"],
        "mdb1"    => ["url" => "mongodb://10.0.0.12:27017","dbname" => "mydb2"],
    ];
 
    /**
     * 创建实例
     * @param  string $confkey
     * @return \m_mgdb
     */
    static function i($confkey = NULL) {
        if (!$confkey) {
            $confkey = self::$def;
        }
        if (!isset(self::$ins[$confkey]) && ($conf = self::$_config[$confkey])) {
            $m = new m_mgdb($conf);
            self::$ins[$confkey] = $m;
        }
        return self::$ins[$confkey];
    }
 
    /**
     * 构造方法
     * 单例模式
     */
    private function __construct(array $conf) {
        $this->_conn = new MongoDB\Driver\Manager($conf["url"]."/{$conf["dbname"]}");
        $this->_db   = $conf["dbname"];
    }
 
    /**
     * 插入数据
     * @param  string $collname
     * @param  array  $documents    [["name"=>"values", ...], ...]
     * @param  array  $writeOps     ["ordered"=>boolean,"writeConcern"=>array]
     * @return \MongoDB\Driver\Cursor
     */
    function insert($collname, array $documents, array $writeOps = []) {
        $cmd = [
            "insert"    => $collname,
            "documents" => $documents,
        ];
        $cmd += $writeOps;
        return $this->command($cmd);
    }
 
    /**
     * 删除数据
     * @param  string $collname
     * @param  array  $deletes      [["q"=>query,"limit"=>int], ...]
     * @param  array  $writeOps     ["ordered"=>boolean,"writeConcern"=>array]
     * @return \MongoDB\Driver\Cursor
     */
    function del($collname, array $deletes, array $writeOps = []) {
        foreach($deletes as &$_){
            if(isset($_["q"]) && !$_["q"]){
                $_["q"] = (Object)[];
            }
            if(isset($_["limit"]) && !$_["limit"]){
                $_["limit"] = 0;
            }
        }
        $cmd = [
            "delete"    => $collname,
            "deletes"   => $deletes,
        ];
        $cmd += $writeOps;
        return $this->command($cmd);
    }
 
    /**
     * 更新数据
     * @param  string $collname
     * @param  array  $updates      [["q"=>query,"u"=>update,"upsert"=>boolean,"multi"=>boolean], ...]
     * @param  array  $writeOps     ["ordered"=>boolean,"writeConcern"=>array]
     * @return \MongoDB\Driver\Cursor
     */
    function update($collname, array $updates, array $writeOps = []) {
        $cmd = [
            "update"    => $collname,
            "updates"   => $updates,
        ];
        $cmd += $writeOps;
        return $this->command($cmd);
    }
 
    /**
     * 查询
     * @param  string $collname
     * @param  array  $filter     [query]     参数详情请参见文档。
     * @return \MongoDB\Driver\Cursor
     */
    function query($collname, array $filter, array $writeOps = []){
        $cmd = [
            "find"      => $collname,
            "filter"    => $filter
        ];
        $cmd += $writeOps;
        return $this->command($cmd);
    }
 
    /**
     * 执行MongoDB命令
     * @param array $param
     * @return \MongoDB\Driver\Cursor
     */
    function command(array $param) {
        $cmd = new MongoDB\Driver\Command($param);
        return $this->_conn->executeCommand($this->_db, $cmd);
    }
 
    /**
     * 获取当前mongoDB Manager
     * @return MongoDB\Driver\Manager
     */
    function getMongoManager() {
        return $this->_conn;
    }
}
```
测试代码：mongo_test.php
```
<?php
 
require_once 'm_mgdb.php';
 
// 示例代码
//$db = m_mgdb::i("mdb1"); // 使用配置self::$_config["mdb1"]
$db = m_mgdb::i();         // 使用配置self::$_config[self::$def]
$collname = "proinfo";
 
 
// echo "\n---------- 查询支持命令 -----------\n";
// $cmd = [
//     "listCommands" => 1,
// ];
// $rs = $db->command($cmd);
// print_r($rs->toArray());
 
 
echo "\n---------- 删除 proinfo 所有数据 -----------\n";
$delets = [
    ["q" => [],"limit" => 0]
];
$rs = $db->del($collname, $delets);
print_r($rs->toArray());
 
 
echo "\n---------- 创建索引 -----------\n";
$cmd = [
    "createIndexes" => $collname,
    "indexes"       => [
        ["name" => "proname_idx", "key" => ["name"=>1],"unique" => true],
    ],
];
$rs = $db->command($cmd);
print_r($rs->toArray());
 
 
echo "\n---------- 查询索引 -----------\n";
$cmd = [
    "listIndexes" => $collname,
];
$rs = $db->command($cmd);
print_r($rs->toArray());
 
 
echo "\n------------ 插入数据 ---------\n";
$rows = [
    ["name" => "ns w1","type"=>"ns","size"=>["height"=>150,"width"=>30],"price"=>3000],
    ["name" => "ns hd","type"=>"ns","size"=>["height"=>154,"width"=>30],"price"=>3500],
    ["name" => "ns w3","type"=>"ns","size"=>["height"=>160,"width"=>30],"price"=>3800],
    ["name" => "bt s1","type"=>"bt","size"=>["height"=>158,"width"=>32],"price"=>3500],
    ["name" => "bt w1","type"=>"bt","size"=>["height"=>157,"width"=>30],"price"=>3600],
    ["name" => "an w1","type"=>"bt","size"=>["height"=>157,"width"=>30],"price"=>3700],
    ["name" => "wn w6","type"=>"wn","size"=>["height"=>157,"width"=>30],"price"=>3500],
];
$rs = $db->insert($collname, $rows);
print_r($rs->toArray());
 
 
echo "\n---------- 查询数据 -----------\n";
$filter = [
    "name" => ['$regex' => '\sw\d'], // mongo 正则匹配
    '$or'  => [["type"  => "bt"], ["size.height" => ['$gte' => 160]]]
];
$queryWriteOps = [
    "projection" => ["_id"   => 0],
    "sort"       => ["price" => -1],
    "limit"      => 20
];
$rs = $db->query($collname, $filter, $queryWriteOps);
print_r($rs->toArray());
 
 
echo "\n---------- 更新数据 -----------\n";
$updates = [
    [
        "q"     => ["name" => "ns w3"],
        "u"     => ['$set' => ["size.height" => 140],'$inc' => ["size.width" => 14]],
        "multi" => true,
    ]
];
$rs = $db->update($collname, $updates);
print_r($rs->toArray());
 
 
echo "\n---------- 查询数据 -----------\n";
$filter = [
    "name" => "ns w3",
];
$rs = $db->query($collname, $filter, $queryWriteOps);
print_r($rs->toArray());
```

转载[https://blog.csdn.net/color_wind/article/details/52008674](https://blog.csdn.net/color_wind/article/details/52008674)
