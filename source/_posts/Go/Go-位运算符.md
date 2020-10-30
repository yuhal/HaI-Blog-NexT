---
title: Go-位运算符
categories: Go
---
![WechatIMG266.jpeg](https://upload-images.jianshu.io/upload_images/15325592-8f2403bef7de7fe6.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 代码

```
package main
import "fmt"
func main() {
	fmt.Println(1&1)
	fmt.Println(1|0)
	fmt.Println(1^1)
}
```

- 执行

```
1
1
0
```

- 总结

|  位运算符 |   说明|
| ------------ | ------------ |
|  & |  表示`按位与操作`，都是1时，结果才为1 | 
|I  |表示`按位或运算`，也称为`双目运算符`，只要有1，那么就是1 | 
|  ^|  表示`按位异或运算`，只要一样结果就是0 | 
