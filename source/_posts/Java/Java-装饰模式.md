---
title: Java-装饰模式
categories: Java
---
![2020-09-04_5f51e9777d251.jpeg](https://upload-images.jianshu.io/upload_images/15325592-5157ada07c1f26ba.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  介绍

> 装饰模式，可称为装饰器模式或修饰模式，是面向对象编程领域中，一种动态地往一个类中添加新的行为的设计模式。在原有的基础上进行功能增强。就功能而言，装饰模式相比生成子类更为灵活，这样可以给某个对象而不是整个类添加一些功能。特点是用来增强原有对象功能，依附于原有对象。应用在用于需要对原有对象增加功能而不是完全覆盖的场景。


#  角色 

|角色|    说明|
 | ------------ |------------ |
 |Component | 抽象构件 |
 |ConcreteComponent | 具体构件 |
 |Decorator |抽象装饰类 |
 |ConcreteDecorator | 具体装饰类 |

#  角色示例

|类名 |担任角色|  说明|
| ------------ | ------------ |------------ |
|Soldier|Component|士兵|
|LandSoldier|ConcreteComponent|陆军|
|SeaSoldier|ConcreteComponent|海军|
|SoldierArsenal|Decorator|士兵军火库|
|M4a1|ConcreteDecorator|M4a1枪支|
|Ak47|ConcreteDecorator|Ak47枪支|

#  UML类图

![2020-09-04_5f51e8aa3d4aa.jpg](https://upload-images.jianshu.io/upload_images/15325592-a10f84e9572a38d1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



#  代码

```
abstract class Soldier {
    String weapon = "no weapon";

    public String getWeapon(){
        return weapon;
    }
}

class LandSoldier extends Soldier {
    public LandSoldier() {
        weapon = "+LandSoldier";
    }
}

class SeaSoldier extends Soldier {
    public SeaSoldier() {
        weapon = "+SeaSoldier";
    }
}

abstract class SoldierArsenal extends Soldier {
    public abstract String getWeapon();
}

class M4a1 extends SoldierArsenal {

    private Soldier soldier;

    public M4a1(Soldier s) {
        soldier = s;
    }

    @Override
    public String getWeapon() {
        return soldier.getWeapon() + "+with M4a1";
    }

}

class Ak47 extends SoldierArsenal {
    
    private Soldier soldier;

    public Ak47(Soldier s) {
        soldier = s;
    }

    @Override
    public String getWeapon() {
        return soldier.getWeapon() + "+with Ak47";
    }

}

public class SoldierTest {
    public static void main(String[] args) {
        Soldier s1 = new LandSoldier();
        System.out.println(s1.getWeapon());

        M4a1 s2 = new M4a1(s1);
        System.out.println(s2.getWeapon());

        Ak47 s3 = new Ak47(s2);
        System.out.println(s3.getWeapon());
    }
}
```
> 创建 SoldierTest.java，内容如上。

#  执行

```
$ javac SoldierTest.java
$ java SoldierTest
+LandSoldier
+LandSoldier+with M4a1
+LandSoldier+with M4a1+with Ak47
```
