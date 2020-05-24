---
title: PHP-利用多进程处理任务
categories: PHP
---

![image](https://upload-images.jianshu.io/upload_images/15325592-67e83cbf0ccd1a95?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

PHP多进程一般应用在PHP_CLI命令行中执行php脚本，不要在web访问时使用。
多进程处理分解任务一般要比单进程更快。

# php查看是否安装多进程模块
```
php -m | grep pcntl
```
创建子进程的函数fork，了解过C语言的同学应该都知道这个。
php多进程的一些库函数手册：[http://php.net/manual/zh/function.pcntl-fork.php](http://php.net/manual/zh/function.pcntl-fork.php)
pcntl_fork — 在当前进程当前位置产生分支（子进程）。
译注：fork是创建了一个子进程，父进程和子进程 都从fork的位置开始向下继续执行，不同的是父进程执行过程中，得到的fork返回值为子进程号，而子进程得到的是0。

# 一个fork子进程的基础示例
```
<?php
$pid = pcntl_fork();
//父进程和子进程都会执行下面代码
if ($pid == -1) {
    //错误处理：创建子进程失败时返回-1.
     die('could not fork');
} else if ($pid) {
     //父进程会得到子进程号，所以这里是父进程执行的逻辑
     pcntl_wait($status); //等待子进程中断，防止子进程成为僵尸进程。
} else {
     //子进程得到的$pid为0, 所以这里是子进程执行的逻辑。
}
```
如果一个任务被分解成多个进程执行，就会减少整体的耗时。
比如有一个比较大的数据文件要处理，这个文件由很多行组成。如果单进程执行要处理的任务，量很大时要耗时比较久。这时可以考虑多进程。
多进程处理分解任务，每个进程处理文件的一部分，这样需要均分割一下这个大文件成多个小文件（进程数和小文件的个数等同就可以）。
比如该文件file.log有10万行数据，现在想分4个进程处理。需要分割2.5万行一个文件。命令split可以做到。
split的用法比较简单，可以man split查看下手册。 
```
split -l 25000 -d file.log prefix_name
```
-l是按照行分割，-d是分割后的文件名按照数字，-a是分割后的文件个数位数（默认是2，做多就是99个；比如超过100个，-a可以写3）。自己尝试分割一下就知道了。
# 处理代码：
```
<?php
shell_exec('split -l 25000 -d file.log prefix_name');
// 3个子进程处理任务
for ($i = 0; $i < 3; $i++){
    $pid = pcntl_fork();

    if ($pid == -1) {
        die("could not fork");

    } elseif ($pid) {
        echo "I'm the Parent $i\n";

    } else {// 子进程处理
        $content = file_get_contents("prefix_name0".$i);
        // 业务处理 begin

        // 业务处理 end

        exit;// 一定要注意退出子进程,否则pcntl_fork() 会被子进程再fork,带来处理上的影响。
    }
}

// 等待子进程执行结束
while (pcntl_waitpid(0, $status) != -1) {
    $status = pcntl_wexitstatus($status);
    echo "Child $status completed\n";
}
```

转载[https://www.cnblogs.com/firstForEver/p/7301630.html](https://www.cnblogs.com/firstForEver/p/7301630.html)
