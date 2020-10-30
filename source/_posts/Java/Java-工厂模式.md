---
title: Java-工厂模式
categories: Java
---
![WechatIMG136.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e86712e339ec0337.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  介绍

> 定义一个创建对象的接口，但让实现这个接口的类来决定实例化哪个类。

#  角色

| 角色  | 说明  |
| ------------ | ------------ |
| Factory| 抽象工厂类，负责创建具体产品的实例| 
| Product| 抽象产品类，定义产品子类的公共接口| 
| ConcreteProduct| 具体产品类，实现 Product 父类的接口功能，也可添加自定义的功能| 

#  角色示例

| 类名  |担任角色  | 说明  |
| ------------ | ------------ | ------------ |
| Phone  | Product| 手机类，定义手机子类的公共接口  |
|  IPhoneX | ConcreteProduct|  IPhoneX 手机类，实现 IPhoneX 类的接口功能，也可添加自定义的功能 |
|  HUAWEIP40 | ConcreteProduct | HUAWEIP40 手机类，实现 HUAWEIP40 类的接口功能，也可添加自定义的功能 |
|PhoneFactory|Factory|手机工厂类，负责生产手机的实例|
|FactoryTest|Factory|工厂测试类，负责调用生产什么型号手机|

#  UML 类图

![工厂模式.jpg](https://upload-images.jianshu.io/upload_images/15325592-13fa6d56d7be5c0f.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  普通工厂模式

- 创建 Phone.java，代码如下：

```
interface Phone{
    public void call();
    public void photograph();
}
```

- 创建 HUAWEIP40.java，代码如下：

```
class HUAWEIP40 implements Phone{
    public void call(){
        System.out.println("HUAWEIP40 can call.");
    }
    public void photograph(){
        System.out.println("HUAWEIP40 can photograph.");
    }
}
```

- 创建 IPhoneX.java，代码如下：

```
class IPhoneX implements Phone{
    public void call(){
        System.out.println("IPhoneX can call.");
    }
    public void photograph(){
        System.out.println("IPhoneX can photograph.");
    }
}
```

- 创建 PhoneFactory.java，代码如下：

```
class PhoneFactory{
    public Phone createPhone(String model){
        if( model.equals("IPhoneX") ){
           return new IPhoneX();
        }else if( model.equals("HUAWEIP40")){
           return new HUAWEIP40();
        }else {
            System.out.println("Please enter the correct model!");
            return null;
        }
    }
}
```

- 创建 FactoryTest.java，代码如下：

```
class FactoryTest {
    public static void main(String[] args){
        PhoneFactory factory = new PhoneFactory();
        Phone phone = factory.createPhone("IPhoneXS");
        phone.call();
        phone.photograph();
    }
}
```

- 执行

```
$ javac FactoryTest.java
$ java FactoryTest
Please enter the correct model!
```

> 普通工厂方法模式中，如果传递的字符串出错，则不能正确创建对象。

#  多个工厂方法模式

- 修改 PhoneFactory.java，代码如下：

```
class PhoneFactory{
    public IPhoneX createIPhoneX() {
        return new IPhoneX();
    }
    public HUAWEIP40 createHUAWEIP40() {
        return new HUAWEIP40();
    }
}
```

- 修改 FactoryTest.java，代码如下：

```
class FactoryTest {
    public static void main(String[] args){
        PhoneFactory factory = new PhoneFactory();
        Phone phone = factory.createIPhoneX();
        phone.call();
        phone.photograph();
    }
}
```

- 执行

```
$ javac FactoryTest.java
$ java FactoryTest
IPhoneX can call.
IPhoneX can photograph.
```

> 多个工厂方法模式是提供多个工厂方法，分别创建对象。

#  静态工厂方法模式

- 修改 PhoneFactory.java，代码如下：

```
class PhoneFactory{
    public static IPhoneX createIPhoneX() {
        return new IPhoneX();
    }
    public static HUAWEIP40 createHUAWEIP40() {
        return new HUAWEIP40();
    }
}
```

- 修改 FactoryTest.java，代码如下：

```
class FactoryTest {
    public static void main(String[] args){
        Phone phone = PhoneFactory.createHUAWEIP40();
        phone.call();
        phone.photograph();
    }
}
```

- 执行

```
$ javac FactoryTest.java
$ java FactoryTest
HUAWEIP40 can call.
HUAWEIP40 can photograph.
```

> 静态工厂方法模式里的方法是静态，可以直接调用。
