---
title: Linux-安装php-cs-fixer
categories: Linux
---
![image](https://upload-images.jianshu.io/upload_images/15325592-950301a491674e27.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# PHP-CS-Fixer
一个PHP编码标准修复工具，可修复PHP代码以遵循标准，遵循PSR-1，PSR-2等中定义的PHP编码标准，来统一代码风格。官网地址(https://cs.symfony.com/)

# 要求
PHP必须是PHP 5.6.0的最低版本

# 安装
可以运行以下命令来安装php-cs-fixer
```
wget https://cs.symfony.com/download/php-cs-fixer-v2.phar -O php-cs-fixer
```
或指定版本
```
wget https://github.com/FriendsOfPHP/PHP-CS-Fixer/releases/download/v2.16.1/php-cs-fixer.phar -O php-cs-fixer
```
或使用curl
```
curl -L https://cs.symfony.com/download/php-cs-fixer-v2.phar -o php-cs-fixer
```
安装完成后，给所有用户加上可执行权限
```
sudo chmod a+x php-cs-fixer
```
然后将php-cs-fixer移动到/usr/local/bin/目录下
```
sudo mv php-cs-fixer /usr/local/bin/php-cs-fixer
```
最后，执行php-cs-fixer
```
php-cs-fixer
```
看到以下信息表示安装成功
```
PHP CS Fixer 2.16.1 Yellow Bird by Fabien Potencier and Dariusz Ruminski (c8afb59)

Usage:
  command [options] [arguments]

Options:
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  describe     Describe rule / ruleset.
  fix          Fixes a directory or a file.
  help         Displays help for a command
  list         Lists commands
  readme       Generates the README content, based on the fix command help.
  self-update  [selfupdate] Update php-cs-fixer.phar to the latest stable version.
```

