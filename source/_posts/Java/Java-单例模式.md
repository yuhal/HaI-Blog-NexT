---
title: Java-单例模式
categories: Java
---
![WechatIMG148.jpeg](https://upload-images.jianshu.io/upload_images/15325592-eb0992af871b510f.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



#  介绍
> wiki:单例模式，也叫单子模式，是一种常用的软件设计模式。在应用这个模式时，单例对象的类必须保证只有一个实例存在。许多时候整个系统只需要拥有一个的全局对象，这样有利于我们协调系统整体的行为。实现单例模式的思路是：一个类能返回对象一个引用(永远是同一个)和一个获得该实例的方法（必须是静态方法，通常使用 `getInstance` 这个名称）；当我们调用这个方法时，如果类持有的引用不为空就返回这个引用，如果类保持的引用为空就创建该类的实例并将实例的引用赋予该类保持的引用；同时我们还将该类的构造函数定义为私有方法，这样其他处的代码就无法通过调用该类的构造函数来实例化该类的对象，只有通过该类提供的静态方法来得到该类的唯一实例。


#  角色 

|角色|    说明|
 | ------------ |------------ |
|Single|单例类|

#  角色示例

|类名 |担任角色|  说明|
| ------------ | ------------ |------------ |
|IdCard|Single|身份证类|


#  UML类图

![单例模式.jpg](https://upload-images.jianshu.io/upload_images/15325592-265fac085a967dbe.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  代码

```
import java.util.ArrayList;
class Idcard {
    private volatile static Idcard idcard;

    private Idcard() { }

    private String number;

    public static Idcard getIdcard() {
        if (idcard == null) {
            synchronized(Idcard.class) {
                if (idcard == null) {
                    idcard = new Idcard();
                }
            }
        }
        return idcard;
    }

    public void setNumber(String number){
        this.number = number;
    }

    public String getNumber(){
        return number;
    }
}

public class IdcardTest {
    public static void main(String[] args) {
        Idcard idcard = Idcard.getIdcard();
        idcard.setNumber("329728202003289098");
        System.out.println(idcard.getNumber());
    }
}
```
> 创建 IdcardTest.java，代码如上。

#  执行

```
$ javac IdcardTest.java
$ java IdcardTest
329728202003289098
```
