---
title: Git-配置多个SSH-Key
categories: Git
---

![WechatIMG1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-723bcd98dfacf485.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 场景

当有多个git账号时，比如：
a. 一个gitee，用于公司内部的工作开发；
b. 一个github，用于自己进行一些开发活动；

# 解决

- 生成一个公司用的SSH-Key
`ssh-keygen -t rsa -C 'xxxxx@company.com' -f ~/.ssh/gitee_id_rsa`

- 生成一个github用的SSH-Key
`ssh-keygen -t rsa -C 'xxxxx@qq.com' -f ~/.ssh/github_id_rsa`

- 在 ~/.ssh 目录下新建一个config文件，添加如下内容
```
#  gitee
Host gitee.com
HostName gitee.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/gitee_id_rsa
#  github
Host github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/github_id_rsa
```
>其中Host和HostName填写git服务器的域名，IdentityFile指定私钥的路径

- 用ssh命令分别测试
```
ssh -T git@gitee.com
Hi xxx! You've successfully authenticated, but GITEE.COM does not provide shell access.
```
>这里以gitee为例，成功的话会返回如上内容

转[https://gitee.com/help/articles/4229# article-header0](https://gitee.com/help/articles/4229# article-header0)

