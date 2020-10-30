---
title: Go-解决最短路径问题
categories: Go
---
![WechatIMG59.jpeg](https://upload-images.jianshu.io/upload_images/15325592-184f46813fe45ee8.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  最短路径问题

> wiki:最短路径问题是图论研究中的一个经典算法问题，旨在寻找图（由结点和路径组成的）中两结点之间的最短路径。

#  代码

```
package main

import (
    "fmt"
)

func minPath(matrix  [][]int) int {
	return process(matrix, len(matrix[0])-1)
}

func process(matrix [][]int, i int) int {
	if i == 0 {
		return 0
	} else {
		distance := 999
		for j := 0; j < i; j++ {
			if(matrix[j][i]!=0){
                d_tmp := matrix[j][i] + process(matrix, j);
                if d_tmp < distance {
                    distance = d_tmp;
                }
            }
		}
		return distance
	}
}

func main() {
	m := [][]int{
		{0,5,3,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,1,3,6,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,8,7,6,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,3,5,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,3,5,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3},}
    fmt.Printf("最短路径：%v",minPath(m))
}
```

#  执行

```
$ go run minPath.go
最短路径：18
```
