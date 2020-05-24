---
title: PHP-curl扩展库使用详解
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-c0c77d8f5050b5d0?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 使用curl发送请求的基本流程
使用CURL的PHP扩展完成一个HTTP请求的发送一般有以下几个步骤：
- 初始化连接句柄
- 设置CURL选项
- 执行并获取结果
- 释放VURL连接句柄

下面的程序片段是使用CURL发送HTTP的典型过程
```
//1.初始化
$ch = curl_init();
//2.设置选项，包括URL
curl_setopt($ch, CURLOPT_URL, "https://www.yuhal.ocm");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HEADER, 0);
//3.执行并获取HTML文档内容
$output = curl_exec($ch);
if($output === FALSE){
	echo "curl error：".curl_error($ch);
}
//4.释放curl句柄
curl_close($ch);
```
上述代码中使用到了四个函数
- curl_init() 和 curl_close() 分别是初始化CURL连接和关闭CURL连接，都比较简单。
- curl_exec() 执行CURL请求，如果没有错误发生，该函数的返回是对应URL返回的数据，以字符串表示满意；如果发生错误，该函数返回 FALSE。需要注意的是，判断输出是否为FALSE用的是全等号，这是为了区分返回空串和出错的情况。
- CURL函数库里最重要的函数是curl_setopt(),它可以通过设定CURL函数库定义的选项来定制HTTP请求。上述代码片段中使用了三个重要的选项：
- CURLOPT_URL 指定请求的URL；
- CURLOPT_RETURNTRANSFER 设置为1表示稍后执行的curl_exec函数的返回是URL的返回字符串，而不是把返回字符串定向到标准输出并返回TRUE；
- CURLLOPT_HEADER设置为0表示不返回HTTP头部信息。

CURL的选项还有很多，可以到PHP的官方网站（[http://www.php.net/manual/en/function.curl-setopt.php](http://www.php.net/manual/en/function.curl-setopt.php)）上查看CURL支持的所有选项列表。

# 获取curl请求的输出信息
在curl_exec()函数执行之后，可以使用curl_getinfo()函数获取CURL请求输出的相关信息，示例代码如下：
```
curl_exec($ch);
$info = curl_getinfo($sh);
echo ' 获取 '.$info['url'].'耗时'.$info['total_time'].'秒';
```
上述代码中curl_getinfo返回的是一个关联数组，包含以下数据：
- url:网络地址。
- content_type:内容编码。
- http_code:HTTP状态码。
- header_size:header的大小。
- request_size:请求的大小。
- filetime:文件创建的时间。
- ssl_verify_result:SSL验证结果。
- redirect_count:跳转计数。
- total_time:总耗时。
- namelookup_time:DNS查询耗时。
- connect_time:等待连接耗时。
- pretransfer_time:传输前准备耗时。
- size_uplpad:上传数据的大小。
- size_download:下载数据的大小。
- speed_download:下载速度。
- speed_upload:上传速度。
- download_content_length:下载内容的长度。
- upload_content_length:上传内容的长度。
- starttransfer_time:开始传输的时间表。
- redirect_time:重定向耗时。
>curl_getinfo()函数还有一个可选择参数\$opt,通过这个参数可以设置一些常量，对应到上术这个字段，如果设置了第二个参数，那么返回的只有指定的信息。例如设置\$opt为CURLINFO_TOTAL_TIME，则curl_getinfo()函数只返回total_time,即总传输消耗的时间，在只需要关注某些传输信息时，设置\$opt参数很有意义。

# 使用curl发送get请求
>如何使用CURL来发送GET请求，发送GET请求的关键是拼装格式正确的URL。请求地址和GET数据由一个“?”分割,然后GET变量的名称和值用“=”分隔，各个GET名称和值由“&”连接。PHP为我们提供了一个函数专门用来拼装GET请求和数据部分——http_build_query,该函数接受一个关联数组，返回由该关联数据描述的GET请求字符串。使用这个函数，结合CURL发送HTTP请求的一般流程，我封闭了一个发送GET请求的函数——dataRequest,具体代码如下：
```
function curl_get($url){  
   $testurl = $url;  
   $ch = curl_init();    
   curl_setopt($ch, CURLOPT_URL, $testurl);    
    //参数为1表示传输数据，为0表示直接输出显示。  
   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);  
    //参数为0表示不带头文件，为1表示带头文件  
   curl_setopt($ch, CURLOPT_HEADER,0);  
   $output = curl_exec($ch);   
   curl_close($ch);   
   return $output;  
 }
```
# 使用curl发送post请求
可以使用CURL提供的选项CURLOPT_POSTFIELDS，设置该选项为POST字符串数据就可以把请求放在正文中。同样我们实现了一个发送POST请求的函数——doCurlPostRequest，代码如下：
```
function curl_post($curlHttp, $postdata) {
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $curlHttp);
    curl_setopt($curl, CURLOPT_HEADER, false);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); //不显示
    curl_setopt($curl, CURLOPT_TIMEOUT, 60); //60秒，超时
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $postdata);
    $data = curl_exec($curl);
    curl_close($curl);
    return $data;
}
```
