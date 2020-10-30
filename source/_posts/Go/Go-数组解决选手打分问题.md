---
title: Go-数组解决选手打分问题
categories: Go
---
![7a05ce7cb079c59f88a46efc70f26167bb6ed2e5.jpg](https://upload-images.jianshu.io/upload_images/15325592-a95a558f71f5ee8d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  选手打分

> 假设一个场景，相亲现场中，10位小姐姐对1位小哥哥打分，打分区间为1-10分，且每位小姐姐的打分都不相等。现在需要去掉一个最高分和一个最低分后，得出8个打分样本并计算平均分。

#  代码

```
package main

import (
    "fmt"
    "math"
)

func swapTwo(a *int, b *int) {
    *a, *b = *b, *a
}

func main() {
    scoreList := [10]float64{8.5,9.1,9.6,10,9.3,9.7,9.2,9.5,8.9,8.8}
    var maxIndex,minIndex = -1,-1
    var maxScore,minScore = 0.0,11.0
    var i int
    var sumScore = 0.0
    
    for i=0;i<len(scoreList);i++ {
        if scoreList[i]>maxScore {
            maxIndex=i
            maxScore=scoreList[i]
        }

        if scoreList[i]<minScore {
            minIndex=i
            minScore=scoreList[i]
        }
    }    

    if maxScore<minScore {
        swapTwo(&maxIndex, &minIndex)
    }

    for i=maxIndex;i<len(scoreList)-1;i++ {
        scoreList[i] = scoreList[i+1];
    }

    for i=minIndex;i<len(scoreList)-1;i++ {
        scoreList[i] = scoreList[i+1];
    }

    for i=0;i<len(scoreList)-2;i++ {
        sumScore += scoreList[i];
    }
    fmt.Println(math.Round(sumScore / 8 * 100) / 100)
}
```

#   执行

```
$ go run avgScore.go
9.26
```
