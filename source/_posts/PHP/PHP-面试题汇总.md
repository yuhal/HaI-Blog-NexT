---
title: PHP-面试题汇总
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-0c9f831fb5cbab53.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

### 1. PHP执行的时候有如下执行过程：Scanning(Lexing) - Compilation - Execution - Parsing，其含义分别为（C）
A、将PHP代码转换为语言片段(Tokens)、将Tokens转换成简单而有意义的表达式、顺次执行Opcodes、将表达式编译成Opocdes
B、将PHP代码转换为语言片段(Tokens)、将表达式编译成Opocdes、顺次执行Opcodes、将Tokens转换成简单而有意义的表达式
C、将PHP代码转换为语言片段(Tokens)、将Tokens转换成简单而有意义的表达式、将表达式编译成Opocdes、顺次执行Opcodes
D、将PHP代码转换为语言片段(Tokens)、将表达式编译成Opocdes、将Tokens转换成简单而有意义的表达式、顺次执行Opcodes

### 2.不是php魔术常量的是（B）
A、\__TRAIT__
B、\__CALL__
C、\__CLASS__
D、\__FUNCTION__

### 3.php选项/信息函数作用错误的是（D）
A、phpinfo() 输出关于 PHP 配置的信息
B、php_sapi_name() 返回 web 服务器和 PHP 之间的接口类型
C、ini_set() 为一个配置选项设置值
D、ini_get() 获取所有配置选项

### 4.下列代码的输出是 （A）
```
$father=" mother"; 
$mother="son"; 
echo $$father;
```
A、son
B、mother
C、motherson
D、error

### 5.下列对shell 变量FRUIT 操作，正确的是（C）
A、为变量赋值：```$FRUIT=apple```
B、显示变量的值：```fruit=apple```
C、显示变量的值：```echo $FRUIT```
D、判断变量是否有值：```[ -f ―$FRUIT ]```

### 6.以下不是线性表是（B）
A、数组
B、二叉树
C、队列
D、栈

### 7.以下哪个函数不是PHP的文件指针操作（C）
A、ftell()
B、fseek()
C、file()
D、feof()

### 8.关于线程的，说法错误的是（C）
A、线程是进程的一个实体,是CPU调度和分派的基本单位
B、它是比进程更小的能独立运行的基本单位
C、线程和进程一样拥有系统资源
D、线程自己基本上不拥有系统资源

### 9.GoAccess虽然很强大但是他不能做以下哪项工作（C）
A、生成统计数据带宽统计
B、可生成HTML报告
C、可发送HTTP请求
D、各HTTP状态码统计

### 10.PHP的三个模块不包括哪个（D）
A、内核
B、zend引擎
C、扩展层
D、解析层

### 11.CSRF攻击描述错误的是（A）
A、CSRF需要有JavaScript代码
B、CSRF攻击恶意代码位于第三方站点上
C、过滤用户的输入可以防止恶意代码注入到某个站点，但是它无阻止法恶意代码在第三方站点上运行
D、CSRF符合同源策略

### 12.关于PHP数组在C语言中是哪种存储结构（B）
A、单链表
B、双链表
C、循环链表
D、二叉树

### 13.关于组合模式，说法错误的是（B）
A、它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以向处理简单元素一样来处理复杂元素，从而使得客户程序与复杂元素的内部结构解耦
B、定义了一种一对多的依赖关系，让多个观察者对象同时 监听某一个主题对象。这个主题对象在状态 发生变化时，会通知所有观察者对象，使他们能够自动更新自己
C、树枝和叶子实现统一接口，树枝内部组合该接口
D、将对象组合成树形结构以表示"部分-整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性

### 14.数据结构的储存方式描述错误的是（D）
A、顺序存储用数据元素在存储器中的相对位置来表示数据元素之间的逻辑结构
B、链式存储在每一个数据元素中增加一个存放另一个元素地址的指针，用该指针来表示数据元素之间的逻辑结构
C、顺序结构数据元素存放的地址是连续的
D、数据算法的实现依赖于所采用的逻辑结构

### 15.下面Http协议请求方式中不包括（D）
A、OPTIONS
B、HEAD
C、DELETE
D、SET

### 16.下边不是php的伪类型的是（D）
A、mixed
B、void
C、array|object
D、callable
E、以上都是

### 17.文本文件和二进制文件的存取，错误的是（C）
A、用记事本打开二进制文件时, 出现乱码是很必然了
B、二进制文件还是文本文件, 在存储时都是一连串的0和1
C、打开方式是一样的
D、二进制文件最小单位则是位

### 18.不是PHP加密函数的是？（B）
A、openssl_encrypt
B、json_encode
C、mcrypt_encrypt
D、md5

### 19.什么是PHP的多维数组（B）
A、PHP的值是多种数据类型
B、PHP的值也是数组类型
C、PHP的索引有数字和字母
D、以上都是

### 20.下面哪一个正则表达式用来验证电子邮件（如： zhang.san_123@scse.com.cn ）的格式最正确（C）
A、[_\.0-9a-z]@([0-9a-z]+\.)+[0-9a-z\.-]{2,6}
B、[_\.0~9a~z-]*@([0~9a~z-]+\.)+[0~9a~z\.]+
C、[_\.0-9a-z-]+@([0-9a-z-]+\.)+[0-9a-z\.]+
D、[_\.0~9a~z-]+@([0~9a~z-]+\.)+[0~9a~z]{2,6}

### 21.（C）是一种客户端脚本语言，它采用解释方式在计算机上执行。
A、Python
B、Java
C、PHP
D、JavaScript

### 22.以下关于结构型模式说法错误的是（B）
A、结构型模式可以在不破坏类封装性的基础上，实现新的功能
B、结构型模式主要用于创建一组对象
C、结构型模式可以创建一组类的统一访问接口
D、结构型模式可以在不破坏类封装性的基础上，使得类可以同不曾估计到的系统进行交互

### 23.用PHP打印出前一天的时间格式是2006-5-10 22:21:21（AB）
A、echo date('Y-m-d H:i:s', strtotime('-1 days'));
B、echo date('Y-m-d H:i:s', strtotime('-1 day'));
C、echo date('Y-m-d H:i:s', strttime('-1 days'));
D、echo date('Y-n-d H:i:s', strtotime('-1 days'));

### 24.下面关于数组和数据结构的说法错误的是（D）
A、栈 是 后进先出的线性表，可以随意写入和读取数据
B、队列 是先进先出的线性表，只允许后端插入，前端进行删除操作
C、php中可以用 array_push 入栈,arrar_pop 实现出栈
D、php中用array_push入列，array_shift 出列

### 25.以下关于引用说法错误的是（B）
A、引用不是C的指针
B、引用不允许用两个变量来指向同一个内容
C、用引用可以传递变量
D、可以将一个变量通过引用传递给函数，这样该函数就可以修改其参数的值。

### 26.数组的遍历方式，下列错误的是（C）
A、foreach
B、each
C、for
D、list

### 27.PHP运行模式哪个不适合做http服务（D）
A、cgi模式
B、fastcgi模式
C、isapi模式
D、cli模式

### 28.在 Linux 中，文件（A）用于解析主机域名。
A、etc/hosts 
B、etc/host.conf 
C、etc/hostname
D、etc/bind 

### 29. 字符串"\r","\n","\t","\x20"分别代表什么
- "\r"代表的含义是： 在Linux、unix 中表示返回到当行的最开始位置，在Mac OS 中表示换行且 返回到下一行的最开始位置，相当于Windows 里的 \n 的效果。 
- "\n"代表的含义是： 在Windows 中表示换行且回到下一行的最开始位置。相当于Mac OS 里的 \r  的效果，在Linux、unix 中只表示换行，但不会回到下一行的开始位置。 
- "\t"所代表的含义是： 键盘上的"TAB"键，跳格（移至下一列）。 
- "\x20"所代表的含义是：是32在ASCII表中16进制的表示。

### 30. 以下语句输出的结果是什么
```
$a = 3;
echo "$a",'$a',"\\\$a","${a}","$a"."$a","$a"+"$a";
//得到的结果是： 3$a\$a3336
```

### 31. 以下语句输出的结果是什么
```
setcookie("a","value");
print $_COOKIE['a'];
//得到的结果是：value(若只是这两段编码运行，则会提示PHP Notice: Undefined index: a)
```

### 32. php中将当前页面重定向到另一个页面怎么写？
```
header("Location:www.xxx.php");
```

### 33. 什么是魔术引号(magic_quotes_gpc)? 
魔术引号（Magic Quotes）是一个自动将进入 PHP 脚本的数据进行转义的 过程。提示：最好在编码时不要转义而在运行时根据需要而转义。

### 34. 在类的方法中，如何调用其父类的同名方法？ 
```
parent::方法名
```

### 35. php中如何取得get，post参数，和上传的文件
```
$_GET,$_POST,$_FILES
```

### 36. 如何取得客户端的ip(要求取得一个int)
```
$_SERVER["REMOTE_ADDR"];//ip2long进行转换
```

### 37 .include和require的区别
require:出现错误后直接终止退出，程序不再执行 
include:包含一个不存在的文件，会提示警告程序会继续执行

### 38. extends的作用是什么 
类的继承

### 39.@test()和&test()的区别
@test()的作用是屏蔽test()方法中警告的作用 
&test()引用test()方法

### 40. array+array与array_merge()的区别 
二者之间的区别是： 
⑴键名为数字时，array_merge()不会覆盖掉原来的值，但＋合并数组则会
把最先出现的值作为最终结果返回，而把后面的数组拥有相同键名的那些值"抛弃"掉（不是覆盖） 
```
$arr1 = [1,2,3];
$arr2 = [4,5,6];
$arr3 = $arr1 + $arr2;
print_r($arr3);
//输出
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
)
```
⑵键名为字符时，＋仍然把最先出现的值作为最终结果返回，而把后面的数
组拥有相同键名的那些值"抛弃"掉，但array_merge()此时会覆盖掉前面相同键名的值
```
$arr1 = [1,2,3];
$arr2 = [4,5,6];
$arr3 = array_merge($arr1,$arr2);
print_r($arr3);
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
    [3] => 4
    [4] => 5
    [5] => 6
)
```
### 41. 请列举最少3个php对象的魔术方法和说明它们的用途 
__construct() 构造方法
__destruct() 析构方法
__get() 控制私有的、受保护的、未定义的成员属性的访问 
__set() 对私有的、受保护的、未定义的成员属性进行赋值控制 
__isset() 对私有的、受保护的、未定义成员属性进行isset和empty的判断控制 

### 42. 什么是fpm 
FastCGI Process Manager：FastCGI进程管理器

### 43. 描述一下php开发中常见的几种攻击以及解决方案 
- SQL注入： 
解决这个问题的办法是，将 PHP 的内置 mysql_real_escape_string() 函
数用作任何用户输入的包装器。这个函数对字符串中的字符进行转义，
使字符串不可能传递撇号等特殊字符并让 MySQL 根据特殊字符进行操作。 
进行数据库操作的时候使用预处理语句。
- XSS跨站点脚本攻击：
strip_tags() 函数，这个函数可以清除任何包围在 HTML 标记中的内容 
或者使用htmlspecialchars() 函数。
- CSRF跨站点请求伪造：
验证 HTTP Referer 字段；在请求地址中添加 token 并验证；在 HTTP 头中自定义属性并验证。

### 44. echo intval(0.58*100) 输出的结果是57，试分析这是为什么？ 
原因就是浮点数精度的问题。简单的十进制分数如同 0.1 或 0.7 不能在不丢失一点点精度的情况下转换为内部二进制的格式。
这就会造成混乱的结果：例如，floor((0.1+0.7) *10) 通常会返回 7 而不是预期中的 8，因为该结果内部的表示其实是类似  7.9999999999…...
这和一个事实有关，那就是不可能精确的用有限位数表达某些十进制分数。
例如，十进制的 1/3 变成了 0.3333333…...
所以永远不 要相信浮点数结果精确到了最后一位，也永远不要比较两个浮点数是否相等 。如果确实需要更高的精度，应该使用任意精度数学函数或者 gmp 函数（GMP是一个开源的数学运算库，它可以用于任意精度的数学运算，包括有符号整数、有理数和浮点数。它本身并没有精度限制，只取决于机器的硬件情况。）

### 45.请用最简单的语言告诉我PHP是什么？
是一种用来开发动态网站的服务器脚本语言。

### 46.什么是MVC？
MVC由Model（模型）, View（视图）和Controller（控制器）组成，PHP MVC可以更高效地管理好3个不同层的PHP代码。
Model：数据信息存取层。
View：view层负责将应用的数据以特定的方式展现在界面上。
Controller：通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

### 47.在页面中引用CSS有几种方式？
引用外部CSS文件
内部定义Style样式
内联样式

### 48.PHP支持多继承吗？
在PHP的面向对象中，接口可以继承接口。PHP类只能继承一个父类（单继承），但是接口可以实现多继承，可以继承一个或者多个接口。当然接口的继承也是和类的继承一样使用extends关键字，要多个继承的话只要用逗号把继承的接口隔开即可。
```
class testA 
{
	function speaking($fans);
}
class testB 
{
	function dancing($name);
}
class testC extends testB,testA
{
	function singing($nickname);
}
//类testC不可以继承类testB和类testA，实例化类testC直接会报语法错误
interface testA
{
	function speaking($viewer);
}
interface testB
{
	function dancing($name);
}
interface testC extends testA,testB
{
	function singing($nickname);
}
class testD implements testC
{
	function speaking($viewer){
		echo $viewer."正在讲话！";
		echo "\n";
	}
	function dancing($name){
		echo $name."正在跳舞！";
		echo "\n";
	}
	function singing($nickname){
		echo $nickname."正在唱歌！";
		echo "\n";
	}
}
$testD = new testD(); 
$testD->speaking('粉丝'); 
$testD->dancing('助跳'); 
$testD->singing("周杰伦");
//接口testC可以继承接口testB和接口testA
```

### 49.echo(),print(),print_r()的区别
echo是PHP语句, print和print_r是函数,语句没有返回值,函数可以有返回值(即便没有用)  
print（）    只能打印出简单类型变量的值(如int,string)  
print_r（） 可以打印出复杂类型变量的值(如数组,对象)  
echo     输出一个或者多个字符串

### 50.请问GET和POST方法有什么区别？
get是发送请求HTTP协议通过url参数传递进行接收;
post是实体数据,可以通过表单提交大量信息.

### 51.PHP中获取图像尺寸大小的方法是什么？
getimagesize () 获取图片的尺寸
```
$size = getimagesize('1.jpg');
print_r($size);
//输出
Array
(
    [0] => 75
    [1] => 75
    [2] => 3
    [3] => width="75" height="75"
    [bits] => 8
    [mime] => image/png
)
```
Imagesx () 获取图片的宽度
Imagesy () 获取图片的高度
```
$size = getimagesize('1.png');
$img = imagecreatefrompng('1.png');
echo imagesx($img).PHP_EOL;
echo imagesx($img);
//输出
200
100
```

### 52.PHP中的PEAR是什么？
PEAR 是"PHP Extension and Application Repository"的缩写，即PHP扩展和应用仓库。
PEAR 将PHP程序开发过程中常用的功能编写成类库，涵盖了页面呈现、数据库访问、文件操作、数据结构、缓存操作、网络协议、WebService 等许多方面，用户可以通过下载这些类库并适当的作一些定制以实现自己需要的功能。避免重复发明"车轮"。PEAR 的出现大大提高了PHP 程序的开发效率和开发质量。

### 53.如何用PHP和MySQL上传视频？
可以在数据库中存放视频的地址，而不需要将真正的视频数据存在数据库中。将视频数据存放在服务器的指定文件夹下，上传的默认大小是2MB，但是我们也可以在php.ini文件中修改max_file_size选项来改变。

### 54.PHP中的错误类型有哪些？
PHP中遇到的错误类型大致有3类。
- 提示：这都是一些非常正常的信息，而非重大的错误，有些甚至不会展示给用户。比如访问不存在的变量。
- 警告：这是有点严重的错误，将会把警告信息展示给用户，但不会影响代码的输出，比如包含一些不存在的文件。
- 错误：这是真正的严重错误，比如访问不存在的PHP类。

### 55.如何在PHP中定义常量？
PHP中使用Define () 来定义常量。
define('GREETING', 'Hello World');

### 56.如何不使用submit按钮来提交表单？
可以用超链接来提交：
<a href="javascript: document.myform.submit();">Submit Me</a>

### 57.表单中 get与post提交方法的区别?
get是发送请求HTTP协议通过url参数传递进行接收;
post是实体数据,可以通过表单提交大量信息.

### 58.session与cookie的区别?
session:储存用户访问的全局唯一变量,存储在服务器上的php指定的目录中的（session_dir）的位置进行的存放
cookie:用来存储连续访问一个页面时所使用，是存储在客户端，对于Cookie来说是存储在用户本地，两者都可通过时间来设置时间长短

### 59.数据库中的事务是什么?
事务（transaction）是作为一个单元的一组有序的数据库操作。
组中的所有操作都成功，则认为事务成功，最终进行提交；
即使一个操作失败，则认为事物失败，最终进行回滚。

### 60、用PHP打印出前一天的时间格式是2006-5-10 22:21:21
```
echo date('Y-m-d H:i:s', strtotime('-1 day'));
```

### 61、echo(),print(),print_r()的区别
echo是PHP语句, print和print_r是函数,语句没有返回值,函数可以有返回值(即便没有用)  
print（）    只能打印出简单类型变量的值(如int,string)  
print_r（） 可以打印出复杂类型变量的值(如数组,对象)  
echo     输出一个或者多个字符串

### 62、能够使HTML和PHP分离开使用的模板
- Smarty：PHP的一个引擎模板，可以进行更好的进行逻辑与显示的分离，即我们常说的MVC，这个引擎的作用就是将C分离出来。其中的MVC分别指的是M模型(moder)，V视图(view)，C控制器(controller)。简单来说就是将html代码与php代码分离开，使速度更快，减少代码量,方便程序的修改与维护。

- Dwoo：一个PHP5模板引擎。兼容Smarty模板，它在Smarty语法的基础上完全进行重写。支持通过插件扩展其功能。

- TinyButStrong：这个模板引擎确实很小，只有一个文件和一个PHP类！但它有一些显著特性。它可以与MySQL、SQLite和PostgreSQL结合使用，并且它不局限于与HTML文件结合使用：它可以与XML、RTF和WML文件一起使用，也可以与OpenOffice和Microsoft Office的文档文件一起使用。

- Template Lite：Template Lite是一个非常快而且很小HTML模板引擎。该引擎支持Smarty模板引擎所具有的大部分功能和过滤器。

- Savant：是一个强大但轻量级的面向对象PHP模板引擎。不象其模板系统，Savant默认没有把模板编译成PHP，而是使用PHP本身来作为它的模板语言所以你不需要学习一套新的标记系统。Savant有一个面向对象的模板插件系统和输出过滤器，可以让你快速为它新增新的行为。

- phemplate：是一个简单而且快速的PHP模板引擎。它允许在模板中加入变量和一些动态程序块包括循环。该模板引擎能够可以实现表现与逻辑相分离，也就是说你可以从PHP脚本中抽出所有HTML内容。设计人员可以随意更改HTML而不用担心弄乱你的PHP脚本。

- XTemplate：是一个适用于PHP的模板引擎。它允许把HTML代码与PHP代码分开存储。XTemplate包含了许多有用的功能比如嵌套的程序块，各种类型的插值变量。其代码非常简洁并且是最优化的。

### 63、使用哪些工具进行版本控制?
svn，优点：各平台（windows、unix、mac）都能使用。

### 64、如何实现字符串翻转?
echo strrev($a);

### 65、优化MYSQL数据库的方法。(4分，多写多得)
①、选取最适用的字段属性,尽可能减少定义字段长度,尽量把字段设置NOT NULL,例如'省份,性别',最好设置为ENUM（枚举类型）
②、使用连接（JOIN）来代替子查询:
③、使用联合(UNION)来代替手动创建的临时表
④、事务处理，保证数据完整性,例如添加和修改同时,两者成立则都执行,一者失败都失败
⑥、使用外键，优化表结构：
**On Delete属性：**
- 当取值为No Action或者Restrict时，则当在外键的表中删除对应记录时，首先检查该记录是否有对应外键，如果有则不删除。
- 当取值为Cascade时，则当在外键的表中删除对应记录时，首先检查该记录是否有对应外键，如果有则删除。
- 当取值为Set Null时，则当在即外键的表中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null（不过这就要求该外键允许取null）。

**On Update属性：**
- 当取值为No Action或者Restrict时，则当在外键的表中更新对应记录时，首先检查该记录是否有对应外键，如果有则不更新。
- 当取值为Cascade时，则当在外键的表中更新对应记录时，首先检查该记录是否有对应外键，如果有则更新。
- 当取值为Set Null时，则当在即外键的表中更新对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null（不过这就要求该外键允许取null）。

⑦、建立索引:普通索引/唯一索引/主键/联合索引
⑧、优化查询语句
a.最好在相同字段进行比较操作,在建立好的索引字段上尽量减少函数操作
```
// 例子1:
SELECT * FROM order WHERE YEAR(orderDate)<2008;(慢)
SELECT * FROM order WHERE orderDate<"2008-01-01";(快)
// 例子2:
SELECT * FROM order WHERE addtime/7<24;(慢)
SELECT * FROM order WHERE addtime<24*7;(快)
// 例子3:
SELECT * FROM order WHERE title like "%good%";(慢)
SELECT * FROM order WHERE title>="good" and name<"good";(快)
```

### 66、请用最简单的语言告诉我PHP是什么？
是一种用来开发动态网站的服务器脚本语言。

### 67、MYSQL取得当前时间的函数是?，格式化日期的函数是
```
now(),date()
```

### 68、实现中文字串截取无乱码的方法。
使用mbstring扩展库的mb_substr截取就不会出现乱码了。
```
// mb_substr是按字来切分字符，
echo mb_substr('PHP是最好的语言^_^', 0, 7, 'utf-8');
// mb_strcut是按字节来切分字符
echo mb_strcut('PHP是最好的语言^_^', 0, 10, 'utf-8');
```
### 69、您是否用过版本控制软件? 如果有您用的版本控制软件的名字是?
是,git

### 70、您是否用过模板引擎? 如果有您用的模板引擎的名字是?
用过,smarty

### 71、请简单阐述您最得意的开发之作
礼业社交小程序(集购物支付、信息查询、微博功能、积分系统、社交功能的B2B2B平台)

### 72、对于大流量的网站,您采用什么样的方法来解决访问量问题?
确认服务器硬件是否足够支持当前的流量,数据库读写分离,优化数据表,
程序功能规则,禁止外部的盗链,控制大文件的下载,使用不同主机分流主要流量

### 73、用PHP写出显示客户端IP与服务器IP的代码
```
// 打印客户端IP（不能在CLI模式下执行）:
// echo $_SERVER['REMOTE_ADDR'].PHP_EOL; 
// 或者: 
echo getenv('REMOTE_ADDR').PHP_EOL;
// 打印服务器IP:
echo gethostbyname("www.yuhal.com").PHP_EOL;
```

### 74、语句include和require的区别是什么?为避免多次包含同一文件，可用什么语句代替它们? 
require:出现错误后直接终止退出，程序不再执行 
include:包含一个不存在的文件，会提示警告程序会继续执行
require_once或者include_once

### 75、如何修改SESSION的生存时间.
```
// 方法1:
将php.ini中的session.gc_maxlifetime设置为9999重启apache或/nginx
// 方法2:
$savePath = "./session_save_dir/";
$lifeTime = 小时 * 秒;
session_save_path($savePath);
session_set_cookie_params($lifeTime);
session_start();
// 方法3:
setcookie() and session_set_cookie_params($lifeTime);
```
### 76、有一个网页地址, 比如58同城首页: https://sh.58.com,如何得到它的内容?
```
// 方法1(对于PHP5及更高版本):
$readcontents = fopen("https://sh.58.com", "rb");
$contents = stream_get_contents($readcontents);
fclose($readcontents);
echo $contents;
// 方法2:
echo file_get_contents("https://sh.58.com");
```
### 77、在HTTP 1.0中，状态码401的含义是是什么;如果返回"找不到文件"的提示，则可用 header 函数，其语句为？;
状态401代表未被授权,header("Location:www.xxx.php");

### 78、在PHP中，heredoc的语法是什么?
heredoc的语法是用"<<<"加上自己定义成对的标签，在标签范围內的文字视为一个字符串
```
$str = <<< EOT
   my name is HaI!
EOT;
```
### 79、请描述尽可能多的HTTP状态码及含义
- 200 请求成功
- 301 资源（网页等）被永久转移到其它URL
- 302 资源（网页等）被临时转移，客户端继续使用原有URI
- 400 客户端请求的语法错误，服务器无法理解
- 400 未授权，请求要求用户的身份认证
- 404 请求的资源（网页等）不存在
- 500 内部服务器错误

### 80、什么是MVC？
MVC由Model（模型）, View（视图）和Controller（控制器）组成，PHP MVC可以更高效地管理好3个不同层的PHP代码。
Model：数据信息存取层。
View：view层负责将应用的数据以特定的方式展现在界面上。
Controller：通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

### 81、写出发贴数最多的十个人名字的SQL，利用下表：
``` 
CREATE TABLE `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `username` varchar(255) NOT NULL COMMENT '用户名称',
  `posts` varchar(255) DEFAULT '0' COMMENT '发帖数量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
SELECT username FROM members ORDER BY posts DESC limit 0,10;
```
### 82. 请说明php中传值与传引用的区别。什么时候传值什么时候传引用?
按值传递：函数内对值的任何改变在函数外部都会被忽略。
引用传递：函数内对值的任何改变在函数外部也能反映出这些修改。
应用场景：按值传递时，php必须复制值，而按引用传递则不需要复制值，故引用传递一般用于大字符串或对象。

### 83. 在PHP中error_reporting这个函数有什么作用? 
设置错误级别与错误信息回报

### 84. 请写一个函数验证电子邮件的格式是否正确 
```
function checkEmail($email){
	$pregEmail = "/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/";
	return preg_match($pregEmail,$email);  
}
print_r(checkEmail('AA1573+6736889@1ss63.com')).PHP_EOL;
```

### 85. http和https有什么区别?
- http是超文本传输协议，信息是明文传输，https是具有安全性的ssl加密传输协议
- http和https使用的是完全不一样的连接方式，端口也不一样，前者默认是80端口，后者则是443端口
- http是无状态的协议，而https是由ssl+http构建的可进行加密传输、身份认证的网络协议。
- https比http慢，因为http在TCP/IP基础上传输的，TCP只需要三次握手。而https需要在TCP/IP基础上再加TLS的四次握手。所以一定慢。
- https可以进行加密传输，相对而言比http安全很多，是现在网站的大趋势
- https解决的三大风险：窃听风险、篡改风险、冒充风险。会话密钥解决了盗听风险，数字签名解决了篡改风险，数字证书（CA认证）解决了冒充风险

### 86、JS表单弹出对话框函数是?获得输入焦点函数是? 
弹出对话框: alert(),prompt(),confirm()
获得输入焦点 focus()

### 87、JS的转向函数是?怎么引入一个外部JS文件?
window.location.href
<script type="text/javascript"src="JS文件路径"></script>

### 88、foo()和@foo()之间有什么区别?
@foo()控制错误输出
foo()是调用该函数

### 89、如何声明一个名为"myclass"的没有方法和属性的类? 
class myclass{}

### 90、如何实例化一个名为"myclass"的对象?
new myclass()

### 91、你如何访问和设置一个类的属性? 
```
class myclass
{
	public $test;
}
$object = new myclass();
$newstr = $object->test;
$object->test = "info";
echo $object->test.PHP_EOL;
```

### 92、mysql_fetch_row() 和mysql_fetch_array之间有什么区别? 
mysql_fetch_row是从结果集取出一行数组,作为枚举
mysql_fetch_array是从结果集取出一行数组作为关联数组,或数字数组,两者兼得

### 93、GD库是做什么用的? 
GD库提供了一系列用来处理图片的API使用，GD库可以处理图片或者生成图片。 
在网站上GD库通常用来生成缩略图或者用来对图片加水印或者对网站数据生成报表。

### 94、指出一些在PHP输入一段HTML代码的办法。
echo "<span>hello</span>";

### 95、下面哪个函数可以打开一个文件，以对文件进行读和写操作? C
A.fget() 	  
B.file_open()		
C.fopen() 	
D.open_file()  

### 96、下面哪个选项没有将 john 添加到users 数组中?  BD
A. \$users[] = 'john';
B. array_add(\$users,'john');
C. array_push(\$users,'john');
D. \$users ||= 'john'; 

### 97、下面的程序的输出结果? 
```
<?php
$num = 10;
function multiply(){
	$num = $num * 10;
}
multiply();
echo $num;
?>
//输出:10
```

### 98、使用php写一段简单查询，查出所有姓名为"John"的内容并打印出来 
表名User
Name Tel Content Date
Marry 13333663366 CET4 2006-10-11
John 13612312331 CET6 2006-10-15
Peter 021-55665566 CET3 2006-10-15
请根据上面的题目完成代码：
```
// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
$sql = "SELECT * FROM tbl_user WHERE name='John'";
$result = $conn->query($sql);
// 输出数据
while($row = $result->fetch_assoc()) {
    echo "name: " . $row["name"].PHP_EOL."tel: " . $row["tel"].PHP_EOL."content: " . $row["content"].PHP_EOL."date: " . $row["date"].PHP_EOL;
}
``` 

### 99、浏览器访问网页过程中发生了什么？
- 第一步，解析域名，找到主机IP
- 第二步，浏览器与网站建立TCP连接
- 第三步，浏览器发起GET请求 
- 第四步，显示页面或返回其他

### 100、写出 SQL语句的格式 : 插入 ，更新 ，删除 
表名User
Name Tel Content Date
Marry 13333663366 CET6 2006-10-11
John 13612312331 CET4 2006-10-15
Peter 021-55665566 CET4 2006-10-15
(a) 有一新记录(Pack 13254748547 CET6 2007-05-06)请用SQL语句新增至表中
(b) 请用sql语句把John的时间更新成为当前系统时间
(c) 请写出删除名为Peter的全部记录
```
a. mysql_query("INSERT INTO `user` (name,tel,content,date) VALUES 
('Pack','13254748547','CET6','2007-05-06')")
b. $nowDate = date("Ymd");
mysql_query("UPDATE `user`SET date='".$nowDate."'WHERE name='John'");
c.mysql_query("DELETE FROM `user` WHERE name='Peter'");
```

### 101、请写出数据类型(int char varchar datetime text)的意思; 请问varchar和char有什么区别
- int是数字类型
- char固定长度字符串
- varchar实际长度字符串
- datetime日期时间型
- text文本字符串
char的场地固定为创建表设置的长度，varchar为可变长度的字符

### 102、写出以下程序的输出结果 	
```
<?php
$b = 201;
$c = 40;
$a = $b>$c?4:5;
echo $a;
?>
//输出 4
```

### 103、检测一个变量是否有设置的函数是否?是否为空的函数是?
isset();
empty();

### 104、取得查询结果集总数的函数是?
mysql_num_rows();

### 105、$arr = array('james', 'tom', 'symfony'); 请打印出第一个元素的值 
echo $array[0];

### 106、请将数组的值用','号分隔并合并成字串输出
echo rtrim(implode(',',$array));

### 107、PHP二维数组去重
```
function assoc_unique($arr, $key) {
    $tmp_arr = array();
    foreach ($arr as $k => $v) {
        //搜索$v[$key]是否在$tmp_arr数组中存在，若存在返回true
        if (in_array($v[$key], $tmp_arr)) {
            unset($arr[$k]);
        } else {
            $tmp_arr[] = $v[$key];
        }
    }
    //sort函数对数组进行排序
    sort($arr); 
    return $arr;
}
$aa = array(
array('id' => 123, 'name' => '张三'),
array('id' => 123, 'name' => '李四'),
array('id' => 124, 'name' => '王五'),
array('id' => 125, 'name' => '赵六'),
array('id' => 126, 'name' => '赵六')
);
$key = 'id';
$arr = assoc_unique($aa, $key);
print_r($arr);
//输出
Array
(
    [0] => Array
        (
            [id] => 123
            [name] => 张三
        )

    [1] => Array
        (
            [id] => 124
            [name] => 王五
        )

    [2] => Array
        (
            [id] => 125
            [name] => 赵六
        )

    [3] => Array
        (
            [id] => 126
            [name] => 赵六
        )

)
```

### 108、\$a='abcdef'; 请取出$a的值并打印出第一个字母
```
echo $a{0}; 
//或
echo substr($a,0,1)
```

### 109、PHP可以和sql server/oracle等数据库连接吗?
当然可以

### 110、请写出PHP5权限控制修饰符
public(公共),private(私用),protected(继承)

### 111、请写出php5的构造函数和析构函数
__construct , __destruct

### 112、完成以下:
(一)创建新闻发布系统，表名为message有如下字段 
id 文章id
title 文章标题
content 文章内容
category_id 文章分类id
hits 点击量
```
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `title` char(30) NOT NULL COMMENT '文章标题',
  `content` varchar(255) NOT NULL COMMENT '文章内容',
  `category_id` int(11) NOT NULL COMMENT '文章分类id',
  `hits` int(11) NOT NULL COMMENT '点击量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8
```

(二)同样上述新闻发布系统：表comment记录用户回复内容，字段如下 
comment_id 回复id
id 文章id，关联message表中的id
comment_content 回复内容
```
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL COMMENT '回复id',
  `id` int(11) DEFAULT NULL COMMENT '文章id，关联message表中的id',
  `comment_content` varchar(255) DEFAULT NULL COMMENT '回复内容',
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
现通过查询数据库需要得到以下格式的文章标题列表,并按照回复数量排序，回复最高的排在最前面
文章id 文章标题 点击量 回复数量
用一个SQL语句完成上述查询，如果文章没有回复则回复数量显示为0
```
SELECT message.id id,message.title title,IF(message.`hits` IS NULL,0,message.`hits`) hits,IF(comment.`id` is NULL,0,count(*))number FROM message LEFT JOIN comment ON message.id=comment.id GROUP BY message.`id`;
```

(三)上述内容管理系统，表category保存分类信息，字段如下 
category_id 分类id
categroy_name 分类名称
```
CREATE TABLE `category` (
  `category_id` int(4) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类id',
  `category_name` varchar(40) NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
用户输入文章时，通过选择下拉菜单选定文章分类
写出如何实现这个下拉菜单
```
$sql = "SELECT * FROM category";
$result = $conn->query($sql);
print("<select>");
while($row = $result->fetch_assoc()) {
    print("<option>".$row['category_name']."</option>");
}
print("</select>");
```

### 113. 写一个函数，尽可能高效的，从一个标准 url 里取出文件的扩展名
例如: https://yuhal.com/index.php?id=1 需要取出 php 或 .php
方案1:
```
function getExt($url){
   $arr = parse_url($url);
   $file = basename($arr['path']);
   $ext = explode(".",$file);
   return $ext[1];
}
```
方案2:
```
function getExt($url) {
    $url = basename($url);
    $pos1 = strpos($url,".");
    $pos2 = strpos($url,"?");
    if(strstr($url,"?")){
         return substr($url,$pos1 + 1,$pos2 - $pos1 - 1);
    } else {
      return substr($url,$pos1);
    }
}
```

### 114.写一个函数，算出两个文件的相对路径
```
//计算出 $b 相对于 $a 的相对路径
$a = '/a/b/c/d/e.php';
$b = '/a/b/12/34/c.php';
function getRelativePath($a, $b) {   
    $returnPath = array(dirname($b));   
    $arrA = explode('/', $a);   
    $arrB = explode('/', $returnPath[0]);   
    for ($n = 1, $len = count($arrB); $n < $len; $n++) {   
        if ($arrA[$n] != $arrB[$n]) {   
            break;   
        }    
    }   
    if ($len - $n > 0) {   
        $returnPath = array_merge($returnPath, array_fill(1, $len - $n, '..'));   
    }    
    $returnPath = array_merge($returnPath, array_slice($arrA,$n));   
    return implode('/', $returnPath);   
}   
echo getRelativePath($a, $b); 
```

### 115.写一个函数，能够遍历一个文件夹下的所有文件和子文件夹。
```
function my_scandir($dir){
 	$files = array();
 	if ( $handle = opendir($dir) ) {
        while ( ($file = readdir($handle)) !== false ) {
	        if ( $file != ".." && $file != "." ) {
		        if ( is_dir($dir . "/" . $file) ) {
		            $files[$file] = scandir($dir . "/" . $file);
		        }else {
	        		$files[] = $file;
	            }
	        }
        }
        closedir($handle);
        return $files;
 	}
}
```

### 116.简述论坛中无限分类的实现原理。
```
CREATE TABLE category(
	cat_id smallint unsigned not null auto_increment primary key comment'类别ID',
	cat_name VARCHAR(30)NOT NULL DEFAULT''COMMENT'类别名称',
	parent_id SMALLINT UNSIGNED NOT NULL DEFAULT 0 COMMENT'类别父ID'
)engine=MyISAM charset=utf8;

function tree($arr,$pid=0,$level=0){
    static $list = array();
    foreach ($arr as $v) {
        //如果是顶级分类，则将其存到$list中，并以此节点为根节点，遍历其子节点
        if ($v['parent_id'] == $pid) {
            $v['level'] = $level;
            $list[] = $v;
            tree($arr,$v['cat_id'],$level+1);
        }
    }
    return $list;
}
```

### 117.PEAR中的数据库连接字符串格式是?
```$dsn = pgsql://postgres:123@tcp+192.168.0.1:8848/testdb。```

### 118.写出一个正则表达式，过虑网页上的所有JS/VBS脚本(即把scrīpt标记及其内容都去掉):
```
$script = '123<script> alert(123) </script>';
$str = preg_replace("/<script>.*?<\/script>/i", "", $script);
print_r($str);
//输出
111
```

### 119.数组函数 arsort 的作用是?
对数组进行逆向排序并保持索引关系
```
$arr = [1,2,3,4];
arsort($arr);
print_r($arr);
//输出
Array
(
    [3] => 4
    [2] => 3
    [1] => 2
    [0] => 1
)
```

### 120.mysql存储引擎Innode和MyISAM的区别。
|   | Innode  | MyISAM  | 
| ------------ | ------------ |------------ |
| 事务处理方面 | 支持事务 | 不支持事务 |
| 锁 | 行级锁 | 表级锁 |
| 增删改查性能 | 大量的增删改 | 大量的查询 |
| 自增类型字段 | 可以和其他字段一起建立联合索引 | 必须包含只有该字段的索引 |

### 121. Yii 2 Framework的最新版本是什么？
最新版本的Yii 2是2.0.15，发布于2018年3月20日。

### 122. 在Yii2中如何获取当前URL？
```
//获取Yii框架中的当前url。
Yii::app()->request->getUrl()
```

### 123. Yii中“render”和“renderpartial”有什么区别？
render函数用于使用指定的布局渲染Yii中的视图，而renderpartial用于渲染，视图中不包含视图布局。
当必须通过AJAX更新页面的一部分时，基本上使用Renderpartial。
用法：
```
render('yourviewname');
renderpartial('yourviewpartial');
```
### 124. yii中的Active Record（AR）是什么？
Active Record提供了一个面向对象的接口，用于访问和操作存储在数据库中的数据。 Active Record类与数据库表相关联，Active Record实例对应于该表的一行，Active Record实例的属性表示该行中特定列的值。 可以访问Active Record属性并调用Active Record方法来访问和操作存储在数据库表中的数据，而不是编写原始SQL语句。

### 125.Yii CModel类是什么？
Yii CModel是提供数据模型对象所需的通用功能的基类。CModel定义了需要验证的数据模型的基本框架。Yii中的所有模型都扩展了CModel类。

### 126.类的属性可以序列化后保存到 session 中，从而以后可以恢复整个类，这要用到的函数是?
unserialize()

### 127.SQL中LEFT JOIN的含义是什么？
自然左外链接

### 128.根据下列表信息，查询各个学生姓名及对应的的各科总成绩。
```
CREATE TABLE `tbl_member` (
  `id` int(11) NOT NULL COMMENT '用户ID',
  `name` char(10) DEFAULT NULL COMMENT '用户名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='学生表'

CREATE TABLE `tbl_score` (
  `member_id` int(11) NOT NULL COMMENT '用户id',
  `subject` varchar(255) DEFAULT NULL COMMENT '学科',
  `score` int(11) DEFAULT NULL COMMENT '分数',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='分数表'

select * from tbl_member left join tbl_score on tbl_member.id=tbl_score.member_id
```

### 129.下面的程序的输出结果?
```
echo 8%(-2);
//输出 0
```

### 130.PHP7 和 PHP5 的区别，具体多了哪些新特性？
- 性能提升了两倍
- 结合比较运算符 (<=>)
- 标量类型声明
- 返回类型声明
- try...catch 增加多条件判断，更多 Error 错误可以进行异常处理

### 131.为什么 PHP7 比 PHP5 性能提升了？
- 变量存储字节减小，减少内存占用，提升变量操作速度
- 改善数组结构，数组元素和 hash 映射表被分配在同一块内存里，降低了内存占用、提升了 cpu 缓存命中率
- 改进了函数的调用机制，通过优化参数传递的环节，减少了一些指令，提高执行效率

### 132.laravel中服务提供者是什么？
服务提供者是所有 Laravel 应用程序引导启动的中心, Laravel 的核心服务器、注册服务容器绑定、事件监听、中间件、路由注册以及我们的应用程序都是由服务提供者引导启动的。

### 133.laravel中IoC 容器是什么？
IoC（Inversion of Control）译为 「控制反转」，也被叫做「依赖注入」(DI)。什么是「控制反转」？对象 A 功能依赖于对象 B，但是控制权由对象 A 来控制，控制权被颠倒，所以叫做「控制反转」，而「依赖注入」是实现 IoC 的方法，就是由 IoC 容器在运行期间，动态地将某种依赖关系注入到对象之中。
其作用简单来讲就是利用依赖关系注入的方式，把复杂的应用程序分解为互相合作的对象，从而降低解决问题的复杂度，实现应用程序代码的低耦合、高扩展。
Laravel 中的服务容器是用于管理类的依赖和执行依赖注入的工具。

### 134.laravel中Facades 是什么？
Facades（一种设计模式，通常翻译为外观模式）提供了一个"static"（静态）接口去访问注册到 IoC 容器中的类。提供了简单、易记的语法，而无需记住必须手动注入或配置的长长的类名。此外，由于对 PHP 动态方法的独特用法，也使测试起来非常容易。

### 135.laravel中Contract 是什么？
Contract（契约）是 laravel 定义框架提供的核心服务的接口。Contract 和 Facades 并没有本质意义上的区别，其作用就是使接口低耦合、更简单。

### 136.laravel中依赖注入的原理？
依赖注入原理其实就是利用类方法反射，取得参数类型，然后利用容器构造好实例。然后再使用回调函数调起。
注入对象构造函数不能有参数。否则会报错。Missing argument 1
依赖注入故然好，但它必须要由 Router 类调起，否则直接用 new方式是无法实现注入的。所以这就为什么只有 Controller 、Job 类才能用这个特性了。

### 137.laravel的生命周期以及简单描述下laravel路由
Laravel 的生命周期从pu访问入口开始，再从访问入口结束结束。路由由注册到启动来实现

### 138.Mysql中like查询字符串的索引使用区别
field like"str%"会使用索引，like"%str%"不使用索引

### 139.什么是 Composer， 工作原理是什么？
Composer 是 PHP 的一个依赖管理工具。工作原理就是将已开发好的扩展包从 packagist.org composer 仓库下载到我们的应用程序中，并声明依赖关系和版本控制。

### 140.composer autoload的原理
使用php自带的spl_autoload_register函数，注册处理__autoload的方法

### 141.Redis、Memecached 这两者有什么区别？
- Redis 支持更加丰富的数据存储类型，String、Hash、List、Set 和 Sorted Set。- - - 
-  Memcached 仅支持简单的 key-value 结构。-
- Memcached key-value存储比 Redis 采用 hash 结构来做 key-value 存储的内存利用率更高。
- Redis 提供了事务的功能，可以保证一系列命令的原子性
- Redis 支持数据的持久化，可以将内存中的数据保持在磁盘中
- Redis 只使用单核，而 Memcached 可以使用多核，所以平均每一个核上 Redis 在存储小数据时比 Memcached 性能更高。

### 142.Redis 如何实现持久化？
- RDB 持久化，将 redis 在内存中的的状态保存到硬盘中，相当于备份数据库状态。
- AOF 持久化（Append-Only-File），AOF 持久化是通过保存 Redis 服务器锁执行的写状态来记录数据库的。相当于备份数据库接收到的命令，所有被写入 AOF 的命令都是以 redis 的协议格式来保存的。

### 143.什么是索引，作用是什么？常见索引类型有那些？
索引是一种特殊的文件,它们包含着对数据表里所有记录的引用指针，相当于书本的目录。其作用就是加快数据的检索效率。常见索引类型有主键、唯一索引、联合索引、普通索引索引。

### 144.Mysql 建立索引的原则？
- 最左前缀原理
- 选择区分度高的列作为索引
- 尽量的扩展索引，不要新建索引

### 145.高并发如何处理？
- 使用缓存
- 优化数据库，提升数据库使用效率
- 负载均衡

### 146.写出以下程序的输出结果
```
$arr = [1,2,3,4];
foreach ($arr as $v) {
	echo $v.PHP_EOL;
	$v = 5;
}
print_r($arr);
//输出
1
2
3
4
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
    [3] => 4
)
```





