---
title: JS-构造函数存在的问题
categories: JS
---

![e4b867b91685cb2b19cd6622924f9c839e3a2373.jpg_640w_400h.png](https://upload-images.jianshu.io/upload_images/15325592-db9046b37dfe3676.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  问题

```
function DuelMonster(name, gender, attack) {
  this.name = name;
  this.gender = gender;
  this.attack = attack;
  this.useSkill = function () {
    console.log("黑魔导");
  };
}

var m1 = new DuelMonster("黑魔术师", "male", 2500);
m1.useSkill(); // 打印黑魔导

var m2 = new DuelMonster("黑魔导少女", "female", 2000);
m2.useSkill(); // 打印黑魔导

console.log(m1.useSkill == m2.useSkill); // 结果为 false
```

> 在创建完`DuelMonster`构造函数后，又创建两个实例化对象`m1`和`m2`去调用`useSkill()`方法，然后打印这两个方法是否相等，返回了 false 。由于每个对象都是由 `new DuelMonster`创建出来的，因此每创建一个对象，函数 `useSkill()`都会被重新创建一次，这个时候，每个对象都调用了功能完全相同的方法，但是它们分别是独立的。

#  解决

- 方法一

```
function useSkill() {
  console.log("黑魔导");
}

function DuelMonster(name, gender, attack) {
  this.name = name;
  this.gender = gender;
  this.attack = attack;
  this.useSkill = useSkill;
}

var m1 = new DuelMonster("黑魔术师", "male", 2500);
m1.useSkill(); // 打印黑魔导
var m2 = new DuelMonster("黑魔导少女",  "female", 2000);
m2.useSkill(); // 打印黑魔导
console.log(m1.useSkill == m2.useSkill); // 结果为 true
```

> 单独把`useSkill()`方法提出来，再每次调用

- 方法二

```
function DuelMonster(name, gender, attack) {
  this.name = name;
  this.gender = gender;
  this.attack = attack;
}

DuelMonster.prototype.useSkill = function () {
  console.log("黑魔导");
};

var m1 = new DuelMonster("黑魔术师", "male", 2500);
m1.useSkill(); // 打印黑魔导
var m2 = new DuelMonster("黑魔导少女",  "female", 2000);
m2.useSkill(); // 打印黑魔导
console.log(m1.useSkill == m2.useSkill); // 结果为 true
```

> 使用 JS 中的 prototype (原型)，指向另一个对象。这个对象的所有属性和方法，都会被构造函数的实例继承。在这里，`useSkill()`方法被`DuelMonster`构造函数所继承。
