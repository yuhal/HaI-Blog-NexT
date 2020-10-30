---
title: JS-创建对象的四种方式
categories: JS
---

![WechatIMG2.png](https://upload-images.jianshu.io/upload_images/15325592-845b3fd349885897.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 通过对象字面量来创建

```
var duelist = {
  name: "武藤游戏",
  age: 16,
  gender: "男",
  sayHi: function () {
    console.log("你好，我的名字是 " + this.name);
  },
};
```

- 通过 new Object() 创建对象

```
var duelist = new Object();
  (duelist.name = "阿图姆"),
  (duelist.age = 3000),
  (duelist.gender = "男"),
  (duelist.sayHi = function () {
    console.log("你好，我的名字是 " + this.name);
});
```

- 通过工厂函数来创建对象

```
function createDuelist(name, age, gender) {
  var duelist = new Object();
  duelist.name = name;
  duelist.age = age;
  duelist.gender = gender;
  duelist.sayHi = function () {
    console.log("你好，我的名字是 " + this.name);
  };
  return duelist;
}
var d1 = createDuelist("武藤游戏", 16, "男");
var d2 = createDuelist("阿图姆", 3000, "男");
```

- 通过构造函数来创建对象

```
function Duelist(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
  this.sayHi = function () {
    console.log("你好，我的名字是 " + this.name);
  };
}
var d1 = new Duelist("武藤游戏", 16, "男");
var d2 = new Duelist("阿图姆", 3000, "男");
```

- 工厂函数和构造函数的区别

|   |创建对象方式  |return 语句|调用方式|
| ------------ | ------------ |------------ |------------ |
| 工厂函数  | 函数内部创建  |有| 赋值调用|
|  构造函数 | 赋值 this 对象 |无| 实例化调用|
