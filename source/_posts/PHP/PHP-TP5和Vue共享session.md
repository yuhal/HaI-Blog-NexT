---
title: PHP-TP5和Vue共享session
categories: PHP
---

![WechatIMG214.jpeg](https://upload-images.jianshu.io/upload_images/15325592-1e1d1731ceb16ba8.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 配置 cookie 有效域名

```
'cookie' => [
      'domain'    => 'domain.com',
],
```

> 修改 application/config.php 中 cookie 配置项，代码如上。

- 服务端响应头配置

```
// 允许单个域名
header('Access-Control-Allow-Origin:https://www.domain.com');
// 支持cookie跨域
header('Access-Control-Allow-Credentials: true');
```

- Vue中axios请求配置

```
// 让ajax携带cookie
axios.defaults.withCredentials = true;
```

> 修改 main.js，代码如上。
