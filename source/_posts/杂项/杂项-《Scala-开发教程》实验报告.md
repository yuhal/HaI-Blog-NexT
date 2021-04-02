---
title: 杂项-《Scala-开发教程》实验报告
categories: 杂项
---
![61c02dc478e51a0828eaa771d4f943ccde528cc2.jpg](https://upload-images.jianshu.io/upload_images/15325592-88cbcc01df04b913.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![Scala 开发教程.jpg](https://upload-images.jianshu.io/upload_images/15325592-231302fbb9a0511c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  Scala 基础

- 定义变量

```
#  字符串常变量
val girl = "诸叶"
#  字符串变量
var weapon = "俱利伽罗丸"
```

- 定义函数

```
#  有返回值
def transform(rouge:Boolean) : String ={
    if (rouge) "崩国的红夜叉"
else
    "无变化"
}
#  无返回值
def skill() = println("红龙破")
```

- 判断

```
var modern = true
val current = if (modern) "现代" else "战国时代"
```

- 循环

```
#  while
val girls = Array("永远","刹那","诸叶")
var i = 0
while (i < 3) {
    println(girls(i))
    i += 1
}
#  for
for (girl <- girls)
    println(girl)
#  foreach
girls.foreach(println)
```

- 数组

```
val weapons = Array("菊十文字","兼光之巴","俱利伽罗丸")
for(i <- 0 to 2)
    print(weapons(i))
```

- 列表

```
#  定义
val pearls = List("银色珍珠","金色珍珠","红色珍珠")
#  打印
print(pearls)
#  取List的首元素
pearls.head
#  判断List是否为空
pearls.isEmpty
#  取除首元素之外的List的其它元素
pearls.tail
#  逆转List中元素的顺序
pearls.reverse
#  返回除前1个元素的List余下的元素
pearls drop 1
#  返回List的前1个元素
pearls take 1
#  把一个List在指定位置分成两个List
pearls splitAt 1
#  展开List
pearls.flatten
#  zip
pearls.indices zip pearls
pearls zip List(1,2,3)
#  unzip
pearls.zipWithIndex.unzip
#  显示List的正规字符表示
pearls.toString
#  格式化List显示
pearls.mkString
#  map
pearls map(_+"x1")
pearls map(_.length)
#  flatMap 
pearls flatMap(_.toList)
#  过滤List
pearls filter (_=="银色珍珠")
```

- 元组

```
val fathers = ("杀生丸","犬夜叉")
print(fathers._1)
```

- 集合

```
#  Set
var girls = Set ("诸叶","刹那")
girls += "永远"
print(girls.contains("芽衣"))
#  Map
val weapons = Map( "永远" -> "菊十文字","刹那" -> "兼光之巴","诸叶" -> "俱利伽罗丸")
print(weapons("永远"))
```

- 读取文件

```
import scala.io.Source
var file_content = Source.fromFile(文件路径)
```

- 异常处理

```
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException
try {
    val f = new FileReader(文件路径)
} catch {
    #  处理不存在的文件
    case ex: FileNotFoundException =>
	#  处理IO错误
    case ex: IOException =>
}
```

#  类和对象

- 类

```
#  定义
class Weapon (w1:String, w2:String, w3:String) {
    print(w1+"\n"+w2+"\n"+w3)
}
#  调用
new Weapon("菊十文字", "兼光之巴", "俱利伽罗丸")
```

- 对象

```
#  定义
object Pearl {
    print("七彩珍珠")
}
#  调用
Pearl
```

- toString

```
#  定义
class Weapon (w1:String, w2:String, w3:String) {
    override def toString = w1+"\n"+w2+"\n"+w3
}
#  调用
new Weapon("菊十文字", "兼光之巴", "俱利伽罗丸")
```

- require

```
#  定义
class RedPearl (color:String) {
    require(color == "红色")
    override def toString = "红色珍珠"
}
#  调用
new RedPearl("红色")
```

- 成员变量

```
#  定义
class Pearl (c:String) {
    val color = c
    override def toString = c+"珍珠"
}
#  调用
val p = new Pearl("金色")
p.color
```

- 私有成员变量

```
#  定义
class Pearl (c:String) {
    #  不能被访问
    private val color = c
    override def toString = c+"珍珠"
}
#  调用
new Pearl("银色")
```

- 辅助构造函数

```
#  定义
class Pearl (p:String, n:String) {
    override def toString = p+"x"+n
	def this(p:String) = this(p, "1")
}
#  调用
new Pearl("银色珍珠")
```

- 私有成员方法

```
#  定义
class Girl (name:String) {
    val pearl = getPearl(name)
    override def toString = pearl
	private def getPearl(name:String):String =
        if (name == "永远") {
		    "银色珍珠"
		} else if (name == "刹那") {
		    "金色珍珠"
		} else if (name == "诸叶") {
		    "红色珍珠"
		} else {
			"未知"
		}
}
#  调用
new Girl("永远")
```

- 隐式参数

```
#  定义
class GoldPearl (implicit n:Int) {
    override def toString = "红色珍珠x"+n
}
#  调用
implicit val n = 1
new GoldPearl()
```

#  函数

- 成员函数

```
#  定义
import scala.io.Source
object Girl {
	def weapon(w:String) {
		skill(w)
	}
	private def skill(w:String){
		print(w+"-旋风阵")
	}
}
#  调用
Girl.weapon("兼光之巴")
```

- 局部函数

```
#  定义
import scala.io.Source
object Girl {
	def weapon(w:String) {
		def skill(){
			print(w+"-旋风阵")
		}
		skill()
	}
}
#  调用
Girl.weapon("兼光之巴")
```

- 函数字面量

```
val skills = (_:String )+"+"+(_:String)
skills("旋风阵", "红龙破")
```

- 闭包函数

```
#  定义
def attack(weapon:String) = (skill:String) => weapon+"-"+skill
#  调用
val attack1 = attack("兼光之巴")
attack1("旋风阵")
val attack2 = attack("俱利伽罗丸")
attack2("红龙破")
```

- 重复参数

```
#  定义
def attack(skills:String *) = for (skill <- skills) println(skill)
#  调用
attack("旋风阵", "破魔之箭")
```

- 命名参数

```
#  定义
def attack(weapon:String, skill:String) :String = weapon+"-"+skill
#  调用
attack(weapon="兼光之巴", skill="旋风阵")
```

- 缺省参数

```
#  定义
def attack(weapon:String="兼光之巴", skill:String="旋风阵") :String = weapon+"-"+skill
#  调用
attack(skill="宿蛾之月")
```

- 递归函数

```
def travel(times:Int):Int = {
	if (times == 0)
		0
	else
		travel(times-1)
}
```

- 柯里化函数

```
#  定义
def attack(weapon:String)(skill:String) = weapon+"-"+skill
#  调用
attack("兼光之巴")("宿蛾之月")
```

- 传名参数

```
def travel(times:()=>Int) =
    if(times() > 0)
        print("可以穿越")
travel(()=>1)
```

#  组合和继承

- 抽象类

```
abstract class Weapon {
	def skills: Array[String]
	val count = skills.length
}
```

- 扩展类

```
#  定义
class Sword(s: Array[String]) extends Weapon {
	def skills: Array[String] = s
}
#  调用
val s = new Sword(Array("宿蛾之月","旋风阵"))
s.skills
s.count
```

- 参数化成员变量

```
#  定义
class Sword(val skills: Array[String]) extends Weapon {}
#  调用
val s = new Sword(Array("红龙破"))
s.skills
s.count
```

- 修饰参数化成员变量

```
#  定义
class Pearl {
	val color = "colorless"
}
class RedPearl (
	override val color: String,
	private val master: String
) extends Pearl
val rp = new RedPearl("red","诸叶")
#  调用
rp.color
rp.master // 不能访问
```

- 多态和动态绑定

```
#  定义
abstract class Weapon {
	def create() {
		println("制造武器")
	}
}
class Sword extends Weapon {
	override def create() {
		println("制造刀")
    }
}
class Spear extends Weapon
#  调用
val s = new Sword
s.create
val s = new Spear
s.create
```

- final 修饰类成员

```
abstract class Weapon {
	final def create() {
		println("制造武器")
	}
}
```

- final 修饰类

```
final abstract class Weapon {
	def create() {
		println("制造武器")
	}
}
```

#  Trait

- 定义 trait

```
trait attack {
    def skill() {
    	println("技能")
    }
}
```

- 类混合 trait

```
#  定义
trait attack {
    def skill() {
    	println("苍龙破")
    }
}
class Weapon {}
class Sword extends Weapon with attack{
    override def toString = "菊十文字"
}
#  调用
val s = new Sword
s.skill
```

#  包

- package

```
package backpack {
    package study {
		class Student {
        	var hb = new HistoryBook
    	}
    	class HistoryBook
    }
    class Bicycle {
    	val s = new study.Student
    }
    class Classmates {
    	class Classmate {
        	def addBicycle() {new Bicycle}
    	}
    }
}
```

- import

```
package backpack
abstract class Pearl(
	val name: String,
	val color:String
)
object Pearls{
    object RedPearl extends Pearl("RedPearl","red")
    object SliverPearl extends Pearl("SliverPearl","sliver")
    object GoldPearl extends Pearl("GoldPearl","gold")
    val all = List(RedPearl,SliverPearl,GoldPearl)
}
// 导入Pearl对象
import backpack.Pear
// 导入backpack的所有成员
import backpack._
// 导入backpack中Pearl对象的所有成员
import backpack.Pearl._
// 隐藏Pearl对象中的GoldPearl
import backpack.Pearl.{GoldPearl}
// 重命名对象
import backpack.Pearl.{GoldPearl => YellowPearl}
// 重命名包
import backpack.{Pearl => P}
```

#  访问修饰符

- private

```
class Modern {
    class Home {
    	private def travel(){
        	println("穿越")
    	}
    	class Tree {
        	travel() // 可以访问
    	}
    }
    (new Home).travel() // 不能访问
}
```

- protected

```
class Ancient{
    class Tree {
    	protected def travel() {
        	println("穿越")
    	}
    }
    class Well extends Tree{
   		travel() // 可以访问
    }
    class Foreast{
    	(new Tree).travel() // 不能访问
    }
}
```
