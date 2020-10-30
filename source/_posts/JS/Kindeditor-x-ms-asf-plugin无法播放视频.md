---
title: Kindeditor-x-ms-asf-plugin无法播放视频
categories: Kindeditor
---

![WechatIMG125.jpeg](https://upload-images.jianshu.io/upload_images/15325592-9b1a5d306a9475a6.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- KindEditor 4.1.7

- Google Chrome Version 85.0.4183.83 (Official Build) (64-bit)

#  问题

![2020-08-31_5f4c9ee944d5d.png](https://upload-images.jianshu.io/upload_images/15325592-6559086b7825d49f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 使用 Kindeditor 编辑器上传的视频，在浏览器中无法播放，原因是 x-ms-asf-plugin 插件不支持。

#  解决

- 修改 kindeditor-min.js

```
function mb(a) {
	if (/\.(rm|rmvb)(\?|$)/i.test(a)) return "audio/x-pn-realaudio-plugin";
	if (/\.(mp4)(\?|$)/i.test(a)) return "video/mp4";
	if (/\.(swf|flv)(\?|$)/i.test(a)) return "application/x-shockwave-flash";
	return "video/x-ms-asf-plugin"
}
```

> 因为 kindeditor-min.js 的代码是经过压缩的，不便于查看。进行代码美化排版一下，找到 mb 方法，增加一行`if (/\.(mp4)(\?|$)/i.test(a)) return "video/mp4";`，完整代码如上。

- 再次上传查看

![Screen Shot 2020-08-31 at 3.29.02 PM.png](https://upload-images.jianshu.io/upload_images/15325592-4d0ebdbe7b924a00.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

