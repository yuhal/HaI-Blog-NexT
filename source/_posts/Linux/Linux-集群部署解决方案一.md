---
title: Linux-集群部署解决方案一
categories: Linux
---
![WechatIMG637.jpeg](https://upload-images.jianshu.io/upload_images/15325592-03581e69dacdc464.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  集群部署图例

![2021-04-01_60653c534a881.jpg](https://upload-images.jianshu.io/upload_images/15325592-2261d46463a19ac8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  准备工作

> 两台阿里云ECS实例中均部署 gitee 仓库项目，传送 [Git Gitee仓库自动部署](https://www.jianshu.com/p/bd3978aa81c2 "Git Gitee仓库自动部署")；
实现文件双向实时同步，传送 [Linux Sersync+Rsync实现文件双向实时同步](https://www.jianshu.com/p/1b34f3c1ec53 "Linux Sersync+Rsync实现文件双向实时同步")；
实现数据库同步实现双机互备，传送 [Mysql 数据库同步实现双机互备](https://www.jianshu.com/p/4d016fdf391a "Mysql 数据库同步实现双机互备")。

- Gitee 仓库

- 阿里云ECS实例*2

- 阿里云负载均衡实例

#  创建负载均衡实例

> 参考[官方教程](https://help.aliyun.com/document_detail/86454.html# task-bh5-dll-vdb "官方教程")

- 选择**传统型负载均衡 CLB(原SLB)**->**实例管理**

![2021-03-31_60641c8cb99e1.png](https://upload-images.jianshu.io/upload_images/15325592-15b2c75e1b3d7763.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 点击**创建传统型负载均衡**

![2021-03-31_60641e097b1c8.png](https://upload-images.jianshu.io/upload_images/15325592-aacbb349809025ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 点击**立即购买**

![2021-03-31_606420ec8ee3c.png](https://upload-images.jianshu.io/upload_images/15325592-ac5cd3a1608d87e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 注意：稍后**添加后端的服务器**只能选该**地域和可用区**下的阿里云ECS实例，创建阿里云ECS实例的教程这里略过。

- 点击**立即开通**

![2021-03-31_606421fe6884e.png](https://upload-images.jianshu.io/upload_images/15325592-efbaf02cd227fd2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  配置负载均衡实例

> 参考[官方教程](https://help.aliyun.com/document_detail/86451.html# task-bh5-dll-vdb "官方教程")

- 打开**负载均衡管理控制台**，选择**传统型负载均衡 CLB(原SLB)**->**实例管理**，点击**添加后端服务器**

![2021-03-31_6064246c627a5.png](https://upload-images.jianshu.io/upload_images/15325592-3765590d4c550129.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 选择服务器，点击**下一步**

![2021-03-31_606424bcb30c0.png](https://upload-images.jianshu.io/upload_images/15325592-7414d8dca4074ba3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->




- 配置权重，点击**添加**

![2021-03-31_606429cd80e18.png](https://upload-images.jianshu.io/upload_images/15325592-68050b136622d430.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 注意：稍后配置的**调度算法**会受**权重**的影响，这里先默认都是100。

- 返回**负载均衡管理控制台**，选择**传统型负载均衡 CLB(原SLB)**->**实例管理**，点击**监听配置向导**

![2021-03-31_6064280bb35cb.png](https://upload-images.jianshu.io/upload_images/15325592-71924444b7a12448.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 配置协议&监听，点击**下一步**

![2021-03-31_606427f252637.png](https://upload-images.jianshu.io/upload_images/15325592-bd2a5cb184e38712.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->



> 端口设置为**80**，调度算法为**一致性哈希**。

- 配置后端服务器，点击**下一步**

![2021-03-31_606429cd80e18.png](https://upload-images.jianshu.io/upload_images/15325592-2a0a61f55aea2e54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- **健康检查**可以跳过，进入**配置审核**后提交

#  测试负载均衡

> 47.117.122.160 作为 server1
47.117.135.141 作为 server2

- 登录 server1，编辑 /home/test/index.html，代码如下

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello server1
</body>
</html>
```

- 登录 server2，编辑 /home/test/index.html，代码如下

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
Hello server2
</body>
</html>
```

> 为了看到测试的变化，先手动修改。测试成功后在改回原来的内容，保持与 Gitee仓库 版本一致。

- 测试访问

![2021-03-31_60644d4ff05e3.png](https://upload-images.jianshu.io/upload_images/15325592-2f93a9495c0052ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


![2021-03-31_60644d3208ad1.png](https://upload-images.jianshu.io/upload_images/15325592-723d04c4d7ba15a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 浏览器访问负载均衡实例的公网IP，通过多次刷新看到页面变化，说明搭建成功。
