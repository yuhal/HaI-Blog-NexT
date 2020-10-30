---
title: Go-实现斐波那契数列
categories: Go
---
![fibonacci-spiral-4720491_1280.jpg](https://upload-images.jianshu.io/upload_images/15325592-1c25709a0dcef9f5.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  斐波那契数列

> 斐波那契数列由0和1开始，之后的斐波那契数就是由之前的两数相加而得出。现通过一个递归函数，输入 x，输出斐波那契数列中第 x 位的元素。

#  代码

```
package main

import (
	"fmt"
)

func main() {
	x := 21
	fmt.Println(fun(x))
}

func fun(n int) int {
	if n == 1 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    return fun(n-1) + fun(n-2);
}
```

> 创建 fibonacci.go，内容如上。

#  执行

```
$ go run fibonacci.go
6765
```
