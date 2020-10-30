---
title: Java-抽象工厂模式
categories: Java
---
![5b1d63cbace7c2002ffa2546334171bad7bb404a.jpg](https://upload-images.jianshu.io/upload_images/15325592-90db23c17942aa1a.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  介绍

> baike:提供一个创建一系列相关或相互依赖对象的接口，而无须指定它们具体的类。抽象工厂模式又称为Kit模式，属于对象创建型模式。此模式是对工厂方法模式的进一步扩展。在工厂方法模式中，一个具体的工厂负责生产一类具体的产品，即一对一的关系，但是，如果需要一个具体的工厂生产多种产品对象，那么就需要用到抽象工厂模式了。

#  角色

| 角色 | 说明 |
| ------------ | ------------ |
|Factory|抽象工厂类，负责创建具体产品的实例|
|ConcreteFactory|具体工厂类，实现 Factory 父类的接口功能，也可添加自定义的功能|
|Product|抽象产品类，定义产品子类的公共接口|
|ConcreteProduct|具体产品类，实现 Product 父类的接口功能，也可添加自定义的功能|

#  角色示例

| 类名  |担任角色 | 说明  |
| ------------ | ------------ | ------------ |
|Foxconn|Factory|富士康工厂类，定义工厂子类的公共接口 |
|ShangHaiFoxconn|ConcreteFactory|上海富士康工厂类，实现工厂类的接口功能，也可添加自定义的功能|
|ShenZhenFoxconn|ConcreteFactory|深圳富士康工厂类，实现工厂类的接口功能，也可添加自定义的功能|
|Phone|Product|抽象手机类，定义手机子类的公共接口|
|IPhoneXS|ConcreteProduct|IPhoneXS手机类，实现手机类的接口功能，也可添加自定义的功能|
|Pad|Product|抽象平板类，定义平板子类的公共接口|
|IPadAir|ConcreteProduct|IPadAir平板类，实现平板类的接口功能，也可添加自定义的功能|

#  UML 类图

![WechatIMG133.png](https://upload-images.jianshu.io/upload_images/15325592-ad742cc88cc42002.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  代码

```
interface Phone {
    public void call();
}

class IPhoneX implements Phone {
    public void call() {
        System.out.println("IPhoneX can call.");
    }
}

class IPhoneXS implements Phone {
    public void call() {
        System.out.println("IPhoneXS can call.");
    }
}

interface Pad {
    public void photograph();
}

class IPadAir2 implements Pad{
    public void photograph() {
        System.out.println("IPadAir2 can photograph.");
    }
}

class IPadAir3 implements Pad{
    public void photograph() {
        System.out.println("IPadAir3 can photograph.");
    }
}

interface Foxconn{
    public Phone createPhone();
    public Pad createPad();
}

class ShangHaiFoxconn implements Foxconn {
    public Phone createPhone() {
       return new IPhoneX();
    }
    public Pad createPad() {
       return new IPadAir2();
    }
}

class ShenZhenFoxconn implements Foxconn {
    public Phone createPhone() {
       return new IPhoneXS();
    }
    public Pad createPad() {
       return new IPadAir3();
    }
}

class FactoryTest {
    public static void main(String[] args) {
       ShenZhenFoxconn shenZhenFoxconn = new ShenZhenFoxconn();
       Phone phone = shenZhenFoxconn.createPhone();
       phone.call();
       Pad pad = shenZhenFoxconn.createPad();
       pad.photograph();
    }
}
```

> 创建 FactoryTest.php，代码如上。

#  执行

```
$ javac FactoryTest.java 
$ java FactoryTest
IPhoneXS can call.
IPadAir3 can photograph.
```
