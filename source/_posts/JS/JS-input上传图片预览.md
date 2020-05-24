---
title: JS-input上传图片预览
categories: JS
---
![image](https://upload-images.jianshu.io/upload_images/15325592-49b794be8b1f1685?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 代码
```
<html>  
<head>  
<script type="text/javascript" src="jquery.min.js"></script>  
<script>  
$(function(){  
    $("# pstimg").change(function(){  
        var file = this.files[0];  
        alert("文件大小:"+(file.size / 1024).toFixed(1)+"kB");  
        if (window.FileReader) {  
            var reader = new FileReader();  
            reader.readAsDataURL(file);  
            //监听文件读取结束后事件  
            reader.onloadend = function (e) {  
                showXY(e.target.result,file.fileName);  
            };  
        }  
    });  
});  
function showXY(source){  
    var img = document.getElementById("loc_img");  
    img.src = source;  
    alert("Width:"+img.width+", Height:"+img.height);  
}  
</script>  
</head>  
<body>  
<input type="file" name="pstimg" id="pstimg"/>  
<img src="" id="loc_img" />  
<body>  
</html>  
```
