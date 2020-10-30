---
title: Go-map解决力扣问题
categories: Go
---
![WechatIMG60.jpeg](https://upload-images.jianshu.io/upload_images/15325592-8ae83b395aa2e857.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  力扣问题

> 给定一个整数数组 arr 和一个目标值 target，在该数组中找出加和等于目标值的两个整数，并返回它们在原数组中的下标。假设，原数组中没有重复元素，而且有且只有一组答案。

#  代码

```
package main

import (
    "fmt"
    "encoding/json"
)

func twoSum(arr []int, target int) (newArr []int) {
	m := make(map[int]int)
	newArr = []int{0}
	for i := 0; i < len(arr); i++ {
		m[arr[i]] = i
		complement := target - arr[i]
		v, ok := m[complement]
		if ok == true && v != i {
			newArr = []int{v,i}
			return newArr;
		} 
	}
	return newArr
}

func main() {
	arr := []int{ 10, 92, 21, 83, 32, 74 }
	str,err := json.Marshal(arr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("原始数据：%s\n",string(str))
	target := 102
	fmt.Printf("目标值：%v\n",target)
	newArr := twoSum(arr, target)
	newStr,err := json.Marshal(newArr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("数组下标：%s\n",string(newStr))
}
```

#  执行

```
$ go run target.go
原始数据：[10,92,21,83,32,74]
目标值：102
数组下标：[0,1]
```
