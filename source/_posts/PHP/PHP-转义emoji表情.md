---
title: PHP-转义emoji表情
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-2b3e16831ee9360c?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
/**
  把用户输入的文本转义（主要针对特殊符号和emoji表情）
 */
function userTextEncode($str){
    if(!is_string($str))return $str;
    if(!$str || $str=='undefined')return '';

    $text = json_encode($str); //暴露出unicode
    $text = preg_replace_callback("/(\\\u[ed][0-9a-f]{3})/i",function($str){
        return addslashes($str[0]);
    },$text); //将emoji的unicode留下，其他不动，这里的正则比原答案增加了d，因为我发现我很多emoji实际上是\ud开头的，反而暂时没发现有\ue开头。
    return json_decode($text);
}
/**
  解码上面的转义
 */
function userTextDecode($str){
    $text = json_encode($str); //暴露出unicode
    $text = preg_replace_callback('/\\\\\\\\/i',function($str){
        return '\\';
    },$text); //将两条斜杠变成一条，其他不动
    return json_decode($text);
}
```
# 优点
1、只转换表情，不会转换中文，所以数据还是直接可读的

2、不会把表情转换为其它标准，只有一个简单的，固定的转换算法，也就是说不需要一个表情库来对照着转换，所以以后其它人要使用这个数据的时候，也很容易知道每个表情是对应的哪个。就算苹果大爷又增加了表情，也不需要做什么额外的修改。

3、可以无限decode输出的都是正确的内容。因为有的时候可能需要在一次请求中的两个地方做decode，其它decode多次会把正确的数据改成其它数据，这个不会。

# 缺点
1、看了上面的代码就知道，这个是强制修改字符编码中，指定区间内的编码，也就说有可能误杀，也有可能有超出这个区间的emoji没杀到。不过仅仅是在字符前加反斜杠，即使误杀了，发现之后也很容易改回来。

