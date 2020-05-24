---
title: PHP-设计模式之结构性模式
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-999a954018170721.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

结构型模式是解析类和对象的内部结构和外部组合，通过优化程序结构解决模块之间的耦合问题。
种类：适配器模式、桥接模式、装饰模式、组合模式、外观模式、享元模式、代理模式
# 适配器模式（adapter）
将一个类的接口转换成客户希望的另一个接口,适配器模式使得原本的由于接口不兼容而不能一起工作的那些类可以一起工作。
应用场景：老代码接口不适应新的接口需求，或者代码很多很乱不便于继续修改，或者使用第三方类库。
```
<?php
/**
*
* 适配器模式
*
*/

//旧代码
class User {
    private $name;

    function __construct($name) {
        $this->name = $name;
    }

  	public function getName() {
   		return $this->name;
  	}
}
   
//新代码，开放平台标准接口
interface UserInterface {
    function getUserName();
}

class UserInfo implements UserInterface {
    protected $user;

    function __construct($user) {
        $this->user = $user;
    }

    public function getUserName() {
        return $this->user->getName();
    }
}

$olduser = new User('张三');
echo $olduser->getName()."\n";

$newuser = new UserInfo($olduser);
echo $newuser->getUserName()."\n";
   
?>
```
注意：这里的新接口使用了组合方式，UserInfo内部有一个成员变量保存老接口User对象，模块之间是松耦合的，这种结构其实就是组合模式。不要使用继承，虽然UserInfo继承User也能达到同样的目的，但是耦合度高，相互产生影响。
# 桥接模式（bridge）
将抽象部分与它的实现部分分离，使它们都可以独立变化
特点：独立存在，扩展性强
应用：需要不断更换调用对象却执行相同的调用方法，实现扩展功能
```
<?php
/**
*
* 桥接模式
* 
*/
 
abstract class Person {
  abstract function getJob();
}
 
class Student extends Person {
  public function getJob() {
    return '学生';
  }
}
 
class Teacher extends Person {
  public function getJob() {
    return '老师';
  }
}
 
class BridgeObj {
  protected $_person;

  public function setPerson($person) {
    $this->_person = $person;
  }

  public function getJob() {
    return $this->_person->getJob();
  }
}
       
$obj = new BridgeObj();
$obj->setPerson(new Student());
printf("本次桥接对象：%s\n", $obj->getJob());

$obj->setPerson(new Teacher());
printf("本次桥接对象：%s\n", $obj->getJob());
?>
```
# 装饰模式（decorate）
动态地给一个对象添加额外的职责。在原有的基础上进行功能增强。
特点：用来增强原有对象功能，依附于原有对象。
应用：用于需要对原有对象增加功能而不是完全覆盖的时候 
```
<?php
/**
* 
* 装饰模式
*
*/

//产品
abstract class Person {
    abstract function getPermission();
}
//被装饰者
class User extends Person {
    public function getPermission() {
        return '公开文档';
    }
}
//装饰类
class PermUser extends Person {
    protected $_user;

    protected $_special = '';

    function __construct($user) {
        $this->_user = $user;
    }

    public function getPermission() {
        return $this->_user->getPermission() . $this->_special;
    }
}

//装饰类产品
class JavaUser extends PermUser {
    protected $_special = ' java程序';
}

class CPlusUser extends PermUser {
    protected $_special = ' c++程序';
}


$user = new User();
printf("permission：%s\n", $user->getPermission());

$user = new JavaUser($user);
printf("permission：%s\n", $user->getPermission());

$user = new CPlusUser($user);
printf("permission：%s\n", $user->getPermission());
?>
```
# 组合模式（combination）
将对象组合成树形结构表示“部分-整体”的层次结构。
特点：灵活性强
应用：对象的部分-整体的层次结构，模糊组合对象和简单对象处理问题
```
<?php
/**
*
* 组合模式
*
*/
   
//继承模式
class UserBaseInfo {
    private $name;

    function __construct($name) {
        $this->name = $name;
    }
    public function getName() {
   		return $this->name;
    }
}

class User extends UserBaseInfo {
    private $login = false;
     
    public function setLogin($islogin) {
   		$this->login = $islogin;
    }
    public function isLogin() {
    	return $this->login;
    }
}

$user = new User('张三');
$user->setLogin(true);
if($user->isLogin()) {
    echo $user->getName()."已经登录了\n";
} else {
    echo $user->getName()."还没有登录\n";
}


//组合模式
class LoginInfo {
    protected $user;

    protected $login = false;
     
    public function setLogin($user, $isLogin){
        $this->user = $user;
        $this->login = $isLogin;
    }

    public function isLogin() {
        return $this->login;
    }
}

$user = new User('张三');
$login = new LoginInfo();
$login->setLogin($user,true);
if($login->isLogin()) {
     echo $user->getName()."已经登录了\n";
} else {
     echo $user->getName()."还没有登录\n";
}

//部分可以更换，用继承则不行
class Admin {
    protected $level;

    function __construct($level) {
        $this->level = $level;
    }

    function getLevel() {
        return $this->level;
    }
}
$admin = new Admin(1);
$login->setLogin($admin,true);
if($login->isLogin()) {
     printf("级别为 %d 的管理员已经登录了\n",$admin->getLevel());
} else {
     printf("级别为 %d 的管理员还没有登录\n",$admin->getLevel());
}

?>
```
上面面的例子分别展示了使用继承和组合来处理新功能，在简单的情况下看似区别不大，但在项目后期越来越复杂的时候组合模式的优势就越来越明显了。
例如上面的登录信息，如果要增加登录次数、最后登录时间、登录ip等信息，登录本身就会变成一个比较复杂的对象。如果以后有新的需求比如好友信息、用户的访问信息等，再要继承的话，用户类就会变得非常庞大，难免各父类之间没有冲突的变量和方法，而外部访问用户类的众多方法也变得很费劲。采用组合模式后，一个类负责一个角色，功能区分非常明显，扩展方便。
# 外观模式/门面模式（appearance）
为了系统中的一组接口提供一个一致的界面
特点：向上抽取，有共性
应用：内部接口众多，由统一的接口来调用
 ```
 <?php
/**
 *
 * 外观模式，也叫门面模式
 *
 */
   
   
class Operation {
     public function testPlus() {
        printf("plus: %s\n", (1+2 == 3 ? 'true' : 'false'));
     }

     public function testMinus() {
        printf("minus: %s\n", (3-2 == 2 ? 'true' : 'false'));
     }

     public function testTimes() {
        printf("times: %s\n", (2*3 == 6 ? 'true' : 'false'));
     }
}
   
class Tester {
    protected $_operation;

    function __construct() {
        $this->_operation = new Operation();
    }

    public function testAll() {
        $this->_operation->testPlus();
        $this->_operation->testMinus();
        $this->_operation->testTimes();
    }
}
 
//测试用例，测试全部接口
$tester = new Tester();
$tester->testAll();
?>
```
门面模式估计大家在实际代码中都已经使用到了，接口较多时把相似功能的接口封装成一个接口供外部调用，这就是门面模式。
# 代理模式（agency）
为其他对象提供一个代理来控制对这个对象的访问，就是给某一对象提供代理对象，并由代理对象控制具体对象的引用。能够协调调用者和被调用者，能够在一定程度上降低系统的耦合性。
特点：低耦合性，独立性好，安全性
应用：客户访问不到或者被访问者希望隐藏自己，所以通过代理来访问自己。
```
<?php
/**
 *
 * 代理模式
 *
 */
   
//内部对象
class User {
    public function getName() {
        return '张三';
    }

    public function getType() {
        return '付费用户';
    }
}
 
//代理接口定义，例如开放平台
interface UserInterface {
    function getName();
}
//代理对象
class UserProxy implements UserInterface {
    protected $_user;

    function __construct() {
        $this->_user = new User();
    }

    public function getName() {
        return $this->_user->getName();
    }
}
 
//内部调用
$user = new User();
printf("username：%s\n", $user->getName());
printf("usertype：%s\n", $user->getType());

//外部调用
// $user = new UserProxy();
// printf("username：%s\n", $user->getName());
// printf("usertype：%s\n", $user->getType());//不能访问，即使知道内部对象有这个方法 
?>
```
模式的选用要根据实际的业务需求，通过对业务逻辑的仔细分析，再根据模式具有的特性和应用场景进行合理的选择和区分。大部分情况下业务的场景决定了哪种模式，而不是选择哪个模式去实现一个业务，少数情况几种模式确实都能解决问题，那主要就是考虑以后的扩展了。
