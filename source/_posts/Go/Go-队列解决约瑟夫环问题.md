---
title: Go-队列解决约瑟夫环问题
categories: Go
---

![2020-06-04_5ed8bd1aa04f1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-ad22456d2877807a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  约瑟夫环

> 约瑟夫环是一个数学的应用问题，具体为，已知 n 个人（以编号 1，2，3...n 分别表示）围坐在一张圆桌周围。从编号为 k 的人开始报数，数到 m 的那个人出列；他的下一个人又从 1 开始报数，数到 m 的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。这个问题的输入变量就是 n 和 m，即 n 个人和数到 m 的出列的人。输出的结果，就是 n 个人出列的顺序。

#  代码

```
package main

import "fmt"

func JosephRing(queue [13]int, n int, m int) {
	var front,rear,round = 0,n,0
	var i int
	for {
		if rear-front==0 { //队不为空 
			break // 跳出循环
		}
		for i=0;i<m-1;i++ {
			front=(front+1)%n
			rear=(rear+1)%n
			queue[rear]=queue[front]
		}
		front=(front+1)%n
		round++
		fmt.Printf("第%d轮:%d\n",round,queue[front])
	}
	return
}

func main() {
	var queue [13]int
	var n,m = 12,3
	var i int
	queue[0] = n
	//初始化队列，入队 
	for i=1;i<n+1;i++{
		queue[i] = i
	}
	JosephRing(queue, n, m)
}
```

#  执行

```
$ go run josephRing.go
第1轮:3
第2轮:6
第3轮:9
第4轮:12
第5轮:4
第6轮:8
第7轮:1
第8轮:7
第9轮:2
第10轮:11
第11轮:5
第12轮:10
```

