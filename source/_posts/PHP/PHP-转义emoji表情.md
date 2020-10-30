---
title: PHP-转义emoji表情
categories: PHP
---

![WechatIMG129.jpeg](https://upload-images.jianshu.io/upload_images/15325592-d54c05b3a1a44f30.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 转码

```
function userTextEncode($str){
	if(!is_string($str)) return $str;
	if(!$str || $str=='undefined') return '';
	$text = json_encode($str);
	$text = preg_replace_callback("/(\\\u[ed][0-9a-f]{3})/i",function($str){
		return addslashes($str[0]);
	},$text);
	return json_decode($text);
}
```

- 解码

```
function userTextDecode($str){
	$text = json_encode($str);
	$text = preg_replace_callback('/\\\\\\\\/i',function($str){
		return '\\';
	},$text);
	return json_decode($text);
}
```
