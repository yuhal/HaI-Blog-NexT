---
title: Linux-FileZilla-免密连接阿里云ECS
categories: Linux
---

![WechatIMG490.jpeg](https://upload-images.jianshu.io/upload_images/15325592-105c5f5dcfa26fdf.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  开放22端口

- 阿里云ECS服务器购买完毕，登录账号进入实例，可查看你的服务器

![2021-02-07_601f8f68630f1.png](https://upload-images.jianshu.io/upload_images/15325592-edc09e4d5e336734.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 点击更多–>网络和安全组–>安全组配置

![2021-02-07_601f8ff1af934.png](https://upload-images.jianshu.io/upload_images/15325592-935eb427f1861134.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 查看安全组->内网入方向全部规则–>端口22默认已存

![2021-02-07_601f902fe630b.png](https://upload-images.jianshu.io/upload_images/15325592-1f97d0980ce5469f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  修改VNC密码

- 返回实例列表进行VNC密码的修改

![2021-02-07_601f90c19dcb9.png](https://upload-images.jianshu.io/upload_images/15325592-a008c95de2adcd02.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  创建密钥对

- 左侧导航栏选择密钥对–>创建密钥对

![2021-02-07_601f920c14ce6.png](https://upload-images.jianshu.io/upload_images/15325592-21ffcca104d9aa35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 自定义密钥对名称，点击确定

![2021-02-07_601f929c6da33.png](https://upload-images.jianshu.io/upload_images/15325592-af9551cdd3bd74a4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 页面会自动时生成并提示你保存，会直接生成密钥 .pem 文件，里面是 rsa 的2048位公钥，用于 ssh 远程连接，保存好 .pem 文件。

#  绑定密钥对

![2021-02-07_601f92fba326f.png](https://upload-images.jianshu.io/upload_images/15325592-030f1eccb03e93dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 选择ECS实例

![2021-02-07_601f92de92449.png](https://upload-images.jianshu.io/upload_images/15325592-7c86a32c19595308.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 从左到右依次点按红箭头击保存即可。

#  VNC远程连接

- 配置完毕，进行远程连接–>VNC远程连接

![2021-02-07_601f938d17984.png](https://upload-images.jianshu.io/upload_images/15325592-f789a91f003907a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 输入VNC密码

![2021-02-07_601f93ba3ac65.png](https://upload-images.jianshu.io/upload_images/15325592-33879eb73cea0ca4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 输入账号密码连接成功，如下显示

![2021-02-07_601f9404d0f96.png](https://upload-images.jianshu.io/upload_images/15325592-928cfc75a85eb17c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  FileZilla链接

- 配置站点

![2021-02-07_601f94d5d2309.png](https://upload-images.jianshu.io/upload_images/15325592-4d1a8e56fb728eda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 输入主机名、用户；登录类型选择密钥文件，使用之前保存的密钥对 .pem 文件，最后点击链接即可。

- 成功链接

![2021-02-07_601f958949456.png](https://upload-images.jianshu.io/upload_images/15325592-4248fc5755282b77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
