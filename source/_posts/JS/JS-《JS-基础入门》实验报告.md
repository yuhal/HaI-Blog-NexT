---
title: JS-《JS-基础入门》实验报告
categories: JS
---

![WechatIMG1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-bc898c03dbc5a707.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

![JavaScript 基础入门.png](https://upload-images.jianshu.io/upload_images/15325592-8fb1d86539936dc6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  Array 对象的常用方法

|  名称 | 说明  |
| ------------ | ------------ |
| concat()   |  用于连接两个或多个数组，并返回结果 |
|  join() |   将数组转换成字符串|
|pop()|删除并返回数组的最后一个元素|
|push() |向数组的末尾添加一个或更多元素，并返回新的长度|
|reverse()|颠倒数组的顺序|
|shift() |删除并返回数组的第一个元素|
|unshift() |向数组的开头添加一个或更多元素，并返回新的长度|
|slice()|从某个已有的数组返回选定的元素|
|splice() |删除或替换当前数组的某些项目|
|sort() |将数组进行排序|
|toString() |把数组转换为字符串，并返回结果|

#  String 对象的常用方法

|  名称 | 说明  |
| ------------ | ------------ |
|charAt() |获取指定位置处字符|
|charCodeAt() |获取指定位置处字符的 Unicode 编码|
|concat() |连接字符串，等效于 “+”，“+” 更常用
|slice() |提取字符串的片断，并在新的字符串中返回被提取的部分
|indexOf() |检索字符串
|toString() |返回字符串
|toLowerCase() |把字符串转换为小写
|toUpperCase() |把字符串转换为大写
|replace() |替换字符串中的某部分
|split() |把字符串分割为字符串数组

#  Date 对象方法

|  名称 | 说明  |
| ------------ | ------------ |
|Date()|返回当日的日期和时间（输出的是中国标准时间）|
|getDate()|从 Date 对象返回一个月中的某一天 (1 ~ 31)|
|getDay()|从 Date 对象返回一周中的某一天 (0 ~ 6)|
|getMonth()|从 Date 对象返回月份 (0 ~ 11)|
|getFullYear()|从 Date 对象以四位数字返回年份|
|getHours()|返回 Date 对象的小时 (0 ~ 23)|
|getMinutes()|返回 Date 对象的分钟 (0 ~ 59)|
|getSeconds()|返回 Date 对象的秒数 (0 ~ 59)|
|getMilliseconds()|返回 Date 对象的毫秒(0 ~ 999)|

#  Math 对象的常用属性

|  名称 | 说明  |
| ------------ | ------------ |
|E |返回常数 e (2.718281828...)|
|LN2 |返回 2 的自然对数 (ln 2)|
|LN10 |返回 10 的自然对数 (ln 10)|
|LOG2E |返回以 2 为底的 e 的对数 (log2e)|
|LOG10E |返回以 10 为底的 e 的对数 (log10e)|
|PI |返回 π（3.1415926535...)|
|SQRT1_2 |返回 1/2 的平方根|
|SQRT2 |返回 2 的平方根|

#  Math 对象的常用方法

|  名称 | 说明  |
| ------------ | ------------ |
|abs(x) |返回 x 的绝对值|
|round(x) |返回 x 四舍五入后的值|
|sqrt(x) |返回 x 的平方根|
|ceil(x) |返回大于等于 x 的最小整数|
|floor(x) |返回小于等于 x 的最大整数|
|sin(x) |返回 x 的正弦|
|cos(x) |返回 x 的余弦|
|tan(x) |返回 x 的正切|
|acos(x) |返回 x 的反余弦值（余弦值等于 x 的角度），用弧度表示|
|asin(x) |返回 x 的反正弦值|
|atan(x) |返回 x 的反正切值|
|exp(x) |返回 e 的 x 次幂 (e^x)|
|pow(n, m) |返回 n 的 m 次幂 (nm)|
|log(x) |返回 x 的自然对数 (ln x)|
|max(a, b) |返回 a, b 中较大的数|
|min(a, b) |返回 a, b 中较小的数|
|random() |返回大于 0 小于 1 的一个随机数|

#  BOM window

|  方法 | 说明  |
| ------------ | ------------ |
|alert()|显示带有一段消息和一个确认按钮的警告框|
|prompt()|显示可提示用户输入的对话框|
|confirm()|显示带有一段消息以及确认按钮和取消按钮的对话框|
|window.onload |当页面加载完成执行|
|window.onunload |当退出页面时执行|
|window.innerWidth|浏览器的宽|
|window.innerHeight |浏览器的高|
|setTimeout()|指定的毫秒数到达之后执行指定的函数，只执行一次|
|setInterval()|设置定时调用的函数也就是可以按照给定的时间（单位毫秒）周期调用函数|

#  DOM HTML 

|  方法 | 说明  |
| ------------ | ------------ |
|write|改变 HTML 输出流|
|innerHTML |改变 HTML 内容|
|attribute |改变 HTML 属性|

#  DOM CSS 

|  方法 | 说明  |
| ------------ | ------------ |
|style.<属性名> |改变 HTML 元素的样式|

#  DOM 节点

|  方法 | 说明  |
| ------------ | ------------ |
|getElementById() |通过元素的 ID 选取元素|
|getElementsByTagName() |通过标签名选取元素|
|getElementsByClassName()|通过类名选取元素|
|createElement()|创建元素节点|
|createAttribute()|创建属性节点|
|createTextNode()|创建文本节点|
|appendChild()|向节点添加最后一个子节点|
|insertBefore (<新子节点>，<指定子节点>) |在指定的子节点前面插入新的子节点|
|removeChild()|删除节点|
|replaceChild()|替换子节点|
|getAttribute()|获取节点属性|
|setAttribute(<属性名>, <属性值>)|设置节点属性|
|removeAttribute()|删除节点属性|

#  DOM 事件

|  事件名 | 说明  |
| ------------ | ------------ |
|onclick	|鼠标单击
|ondblclick	|鼠标双击
|onkeyup	|按下并释放键盘上的一个键时触发
|onchange	|文本内容或下拉菜单中的选项发生改变
|onfocus	|获得焦点，表示文本框等获得鼠标光标。
|onblur	|失去焦点，表示文本框等失去鼠标光标。
|onmouseover	|鼠标悬停，即鼠标停留在图片等的上方
|onmouseout	|鼠标移出，即离开图片等所在的区域
|onload	|网页文档加载事件
|onunload	|关闭网页时
|onsubmit	|表单提交事件
|onreset	|重置表单时

#  Object.prototype 常用成员

| 成员  |  描述 |
| ------------ | ------------ |
|  object.prototype.\_proto\_ |  指向当对象被实例化的时候,用作原型的对象|
| object.prototype.hasOwnProperty()  |  返回一个布尔值,用来判断一个属性是定义在对象本身而不是继承自原型链 |
|object.prototype.isPrototype0f()|返回一个布尔值,表示指定的对象是否在本对象的原型链中|
|object.prototype.toString()|返回一一个表示该对象的字符串|
|object.prototype.value0f()|返回指定对象的原始值|
