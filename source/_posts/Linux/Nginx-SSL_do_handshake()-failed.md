---
title: Nginx-SSL_do_handshake()-failed
categories: Nginx
---

![image](https://upload-images.jianshu.io/upload_images/15325592-e0d3e806ca16f02f.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

nginx做正向代理https遇到502错误返回，查看nginx的错误日志发现有大量的此类错误
```
SSL_do_handshake() failed (SSL: error:14094085:SSL routines:ssl3_read_bytes:ccs received early) while SSL handshaking, client: 52.81.99.160
```
解决方法是在nginx配置文件location一栏中增加：
```
location / {
	proxy_ssl_session_reuse off;
}
```
然后重启nginx
```
service nginx restart
```
