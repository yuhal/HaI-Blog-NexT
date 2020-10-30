---
title: Go-数组解决汉诺塔问题
categories: Go
---
![WechatIMG42.jpeg](https://upload-images.jianshu.io/upload_images/15325592-23fa3d7509d5b38c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  汉诺塔问题

> 汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。

#  代码

```
package main

import (
    "fmt"
)

func hanio(n int, x string, y string, z string) {
    if n < 1 {
        fmt.Printf("汉诺塔的层数不能小于1")
    } else if n == 1 {
        fmt.Printf("移动：%v -> %v\n", x, z)
        return
    } else {
        hanio(n - 1, x, z, y)
        fmt.Printf("移动：%v -> %v\n", x, z)
        hanio(n - 1, y, x, z)
    }
}

func main() {
    var x,y,z = "x","y","z"
    hanio(3, x, y, z)
}
```

#  执行

```
$ go run hanio.go
移动：x -> z
移动：x -> y
移动：z -> y
移动：x -> z
移动：y -> x
移动：y -> z
移动：x -> z
```
