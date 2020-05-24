---
title: PHP-常用到的正则表达式
categories: PHP
---
 ![image](https://upload-images.jianshu.io/upload_images/15325592-fbfbe69c6724072d?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 邮箱验证

```
$email='123456789@qq.com';
$preg_email='/^[a-zA-Z0-9]+([-_.][a-zA-Z0-9]+)*@([a-zA-Z0-9]+[-.])+([a-z]{2,5})$/ims';
if(preg_match($preg_email,$email)){
    echo 1;
}else{
    echo 0;
}

```

# 手机号验证

```
$phone='12345678900';
$preg_phone='/^1[34578]\d{9}$/ims';
if(preg_match($preg_phone,$phone)){
    echo 1;
}else{
    echo 0;
}
```

# 固定号码验证

```
$call='012345678900';
$preg_call='/^(0\d{2,3})?(\d{7,8})$/ims';
if(preg_match($preg_call,$call)){
    echo 1;
}else{
    echo 0;
}

```

# 只包含中英文的名字验证

```
$name='HaI';
$preg_name='/^[\x{4e00}-\x{9fa5}]{2,10}$|^[a-zA-Z\s]*[a-zA-Z\s]{2,20}$/isu';
if(preg_match($preg_name,$name)){
   echo 1;
}else{
   echo 0;
}

```

# 身份证号码验证

```
$IDCard='12345678900';
$preg_card='/^\d{15}|\d{18}$/isu';
if(preg_match($preg_card,$IDCard)){
     echo 1;
}else{
     echo 0;
}        
```

# QQ号码验证

```
$QQ='12345678900';
$preg_QQ='/^\d{5,12}$/isu';
if(preg_match($preg_QQ,$QQ)){
    echo 1;
}else{
    echo 0;
}

```

# 微信号码验证

```
$wechat='12345678900';
$preg_wechat='/^[_a-zA-Z0-9]{5,19}+$/isu';
if(preg_match($preg_wechat,$wechat)){
    echo 1;
}else{
    echo 0;
}
```
