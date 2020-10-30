---
title: Go-实现常用的四种算法排序
categories: Go
---
![WechatIMG57.jpeg](https://upload-images.jianshu.io/upload_images/15325592-cc003b813cb6c027.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  冒泡排序

- 介绍

> 从第一个数据开始，依次比较相邻元素的大小。如果前者大于后者，则进行交换操作，把大的元素往后交换。通过多轮迭代，直到没有交换操作为止。

- 创建 bubble.go 内容如下：

```
package main

import (
	"fmt"
	"encoding/json"
)

func main() {
	arr := [10]int{ 1, 0, 3, 4, 5, -6, 7, 8, 9, 10 }
	str,err := json.Marshal(arr)
    if err != nil {
        panic(err)
    }
	fmt.Printf("原始数据：%s\n",string(str))
	var i,j = 1,0
	for ;i < len(arr); i++ {
		for ;j < len(arr) - i; j++ {
			if arr[j] > arr[j + 1] {
				var temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = temp
			} 
		}
	}

	bubbleStr,err := json.Marshal(arr)
    if err != nil {
        panic(err)
    }
	fmt.Printf("冒泡排序：%s",string(bubbleStr))
}
```

- 执行

```
$ go run bubble.go
原始数据：[1,0,3,4,5,-6,7,8,9,10]
冒泡排序：[0,1,3,4,-6,5,7,8,9,10]
```

#  插入排序

- 介绍

> 选取未排序的元素，插入到已排序区间的合适位置，直到未排序区间为空。

- 创建 insert.go 内容如下：

```
package main

import (
    "fmt"
    "encoding/json"
)

func main() {
    arr := [10]int{ 2, 3, 5, 1, 23, 6, 78, 34 }
    str,err := json.Marshal(arr)
    if err != nil {
        panic(err)
    }
    fmt.Printf("原始数据：%s\n",string(str))
    
    var i = 1
    for ;i < len(arr); i++ {
        var temp = arr[i]
        var j = i - 1
        for ; j >= 0; j-- {
            if arr[j] > temp {
                arr[j + 1] = arr[j]
            } else {
                break
            }
        }
        arr[j + 1] = temp
    }

    bubbleStr,err := json.Marshal(arr)
    if err != nil {
        panic(err)
    }
    fmt.Printf("插入排序：%s",string(bubbleStr))
}
```

- 执行

```
$ go run insert.go
原始数据：[2,3,5,1,23,6,78,34,0,0]
插入排序：[0,0,1,2,3,5,6,23,34,78]
```

#  归并排序

- 介绍

> 归并排序的原理其实就是分治法（二分法）。它采用了二分的迭代方式，首先将数组不断地二分，直到最后每个部分只包含 1 个数据。然后再对每个部分分别进行排序，最后将排序好的相邻的两部分合并在一起，这样整个数组就有序了。

- 创建 merge.go 内容如下：

```
package main

import (
	"fmt"
	"encoding/json"
)

func customMergeSort(a []int, start int, end int) {
	if start < end {
		var mid = (start + end) / 2;
		// 对左侧子序列进行递归排序
		customMergeSort(a, start, mid);
		// // 对右侧子序列进行递归排序
		customMergeSort(a, mid+1, end);
		// // 合并
		customDoubleMerge(a, start, mid, end);
	}
}

func customDoubleMerge(arr []int, start int, mid int, end int){
    leftLen:=mid-start+1
    rightLen:=end-mid
 
    arrLeft:=make([]int,leftLen)
    for i:=0;i<leftLen;i++{
        arrLeft[i]=arr[start+i]
    }
 
    arrRight:=make([]int,rightLen)
    for j:=0;j<rightLen;j++{
        arrRight[j]=arr[mid+j+1]
    }
 
    i,j,k:=0,0,start
    for ;k<=end&&i<leftLen&&j<rightLen;k++{
        if arrLeft[i]<=arrRight[j]{
            arr[k]=arrLeft[i]
            i++
        }else{
            arr[k]=arrRight[j]
            j++
        }
    }
 
    for ;i<leftLen&&k<=end;k++{
        arr[k]=arrLeft[i]
        i++
    }
 
    for ;j<rightLen&&k<=end;k++{
        arr[k]=arrRight[j]
        j++
    }
}

func main() {
	arr := []int{ 49, 38, 65, 97, 76, 13, 27, 50 }
	str,err := json.Marshal(arr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("原始数据：%s\n",string(str))
	customMergeSort(arr, 0, len(arr)-1)
	mergeStr,err := json.Marshal(arr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("归并排序：%s\n",string(mergeStr))
}
```

- 执行

```
$ go run merge.go
原始数据：[49,38,65,97,76,13,27,50]
归并排序：[13,27,38,49,50,65,76,97]
```

#  快速排序

- 介绍

> 快速排序法的原理也是分治法。它的每轮迭代，会选取数组中任意一个数据作为分区点，将小于它的元素放在它的左侧，大于它的放在它的右侧。再利用分治思想，继续分别对左右两侧进行同样的操作，直至每个区间缩小为 1，则完成排序。

- 创建 quick.go 内容如下：

```
package main

import (
	"fmt"
	"encoding/json"
)

func customQuickSort(arr []int, start, end int) {
    if start < end {
        i, j := start, end
        key := arr[(start+end)/2]

        for i <= j {
            for arr[i] < key {
                i++
            }
            for arr[j] > key {
                j--
            }
            if i <= j {
                arr[i], arr[j] = arr[j], arr[i]
                i++
                j--
            }
        }

        if start < j {
            customQuickSort(arr, start, j)
        }
        if end > i {
            customQuickSort(arr, i, end)
        }
    }
}

func main() {
	arr := []int{ 6, 1, 2, 7, 9, 11, 4, 5, 10, 8 }
	str,err := json.Marshal(arr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("原始数据：%s\n",string(str))
	customQuickSort(arr, 0, len(arr)-1)
	quickStr,err := json.Marshal(arr)
	if err != nil {
		panic(err)
	}
	fmt.Printf("快速排序：%s\n",string(quickStr))
}
```

- 执行

```
$ go run quick.go
原始数据：[6,1,2,7,9,11,4,5,10,8]
快速排序：[1,2,4,5,6,7,8,9,10,11]
```


