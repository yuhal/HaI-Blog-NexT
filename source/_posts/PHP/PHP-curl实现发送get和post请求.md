---
title: PHP-curl实现发送get和post请求
categories: PHP
---

![1598944180707.jpg](https://upload-images.jianshu.io/upload_images/15325592-939c9301f31a75cf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 使用curl发送get请求

```
function curl_get($url){  
	$testurl = $url;  
	$ch = curl_init();    
	curl_setopt($ch, CURLOPT_URL, $testurl);    
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);  
	curl_setopt($ch, CURLOPT_HEADER,0);  
	$output = curl_exec($ch);   
	curl_close($ch);   
	return $output;  
 }
```

- 使用curl发送post请求

```
function curl_post($curlHttp, $postdata) {
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, $curlHttp);
	curl_setopt($curl, CURLOPT_HEADER, false);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($curl, CURLOPT_TIMEOUT, 60);
	curl_setopt($curl, CURLOPT_POST, true);
	curl_setopt($curl, CURLOPT_POSTFIELDS, $postdata);
	$data = curl_exec($curl);
	curl_close($curl);
	return $data;
}
```
