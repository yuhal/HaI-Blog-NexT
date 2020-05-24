---
title: Vue-环境搭建
categories: Vue
---

![image](https://upload-images.jianshu.io/upload_images/15325592-769127ae65aecda0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

# 环境
- macOS 10.13.6

# 安装homebrew
- 执行命令
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- 查看版本```brew -v```
```
Homebrew 2.1.11-135-g749b6de
Homebrew/homebrew-core (git revision 9639f; last commit 2019-09-26)
Homebrew/homebrew-cask (git revision 1dab; last commit 2019-09-27)
```
# 安装nodejs
- 执行命令
```
brew install nodejs
```
- 查看版本```node -v```
```
v11.0.0
```
# 安装npm
- 执行命令
```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```
- 查看版本```npm -v```
```
6.12.0
```
# 安装webpack
- 执行命令
```
cnpm install webpack -g
```
- 查看版本```cnpm info webpack```
```
webpack@4.41.3 | MIT | deps: 23 | versions: 626
Packs CommonJs/AMD modules for the browser. Allows to split your codebase into multiple bundles, which can be loaded on demand. Support loaders to preprocess files, i.e. json, jsx, es7, css, less, ... and your custom stuff.
https://github.com/webpack/webpack

bin: webpack

dist
.tarball: https://registry.npm.taobao.org/webpack/download/webpack-4.41.3.tgz
.shasum: cb7592c43080337dbc9be9e98fc6478eb3981026

dependencies:
@webassemblyjs/ast: 1.8.5
@webassemblyjs/helper-module-context: 1.8.5
@webassemblyjs/wasm-edit: 1.8.5
@webassemblyjs/wasm-parser: 1.8.5
acorn: ^6.2.1
ajv-keywords: ^3.4.1
ajv: ^6.10.2
chrome-trace-event: ^1.0.2
enhanced-resolve: ^4.1.0
eslint-scope: ^4.0.3
json-parse-better-errors: ^1.0.2
loader-runner: ^2.4.0
loader-utils: ^1.2.3
memory-fs: ^0.4.1
micromatch: ^3.1.10
mkdirp: ^0.5.1
neo-async: ^2.6.1
node-libs-browser: ^2.2.1
schema-utils: ^1.0.0
tapable: ^1.1.3
terser-webpack-plugin: ^1.4.3
watchpack: ^1.6.0
webpack-sources: ^1.4.1

maintainers:
- jhnns <mail@johannesewald.de>
- sokra <tobias.koppers@googlemail.com>
- thelarkinn <sean.larkin@cuw.edu>

dist-tags:
latest: 4.41.3      next: 5.0.0-beta.9  webpack-3: 3.12.0
legacy: 1.15.0      webpack-2: 2.7.0

published 2 days ago by sokra <tobias.koppers@googlemail.com>
```
#  安装vue脚手架
- 执行命令
```
sudo npm install -g vue-cli
```
- 查看版本```vue -V```
```
2.9.6
```
# 创建vue项目
- 执行命令
```
vue init webpack vuetest 
// vuetest 是项目名称
```
# 启动项目
- 进入项目根目录
```
cd vuetest
```
- 执行命令```npm run dev```
```
> vuetest@1.0.0 dev /private/var/HaI/vuetest
> webpack-dev-server --inline --progress --config build/webpack.dev.conf.js

 12% building modules 22/29 modules 7 active ...vuetest/src/components/HelloWorld.vue{ parser: "babylon" } is deprecated; we now treat it as { parser: "babel" }.
 95% emitting

 DONE  Compiled successfully in 7690ms                                          11:18:12 AM

 I  Your application is running here: http://localhost:8080
```
- 请求 http://localhost:8080
![Screen Shot 2019-12-18 at 11.23.55 AM.png](https://upload-images.jianshu.io/upload_images/15325592-7516b2fefe7063e7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


