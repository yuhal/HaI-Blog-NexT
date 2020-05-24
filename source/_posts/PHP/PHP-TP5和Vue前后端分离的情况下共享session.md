---
title: PHP-TP5和Vue前后端分离的情况下共享session
categories: PHP
---
![image](https://upload-images.jianshu.io/upload_images/15325592-8212929e6f1c706b?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
1、首先在Thinkphp5的应用配置文件application/config.php下修改cookie配置项，让二级域名共享cookie
```
//在cookie选项加入domain，配置域名
'cookie' => [
    // cookie 有效域名
      'domain'    => 'domain.com',
],
```
2、服务器端响应头配置
```
header('Access-Control-Allow-Origin:https://www.domain.com');//允许单个域名
header('Access-Control-Allow-Credentials: true');//支持cookie跨域
```
3、Vue中axios请求配置
XMLHttpRequest的withCredentials标志设置为true，从而使得Cookies可以随着请求发送。因为这是一个简单的GET请求，所以浏览器不会发送一个“预请求”。但是，如果服务器端的响应中，如果没有返回Access-Control-Allow-Credentials: 
true的响应头，那么浏览器将不会把响应结果传递给发出请求的脚步程序，以保证信息的安全
```
在main.js中配置axios
axios.defaults.withCredentials = true;//让ajax携带cookie
```

ThinkPHP5水平分表后分页查询解决方案
[https://blog.csdn.net/tdcqfyl/article/details/82466959](https://blog.csdn.net/tdcqfyl/article/details/82466959)
