---
title: PHP-依赖注入容器
categories: PHP
---

![2020-11-13_5fae3e971d521.png](https://upload-images.jianshu.io/upload_images/15325592-4235978e3b9db610.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  介绍

> 使用 PHP 的反射类 ReflectionClass，创建容器方便管理依赖注入。

#  代码

```
<?php
interface GrowthInterface
{
    public function evolve();
}

class Agumon implements GrowthInterface
{
    public function evolve()
    {
        echo "亚古兽进化\n";
    }
}

class Gabumon implements GrowthInterface
{
    public function evolve()
    {
        echo "加布兽进化\n";
    }
}

class DigitalBaby
{
    public $growth;
    
    public function __construct(GrowthInterface $growth)
    {
        $this->growth = $growth;
    }
}

class DigitalWorld
{
    protected $instances = [];
    protected $bind = [];
    
    public function set($digitalBabyName, $digitalBaby)
    {
        if (!class_exists($digitalBaby)) {
            echo '我不知道数码宝贝是什么';
        } else {
            $this->bind[$digitalBabyName] = $digitalBaby;
        }
    }

    public function get($digitalBabyName, $digitalBaby)
    {
        if (isset($this->instances[$digitalBabyName])) {
            return $this->instances[$digitalBabyName];
        }
        if (!isset($this->bind[$digitalBabyName])) {
            echo $digitalBabyName."这只数码宝贝貌似不存在";
        }
        $reflect = new ReflectionClass($this->bind[$digitalBabyName]);
        return $this->instances[$digitalBabyName] = $reflect->newInstanceArgs($digitalBaby);
    }
}

$digitalWorld = new DigitalWorld();
$digitalWorld->set('Agumon','DigitalBaby');
$digitalWorld->set('Gabumon','DigitalBaby');
echo $digitalWorld->get('Agumon',[new Agumon])->growth->evolve();
echo $digitalWorld->get('Gabumon',[new Gabumon])->growth->evolve();
```

> 创建 digitalBaby.php，代码如上。

#  执行

```
$ php digitalBaby.php
亚古兽进化
加布兽进化
```
