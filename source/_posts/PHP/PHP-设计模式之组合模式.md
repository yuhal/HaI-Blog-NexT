---
title: PHP-设计模式之组合模式
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-cd1376c910d73d88.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
当我们的一个对象可能代表一个单一的实体，或者一个组合的实体，
但是仍然需要通过同样的方式被使用时，这种情形则适合使用组合模式的设计。
组合模式是一种结构型模式。
# 初步理解：
![image](https://upload-images.jianshu.io/upload_images/15325592-f82b30b812d9bf3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
![image](https://upload-images.jianshu.io/upload_images/15325592-9759fe8bb7b6f940.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
![image](https://upload-images.jianshu.io/upload_images/15325592-0ec9c61ad2065862.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
![image](https://upload-images.jianshu.io/upload_images/15325592-5d2b429d814a8716.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# Code:
```
<?php

/**
 * 组合模式抽象基类
 */
abstract class CompanyBase{
    //节点名称
    protected $name;

    public function __construct($name){

        $this->name = $name;
    }

    public function getName(){
        return $this->name;
    }

    //增加节点
    abstract function add(CompanyBase $c);

    //删除节点
    abstract function remove(CompanyBase $c);

    //输出节点信息
    abstract function show($deep);

    //节点职责
    abstract function work($deep);

}

/**
 * 公司类
 */
class Company extends CompanyBase{
    protected $item = [];

    public function add(CompanyBase $c){
        $nodeName = $c->getName();

        if(!isset( $this->item[$nodeName] )){

            $this->item[$nodeName] = $c;
        }else{
            throw new Exception("该节点已存在,节点名称：".$nodeName);
        }
    }

    public function remove(CompanyBase $c){
        $nodeName = $c->getName();

        if(isset( $this->item[$nodeName] )){

            unset($this->item[$nodeName]);
        }else{
            throw new Exception("该节点不存在,节点名称：".$nodeName);
        }
    }

    public function show($deep = 0){
        echo str_repeat("-",$deep).$this->name;
        echo PHP_EOL;

        foreach($this->item as $value){
            $value->show($deep+4);
        }

    }
    public function work($deep = 0){

        foreach($this->item as $value){
            echo str_repeat("   ",$deep)."[{$this->name}]".PHP_EOL;
            $value->work($deep+2);
        }
    }

}

/**
 * 人力资源部门
 */
class HumanResources extends CompanyBase{

    public function add(CompanyBase $c){
        throw new Exception("该节点下不能增加节点");
    }

    public function remove(CompanyBase $c){

        throw new Exception("该节点下无子节点");
    }

    public function show($deep = 0){
        echo str_repeat("-",$deep).$this->name;
        echo PHP_EOL;

    }
    public function work($deep = 0){

        echo str_repeat("   ",$deep)."人力资源部门的工作是为公司招聘人才".PHP_EOL;
        echo PHP_EOL;
    }

}

/**
 * 商务部门
 */
class Commerce extends CompanyBase{

    public function add(CompanyBase $c){
        throw new Exception("该节点下不能增加节点");
    }

    public function remove(CompanyBase $c){

        throw new Exception("该节点下无子节点");
    }

    public function show($deep = 0){
        echo str_repeat("-",$deep).$this->name;
        echo PHP_EOL;

    }
    public function work($deep = 0){

        echo str_repeat("   ",$deep)."商务部门的工作是为公司赚取利润".PHP_EOL;
        echo PHP_EOL;
    }
}

$c = new Company("北京某科技公司");
$h = new HumanResources("人力资源部门");
$com = new Commerce("商务部门");
$c->add($h);
$c->add($com);

//天津分公司
//为了偷懒，分公司的部门直接copy母公司的
$c1 = new Company("天津分公司");
$c1->add($h);
$c1->add($com);
$c->add($c1);

//武汉分公司
$c2 = new Company("武汉分公司");
$c2->add($h);
$c2->add($com);
$c->add($c2);

//使用公司功能
$c->show();
$c->work();

/*输出
北京某科技公司
----人力资源部门
----商务部门
----天津分公司
--------人力资源部门
--------商务部门
----武汉分公司
--------人力资源部门
--------商务部门
[北京某科技公司]
      人力资源部门的工作是为公司招聘人才

[北京某科技公司]
      商务部门的工作是为公司赚取利润

[北京某科技公司]
      [天津分公司]
            人力资源部门的工作是为公司招聘人才

      [天津分公司]
            商务部门的工作是为公司赚取利润

[北京某科技公司]
      [武汉分公司]
            人力资源部门的工作是为公司招聘人才

      [武汉分公司]
            商务部门的工作是为公司赚取利润
*/
```
# 总结组合模式的特点：
- 必须存在不可分割基本元素；
- 组合后的物体任然可以被组合。

