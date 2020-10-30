---
title: Go-实现二分查找的案例
categories: Go
---
![WechatIMG43.jpeg](https://upload-images.jianshu.io/upload_images/15325592-e3062463e7452810.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  案例一

- 介绍

> 在一组数字类型的数组中，查询某个数字的数组下标。

- 创建 simple1.go 内容如下：

```
package main

import (
	"fmt"
)

func main() {
	// 需要查找的数字
	var targetNumb = 8
	// 目标有序数组
	arr := [10]int{10, 2, 7, 4, 6, 5, 3, 8, 1, 10}
	var middle,low = 0,0
	var high = len(arr) - 1
	var isfind = 0

	for {
	    if low <= high {
	    	middle = (high + low) / 2
	    	if arr[middle] == targetNumb {
	    		fmt.Printf("%v 在数组中，下标值为：%v\n",targetNumb,middle)
	    		isfind = 1
	    		break
	    	} else if arr[middle] > targetNumb {
	    		// 说明该数在 low～middle 之间
				high = middle - 1;
	    	} else {
	    		// 说明该数在 middle~high 之间
				low = middle + 1;
	    	}
	    }
	}
	if isfind == 0 {
		fmt.Printf("数组不含 %v\n",targetNumb)
	}
}
```

- 执行

```
$ go run simple1.go
8 在数组中，下标值为：7
```

#  案例二

- 介绍

> 在一组经过任意位数的旋转后的数字类型的有序数组中，查询某个数字的数组下标。

- 创建 simple2.go 内容如下：

```
package main

import (
	"fmt"
	"encoding/json"
)

func main() {
	arr := []int{ 5, 6, 7, 8, 9, 0, 1, 2, 3, 4 }
	str,err := json.Marshal(arr)
    if err != nil {
        panic(err)
    }
    fmt.Printf("原始数据：%s\n",string(str))
	target := 7
	subscript := bs(arr, target, 0, len(arr)-1)
	fmt.Printf("数组下标：%v",subscript)
}

func bs(arr []int, target int, begin int, end int) int {
	if begin == end {
        if target == arr[begin] {
            return begin
        } else {
            return -1
        }
    }
    middle := (begin + end)/2
    if target == arr[middle] {
        return middle
    }
    if arr[begin] <= arr[middle-1] {
        if arr[begin] <= target && target <= arr[middle-1] {
            return bs(arr, target, begin, middle-1)
        } else {
            return bs(arr, target, middle+1, end)
        }
    } else {
        if arr[middle+1] <= target && target <= arr[end] {
            return bs(arr, target, middle+1, end)
        } else {
            return bs(arr, target, begin, middle-1)
        }
    }
}
```

- 执行

```
$ go run simple2.go
原始数据：[5,6,7,8,9,0,1,2,3,4]
数组下标：2
```

#  案例三

- 介绍

> 在一组数字类型的数组中，查询是否存在大于某个数字的数组元素。

- 创建 simple3.go 内容如下：

```
package main

import (
	"fmt"
)

func main() {
	// 需要查找大于的数字
	var targetNumb = 9
	// 目标有序数组
	arr := [10]int{-1, 3, 3, 7, 10, 14, 14}
	var middle,low = 0,0
	var high = len(arr) - 1
	var isfind = 0

	for {
	    if low <= high {
	    	middle = (high + low) / 2
	    	if arr[middle] > targetNumb && (middle == 0 || arr[middle - 1] <= targetNumb) {
	    		fmt.Printf("第一个比 %v 大的数字是 %v\n",targetNumb,arr[middle])
	    		isfind = 1
	    		break
	    	} else if arr[middle] > targetNumb {
	    		// 说明该数在 low～middle 之间
				high = middle - 1;
	    	} else {
	    		// 说明该数在 middle~high 之间
				low = middle + 1;
	    	}
	    }
	}
	if isfind == 0 {
		fmt.Printf("数组不含大于 %v 的数字\n",targetNumb)
	}
}
```

- 执行

```
$ go run simple3.go
第一个比 9 大的数字是 10
```

#  案例四

- 介绍

> 查找两个有序数组合并后的中位数。

- 创建 simple4.go 内容如下：

```
package main
import (
    "fmt"
)

func main(){
    var nums1 = [6]int{1,2,3,4,5,6}
    var nums2 = [3]int{7,8,9}
    median := getMedian(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1)
    fmt.Println(median)
}

func getMedian(a [6]int, begina int, enda int, b [3]int, beginb int, endb int) int {
    if enda - begina == 0 {
        if a[beginb] > b[beginb] {
            return b[beginb]
        } else {
            return a[beginb]
        }
    }
    if enda - begina == 1 {
        if a[begina] < b[beginb] {
            if b[beginb] > a[enda] {
                return a[enda]
            } else {
                return a[beginb]
            }
        } else {
            if b[beginb] < a[enda] {
                return a[begina]
            } else {
                return a[endb]
            }
        }
    }
    if endb-beginb < 2 {
        if (endb - beginb == 0) && (enda - begina)%2 != 0 {
            m := a[beginb]
            bb := b[(enda + begina)/2 - 1]
            c := b[(enda + begina)/2]
            if m < bb {
                return bb
            } else if m < c {
                return m
            } else {
                return c
            }
        } else if (endb - beginb == 0) && (enda - begina)%2 == 0 {
            m := a[beginb]
            c := b[(enda + begina)/2]
            d := b[(enda + begina)/2 + 1]
            if m < c {
                return c
            } else if m < d {
                return m
            } else {
                return d
            }
        } else {
            m := b[beginb]
            n := b[endb]
            bb := a[(enda + begina)/2 - 1]
            c := a[(enda + begina)/2]
            d := a[(enda + begina)/2 + 1]
            if n < bb {
                return bb
            } else if n > bb && n < c {
                return n
            } else if n > c && n < d {
                if m > c {
                    return m
                } else {
                    return c
                }
            } else {
                if m < c {
                    return c
                } else if m < d {
                    return m
                } else {
                    return d
                }
            }
        }
    } else {
        mida := (enda + begina)/2
        midb := (endb + beginb)/2
        if a[mida] < b[midb] {
            step := endb - midb
            return getMedian(a, begina + step, enda, b, beginb, endb - step)
        } else {
            step := midb - beginb
            return getMedian(a, begina, enda - step, b, beginb+ step, endb)
        }
    }
}
```

- 执行

```
$ go run simple4.go
5
```
