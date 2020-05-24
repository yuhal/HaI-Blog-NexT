---
title: PHP-过滤HTML标签、属性等正则表达式汇总
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-b170a4c5602740b8?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
```
$str=preg_replace("/\s+/", " ", $str); //过滤多余回车
$str=preg_replace("/<[ ]+/si","<",$str); //过滤<__("<"号后面带空格)
   
$str=preg_replace("/<\!--.*?-->/si","",$str); //注释
$str=preg_replace("/<(\!.*?)>/si","",$str); //过滤DOCTYPE
$str=preg_replace("/<(\/?html.*?)>/si","",$str); //过滤html标签
$str=preg_replace("/<(\/?head.*?)>/si","",$str); //过滤head标签
$str=preg_replace("/<(\/?meta.*?)>/si","",$str); //过滤meta标签
$str=preg_replace("/<(\/?body.*?)>/si","",$str); //过滤body标签
$str=preg_replace("/<(\/?link.*?)>/si","",$str); //过滤link标签
$str=preg_replace("/<(\/?form.*?)>/si","",$str); //过滤form标签
$str=preg_replace("/cookie/si","COOKIE",$str); //过滤COOKIE标签
   
$str=preg_replace("/<(applet.*?)>(.*?)<(\/applet.*?)>/si","",$str); //过滤applet标签
$str=preg_replace("/<(\/?applet.*?)>/si","",$str); //过滤applet标签
   
$str=preg_replace("/<(style.*?)>(.*?)<(\/style.*?)>/si","",$str); //过滤style标签
$str=preg_replace("/<(\/?style.*?)>/si","",$str); //过滤style标签
   
$str=preg_replace("/<(title.*?)>(.*?)<(\/title.*?)>/si","",$str); //过滤title标签
$str=preg_replace("/<(\/?title.*?)>/si","",$str); //过滤title标签
   
$str=preg_replace("/<(object.*?)>(.*?)<(\/object.*?)>/si","",$str); //过滤object标签
$str=preg_replace("/<(\/?objec.*?)>/si","",$str); //过滤object标签
   
$str=preg_replace("/<(noframes.*?)>(.*?)<(\/noframes.*?)>/si","",$str); //过滤noframes标签
$str=preg_replace("/<(\/?noframes.*?)>/si","",$str); //过滤noframes标签
   
$str=preg_replace("/<(i?frame.*?)>(.*?)<(\/i?frame.*?)>/si","",$str); //过滤frame标签
$str=preg_replace("/<(\/?i?frame.*?)>/si","",$str); //过滤frame标签
   
$str=preg_replace("/<(script.*?)>(.*?)<(\/script.*?)>/si","",$str); //过滤script标签
$str=preg_replace("/<(\/?script.*?)>/si","",$str); //过滤script标签
$str=preg_replace("/javascript/si","Javascript",$str); //过滤script标签
$str=preg_replace("/vbscript/si","Vbscript",$str); //过滤script标签
$str=preg_replace("/on([a-z]+)\s*=/si","On\\1=",$str); //过滤script标签
$str=preg_replace("/&# /si","&＃",$str); //过滤script标签，如javaScript:alert(
```
# 清除空格，换行
```
function DeleteHtml($str){
	$str = trim($str);
	$str = strip_tags($str,"");
	$str = ereg_replace("\t","",$str);
	$str = ereg_replace("\r\n","",$str);
	$str = ereg_replace("\r","",$str);
	$str = ereg_replace("\n","",$str);
	$str = ereg_replace(" "," ",$str);
	return trim($str);
}
```
# 过滤HTML属性
```
//过滤所有html标签的属性的正则表达式：
$html = preg_replace("/<([a-zA-Z]+)[^>]*>/","<\\1>",$html);
```
