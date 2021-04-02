---
title: Git-Gitee仓库自动部署
categories: Git
---
![WechatIMG633.jpeg](https://upload-images.jianshu.io/upload_images/15325592-664d70c5e6423fbb.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- Ubuntu 14.04 

- nginx 1.4.6

- mysql 5.5.44 

- php 5.5.9

#  配置公钥

- 查看 nginx 使用的用户和用户组

```
$ vi /etc/nginx/nginx.conf
user www-data;
......
```

- 生成 www-data 用户的公钥

```
$ sudo -u www-data ssh-keygen -t rsa -C 'Gitee的登录邮箱'
Generating public/private rsa key pair.
Enter file in which to save the key (/var/www/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /var/www/.ssh/id_rsa.
Your public key has been saved in /var/www/.ssh/id_rsa.pub.
The key fingerprint is:
70:32:50:0d:07:82:b9:8c:81:37:a7:20:9f:7d:77:0c zhangyuhai@Xoncology.com
The key's randomart image is:
+--[ RSA 2048]----+
|.  oo.++.        |
|= = .o .E        |
|.B B  + .o       |
|. * . .=. o      |
|     . .S.       |
|                 |
|                 |
|                 |
|                 |
+-----------------+
```

- 添加公钥，点击确定

![2021-03-31_60643b27486da.png](https://upload-images.jianshu.io/upload_images/15325592-a2fca55829221dcf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 将 /var/www/.ssh/id_rsa.pub 中的内容复制到公钥一栏中。

#  创建 test 项目

- 创建 test/index.html，代码如下

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello Yohann! How are you?
I'm fine~
</body>
</html>
```

- 创建 test/webhooks.php，代码如下

```
<?php
// 以流的方式读取
$requestBody = file_get_contents("php:// input");
if (empty($requestBody)) {
    // 这里可以配置异常邮件提醒
    die('send fail');
}
// 项目目录
$projectPath = '/home/test/';
// nginx使用的用户组
$nginxGroup = 'www-data';
// nginx使用的用户
$nginxUser = 'www-data';
// 得到请求内容
$requestBody = json_decode($requestBody,true);
// 加密字符串
$secret_post = $requestBody['sign'];
// 时间戳参数，单位毫秒级
$time_stamp = $requestBody['timestamp'];
// 在WebHooks签名密钥一栏填写的密钥信息
$access_token = '123456';
// 参考加密文档https:// gitee.com/help/articles/4290
$secret_join = $time_stamp . "\n" . $access_token;
// 加密字符串
$base64 = base64_encode(hash_hmac('sha256', $secret_join, $access_token, true));
// 推送的是哪个分支就构建哪个分支，如有需要可以更改规则，比如屏蔽某些分支不构建
$branch = str_replace('refs/heads/', '', $requestBody['ref']);
// 最后将请求内容请空
$requestBody = null;
// 项目根目录下的webhooks.log文件，需要在服务器上创建，并给写权限
$fs = fopen('/home/test/webhooks.log', 'a');
fwrite($fs, date('Y-m-d H:i:s') . ' ================ Update Start ===============' . PHP_EOL);
// 请求ip
$client_ip = $_SERVER['REMOTE_ADDR'];
// 把请求的IP和时间写进log
fwrite($fs, date('Y-m-d H:i:s') . ' Request on [' . date("Y-m-d H:i:s") . '] from [' . $client_ip . ']' . PHP_EOL);
//  验证token，有错就写进日志并退出
if ($base64 !== $secret_post) {
    fwrite($fs, date('Y-m-d H:i:s') . " Invalid token [{$client_token}]" . PHP_EOL);
    $fs and fclose($fs);
    header("HTTP/1.1 404 Not Found");
    header("Status: 404 Not Found");
    exit;
}
// 拉取代码前先赋权限
shell_exec('chown -R '.$nginxGroup.':'.$nginxUser.' '.$projectPath);
// 执行shell命令并把返回信息写进日志，php.ini中shell_exec若被禁用，需要先开启。
$output = shell_exec('git pull origin '.$branch.' 2<&1');
// 拉取代码前再赋权限
shell_exec('chown -R '.$nginxGroup.':'.$nginxUser.' '.$projectPath);
// 代码同步信息写入日志
fwrite($fs, date('Y-m-d H:i:s') . 'Info:' . print_r($output, true) . PHP_EOL);
fwrite($fs, date('Y-m-d H:i:s') .  '================ Update End ===============' . PHP_EOL . PHP_EOL);
// 关闭日志文件
$fs and fclose($fs);
```

- 项目示例

![2021-03-31_60643c3ccfdfe.png](https://upload-images.jianshu.io/upload_images/15325592-1db8dbfa87c2a749.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 登录服务器，在 /home 目录下，拉取 test 项目。

- test 目录赋权限

```
$ chown -R www-data:www-data /home/test/
```

#  配置WebHooks 

- 点击**添加 webHook**

![2021-03-31_60644025d352d.png](https://upload-images.jianshu.io/upload_images/15325592-8eb7ed1b07ed39e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 点击**添加**

![2021-03-31_606440d665bfe.png](https://upload-images.jianshu.io/upload_images/15325592-7751c6d8ed4aabed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 注意：这里的**签名密钥**要跟 webhooks.php 中保持一致。

#  测试自动部署

- 首次访问

```
$ curl 47.117.122.160
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello Yohann! How are you?
I'm fine~
</body>
</html>
```

- 编辑 test/index.html，代码如下

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello World!
</body>
</html>
```

> 提示：可以在 Gitee 仓库的 master 分支上直接编辑。

- 再次访问

```
$ curl 47.117.122.160
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello World!
</body>
</html>
```

> 访问内容发生变化，表示配置成功。
