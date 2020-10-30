---
title: Vue-解决跨域问题
categories: Vue
---
![1921600225473_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-7ec43577af036fca.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- laradock

- @vue/cli 4.5.4

#  问题

- 启动 vue 项目

```
$ yarn serve
```

![2020-09-16_5f6177d2a45f7.png](https://upload-images.jianshu.io/upload_images/15325592-ebbda64d0a5ed44d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


- 访问

![2020-09-16_5f61789f5bdf7.png](https://upload-images.jianshu.io/upload_images/15325592-2daf2a059e4edd4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 访问 http://localhost:8080/admin-dev/ ，看到 network 中请求的 api 报错如上图所示。这是因为后端 api 请求仅支持80端口，这边指向8080，势必不行。

#  解决

- 修改 vue.config.js

```
let proxyObj = {};
proxyObj['/ws'] = {
    ws: true,
    target: "ws://192.168.50.186:8081"
};
proxyObj['/'] = {
    ws: false,
    target: "http://192.168.50.186:80",
    changeOrigin: true,
    pathRewrite: {
        '^/': ''
    }
};
module.exports = {
  devServer: {
      host: '0.0.0.0',
      port: 8080,
      proxy: proxyObj
  }
}
```

> 使用 devServer.proxy 完成代理配置即可，proxyObj.target 指向的是请求的 api 地址，这里分别代理了 api 和 websocket 请求。

- 再次启动 vue 项目

![2020-09-16_5f617e6438e07.png](https://upload-images.jianshu.io/upload_images/15325592-5b4dbc241106e21f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
