---
title: Laravel-500-Server-Error
categories: Laravel
---
![image](https://upload-images.jianshu.io/upload_images/15325592-10010ec89888b6ff.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- Laravel Framework 6.4.1
- nginx/1.12.2
- PHP 7.1.8

#  nginx.conf

```
server    
    {
        listen 82;
        server_name 47.98.220.126;
        root /var/www/laravel/public;

        index index.html index.htm index.php;

        if (!-e $request_filename) {
           rewrite  ^(.*)$  /index.php?s=/$1  last;
           break;
        }
        
        # error_page   404   /404.html;

        #  Deny access to PHP files in specific directory
        # location ~ /(wp-content|uploads|wp-includes|images)/.*\.php$ { deny all; }

        include enable-php.conf;

        location /nginx_status
        {
            stub_status on;
            access_log   off;
        }

        location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
        {
            expires      30d;
        }

        location ~ .*\.(js|css)?$
        {
            expires      12h;
        }

        location ~ /.well-known {
            allow all;
        }

        location ~ /\.
        {
            deny all;
        }

        access_log  /home/wwwlogs/access.log;
    }
```

#  请求

![Screen Shot 2019-12-12 at 10.38.54 AM.png](https://upload-images.jianshu.io/upload_images/15325592-fa546d6a733b9bb3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 解决

- 修改 php.ini 中 display_errors 为 On 并保存，开启 php 错误提示。

- 修改 /laravel/storage 目录，赋读、写、执行权限

```
chmod -R 777 storage
```

- 查看 /laravel/storage/logs 中的日志文件，看到报错信息。

```
production.ERROR: No application encryption key has been specified.
```

> 查看文件根目录下有无 .env 文件。

若没有，修改 .env.example 文件名为 .env 。
根目录执行 php artisan key:generate  获取密码，密码会自动保存到 .env 。

- 请求成功

![Screen Shot 2019-12-12 at 11.12.33 AM.png](https://upload-images.jianshu.io/upload_images/15325592-f4ed893b49fb06a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


 
 
