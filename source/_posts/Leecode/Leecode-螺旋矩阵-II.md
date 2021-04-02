---
title: Leecode-螺旋矩阵-II
categories: Leecode
---

![WechatIMG588.jpeg](https://upload-images.jianshu.io/upload_images/15325592-51501d85f3f06b7e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第59题：[螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/)
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
示例：
![spiraln.jpeg](https://upload-images.jianshu.io/upload_images/15325592-7e4554a2ddad3025.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

#  解题方法

> 模拟
[参照题解](https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/)

- 解题思路

> 创建一个`n*n`的矩阵`matrix`，矩阵元素都为0
模拟按**右下左上**依次填入数字
首先设定四个方向的边`right,down,left,up`
填入数字`x`的初始值为**1**，终止值`y`为**n*n**
在`[x,y]`区间内，按顺序在四个方向上遍历矩阵`matrix`
向右遍历填充`x`，并将`x`累加，重新设定上边界
向下遍历填充`x`，并将`x`累加，重新设定右边界
向左遍历填充`x`，并将`x`累加，重新设定下边界
向上遍历填充`x`，并将`x`累加，重新设定左边界
最终初始值`x`等于终止值`y`，表示遍历完成
最终得到按顺时针顺序螺旋排列的矩阵`matrix`

- 复杂度

> 时间复杂度：O(n^2)，n是给定的正整数
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        left,up,right,down = 0,0,n-1,n-1
        x,y = 1,n*n
        while x<=y:
            for i in range(left,right+1):
                matrix[up][i] = x
                x+=1
            up+=1

            for i in range(up,down+1):
                matrix[i][right] = x
                x+=1
            right-=1

            for i in range(right,left-1,-1):
                matrix[down][i] = x
                x+=1
            down-=1

            for i in range(down,up-1,-1):
                matrix[i][left] = x
                x+=1
            left+=1
        return matrix
```

> php

```
class Solution {
    function generateMatrix($n) {
        $matrix = array_fill(0,$n,array_fill(0,$n,0));
        $left = $up = 0;
        $right = $down = $n-1;
        $x = 1;
        $y = $n*$n;
        while($x<=$y){
            for($i=$left;$i<=$right;$i++){
                $matrix[$up][$i] = $x;
                $x++;
            }
            $up++;

            for($i=$up;$i<=$down;$i++){
                $matrix[$i][$right] = $x;
                $x++;
            }
            $right--;

            for($i=$right;$i>=$left;$i--){
                $matrix[$down][$i] = $x;
                $x++;
            }
            $down--;

            for($i=$down;$i>=$up;$i--){
                $matrix[$i][$left] = $x;
                $x++;
            }
            $left++;
        }
        return $matrix;
    }
}
```
