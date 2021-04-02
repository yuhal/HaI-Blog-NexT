---
title: Linux-LVS-NAT搭建集群环境
categories: Linux
---
![WechatIMG593.jpeg](https://upload-images.jianshu.io/upload_images/15325592-218c783030060b84.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  Linux LVS/NAT搭建集群环境

#  环境

- ubuntu 18.04

- docker 20.10

> 如需按照 docker，前往 [Docker 快速安装](https://www.jianshu.com/p/f160e1082036 "Docker 快速安装")。

- ipvsadm 1.28

#  安装ipvsadm

- 更新软件源

```
$ apt-get update
```

- 执行安装

```
$ apt-get install ipvsadm
```

- 查看版本

```
$ ipvsadm -v
```

#  配置集群服务器

- 使用 docker 创建 ubuntu 容器，模拟集群所需要的多台服务器

```
#  server1和server2
$ docker run --privileged --name=server1 -tdi ubuntu
$ docker run --privileged --name=server2 -tdi ubuntu
```

- 登录 server1

```
root@e73bba5a5b33:/#  docker attach server1
```

- 更新软件源

```
root@e73bba5a5b33:/#  apt-get update
```

- 安装 vim、nginx、net-tools

```
root@e73bba5a5b33:/#  apt-get install vim nginx net-tools -y 
```

- 启动 nginx

```
root@e73bba5a5b33:/#  service nginx start
```

- 修改 nginx 页面

```
root@e73bba5a5b33:/#  vim /var/www/html/index.nginx-debian.html
<h1>Welcome to nginx</h1>
修改为
<h1>Welcome to nginx!server1</h1>
```

> 修改nginx默认展示的html页面，以区分访问的server1还是server2。

- 查看私有IP

```
root@e73bba5a5b33:/#  ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 19713  bytes 48143630 (48.1 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11346  bytes 827130 (827.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

> 查看到server1的私有IP是`172.17.0.2`，使用快捷键`ctrl+p+q`退出当前容器，登录 server2 做以上同样的配置。

#  配置负载均衡器

- 开启内核路由转发 

```
#  开启当前主机的内核路由转发
$ echo '1' | sudo tee /proc/sys/net/ipv4/ip_forward
#  查看是否开启，返回1说明已开启
$ cat /proc/sys/net/ipv4/ip_forward
1 
```

- 使用 ipvsadm 添加 ipvs 规则

```
#  创建集群服务
$ ipvsadm -A -t 172.18.119.29:80 -s rr
#  添加 server1
$ ipvsadm -a -t 172.18.119.29:80 -r 172.17.0.2 -m
#  添加 server2
$ ipvsadm -a -t 172.18.119.29:80 -r 172.17.0.3 -m
#  查看 ipvs 定义的规则
$ ipvsadm -l
```

> `172.18.119.29`是当前主机的`私有IP`，`172.17.0.2`和`172.17.0.3`分别是server1和server2的私有IP。

#  测试负载均衡

![2021-03-18_6052f60c5ad29.png](https://upload-images.jianshu.io/upload_images/15325592-d6d8ef0623b9a876.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
![2021-03-18_6052f63705bbb.png](https://upload-images.jianshu.io/upload_images/15325592-72c7ebc24b5d0045.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

> 浏览器访问当前主机的`公网IP`，通过多次刷新看到页面变化，说明搭建成功。
