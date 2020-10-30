---
title: Flask-virtualenv下的环境配置和安装
categories: Flask
---
![WechatIMG11.jpeg](https://upload-images.jianshu.io/upload_images/15325592-10fbfd678583fc92.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境

- Python 3.7.7

- Flask 1.0.2 

> Flask 是基于 Werkzeug 工具箱和 Jinja2 模板引擎的 Python Web 框架。

- virtualenv 20.0.18

> virtualenv 是用来为一个应用创建一套虚拟的 Python 运行环境。

#  安装virtualenv

- 安装

> 在已经安装过 Python 3 和 pip 的前提下，执行`pip3 install virtualenv`。

- 查看版本

```
$ pip3 freeze | grep virtualenv
virtualenv==20.0.18
```

> 查看安装的 virtualenv 版本，这里的版本是 20.0.18。版本过低的情况下，可以执行`pip3 install virtualenv==20.0.18`升级到此版本。

- 创建虚拟环境

> 任意进入一个目录下执行`virtualenv -p python3 venv`会在此目录下生成一个 venv 文件夹，venv 就是虚拟环境的名称，可以自定义。

- 启动虚拟环境（进入虚拟环境）

```
$ source venv/bin/activate
(venv)
```

> 启动虚拟环境后，命令行中会出现有 (venv) 字样，对应刚刚生成的目录名称，也就是虚拟环境的名称。

#  安装Flask

- 安装

> 在虚拟环境中执行`pip install flask==1.0.2`来安装 flask 框架的 1.0.2 版本。

- 查看版本

```
$ flask --version
Flask 1.0.2
(venv)
```

#  创建项目

- 创建目录

```
$ mkdir flask && cd flask
$ touch app.py
$ mkdir static templates
```

- 查看目录结构

```
$ tree
.
|____app.py
|____static
|____templates
(venv)
```

|  名称 | 说明  |
| ------------ | ------------ |
| app.py |入口文件|
| static  |  静态文件放在 static 目录中 |
| templates |  模板文件放在 templates 目录 |

> flask 非常灵活，它没有一个固定的项目目录组织结构，以上基于 web 应用的简单目录结构。

- 修改 app.py 内容如下：

```
from flask import Flask, render_template
app = Flask(__name__)
#  如果访问根目录 '/' ，返回 Index Page
@app.route('/')
def hello():
    return render_template('hello.html')
```

- 创建 static/hello.css 内容如下：

```
html, body {
    height: 100%;
}
body {
    margin: 0;
    padding: 0;
    width: 100%;
    display: table;
    font-weight: 100;
    font-family: 'Lato';
}
.container {
    text-align: center;
    display: table-cell;
    vertical-align: middle;
}
.content {
    text-align: center;
    display: inline-block;
}
.title {
    font-size: 96px;
}
```

- 创建 templates/hello.html 内容如下：

```
<!DOCTYPE html>
<html>
    <head>
        <title>Flask</title>
        <link
		  rel="stylesheet"
		  type="text/css"
		  href="{{ url_for('static', filename='hello.css') }}"
		/>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <div class="title">Hello world</div>
            </div>
        </div>
    </body>
</html>
```

#  访问项目

- 启动

```
$ export FLASK_APP=app.py && export FLASK_ENV=development && export FLASK_DEBUG=1 && flask run -h 127.0.0.1 -p 8080
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 232-935-217
```

> 在 flask 目录下执行以上命令启动项目。

- 访问

![127.0.0.1_8080_.png](https://upload-images.jianshu.io/upload_images/15325592-dd2b2de4da7a20f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


> 浏览器打开 [http://127.0.0.1:8080](http://127.0.0.1:8080)，如上图所示，成功访问。
