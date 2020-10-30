---
title: Go-关于串的三个经典案例
categories: Go
---
![WechatIMG36.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e6dd161e15b59524.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  子串查找

- 介绍

> 子串查找，也可以成为字符串查找。其中有两个字符串，分为主串和子串(模式串)。在主串中查找是否含有子串，且顺序长度相等。

- 创建 strstr.go 内容如下：

```
package main

import (
    "fmt"
)

func main() {
	var mainString,subString = "mongodb","go"
	var result = false
	for i := 0; i < len(mainString)-len(subString)+1; i++ {
		if mainString[i] == subString[0] {
			var end = 0
			for j := 0; j < len(subString); j++ {
				end = j
				if mainString[i+j] != subString[j] {
					break
				}
			}
			if end == len(subString)-1 {
				result = true
			}
		}
	}
	fmt.Println(result)
}
```

- 执行

```
$ go run strstr.go
true
```

#  最大公共子串

- 介绍
> 最大公共子串，即存在两个字符串中，交集长度最多的一串字符，且顺序长度相等。

- 创建 maxSubStr.go 内容如下：

```
package main

import (
    "fmt"
)

func main() {
	var str1,str2,maxSubStr = "ElasticSearch","ElasticHD",""
	var maxlen,m,n,str1len,str2len = 0,0,0,0,0
	for i := 0; i < len(str1); i++ {
		for j := 0; j < len(str2); j++ {
			if str1[i] == str2[j] {
				m,n = i,j
				str1len,str2len = len(str1),len(str2)
				for ; m<str1len && n<str2len; m,n = m+1,n+1 {
					if str1[m] != str2[n] {
						break
					}
					if maxlen < m-i {
						maxlen = m-i
						maxSubStr = str1[i:m+1]
					}
				}
			}
		}
	}
	fmt.Println(maxSubStr)
}
```

> 上述代码用了三层 for 循环，因此时间复杂度为 O(n)^3。

- 使用`动态规划`方法优化如下。

```
package main

import (
    "fmt"
)

func main() {
	var str1,str2 = "ElasticSearch","ElasticHD"
	m := make([][]int, len(str2)+1) 
        for n := range m{ m[n] = make([]int, len(str1)+1) }

	for i := 1; i <= len(str2); i++ {
	    for j := 1; j <= len(str1); j++ {
	        if str2[i-1] == str1[j-1] {
	            m[i][j] = m[i-1][j-1] + 1
	        }
	    }
	}

	max := 0
	index := 0;
	for x := 0; x < len(str2); x++ {
	    for y := 0; y < len(str1); y++ {
	        if m[x][y] > max {
	            max = m[x][y]
	            index = x
	        }
	    }
	}
	
	maxSubStr := ""
	for i := index-max; i < index; i++ {
		maxSubStr += string(str2[i])
	}
	fmt.Println(maxSubStr)
}
```

- 执行

```
$ go run maxSubStr.go
Elastic
```

#  翻转单词

- 介绍

> 翻转单词，把一段英文单词构成的字符串的顺序逆转。

- 创建 reverseWord.go 内容如下：

```
package main

import (
    "fmt"
    "strings"
)

func main() {
	var str = "she and he"
	arr := strings.Split(str, " ")
	var reverseArr = make([]string, len(arr))
	m := len(arr)-1
	n := 0
	for ; m >= 0; m,n = m-1,n+1 {
		reverseArr[n] = arr[m]
	}
	reverseWord := strings.Join(reverseArr, " ")
	fmt.Println(reverseWord)
}
```

- 执行

```
$ go run reverseWord.go
he and she
```
