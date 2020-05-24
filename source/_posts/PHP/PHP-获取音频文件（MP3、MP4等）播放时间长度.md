---
title: PHP-获取音频文件（MP3、MP4等）播放时间长度
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-da116e2655c14b5f?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
# 一、首先，我们需要先下载一份PHP类—getid3
[https://codeload.github.com/JamesHeinrich/getID3/zip/master](https://codeload.github.com/JamesHeinrich/getID3/zip/master)
# 二、解压放入项目，并引用
```
<?php 
include_once ROOT_PATH.'extend/gedit3/getid3/getid3.php';
$getID3 = new \getID3();
$ThisFileInfo = @$getID3->analyze($path); 
//分析文件，$path为音频文件的地址（文件绝对路径）
$fileduration= $ThisFileInfo['playtime_seconds']; 
//这个获得的便是音频文件的时长
```

转载[https://blog.csdn.net/lovelessdream/article/details/87861210](https://blog.csdn.net/lovelessdream/article/details/87861210)
