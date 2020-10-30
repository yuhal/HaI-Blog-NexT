---
title: Java-适配器模式
categories: Java
---
![2020-09-04_5f51b217c547a.jpg](https://upload-images.jianshu.io/upload_images/15325592-6d2ad5179ad408e4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  介绍

> wiki:在设计模式中，适配器模式（英语：adapter pattern）有时候也称包装样式或者包装(wrapper)。将一个类的接口转接成用户所期待的。一个适配使得因接口不兼容而不能在一起工作的类工作在一起，做法是将类自己的接口包裹在一个已存在的类中。


#  角色 

|角色|    说明|
 | ------------ |------------ |
  |Target |目标抽象类 |
 |Adapter |适配器类 |
 |Adaptee |适配者类 |
 |Client |客户类 |


#  角色示例

|类名 |担任角色|  说明|
| ------------ | ------------ |------------ |
|ChargerInterface|Target|充电器接口类|
|Converter|Adapter|转换器类|
|Charger|Adaptee|充电器类|
|MacBookPro|Client|MacBookPro 类|


#  UML类图

![适配器模式.jpg](https://upload-images.jianshu.io/upload_images/15325592-0ffab3f3005dbd9b.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  代码

```
class Charger {
    public String TypeC() {
        return "TypeC";
    }
}

interface ChargerInterface{
    public String USB();
}

class Converter implements ChargerInterface {
    private Charger charger;

    public Converter(Charger charger){
        this.charger = charger;
    }

    public String USB(){
        return "USB 转换 "+this.charger.TypeC();
    }
}

class MacBookPro {
    private ChargerInterface converter;

    public MacBookPro(ChargerInterface converter){
        this.converter = converter;
    }

    public String convert(){
        return this.converter.USB();
    }
}

class ConverterTest {
    public static void main(String[] args) {
        Charger charger = new Charger();
        ChargerInterface converter = new Converter(charger);
        MacBookPro macBookPro = new MacBookPro(converter);
        System.out.println(macBookPro.convert());
    }
}
```
> 创建 ConverterTest.java，内容如上。

#  执行

```
$ javac ConverterTest.java
$ java ConverterTest
USB 转换 TypeC
```
