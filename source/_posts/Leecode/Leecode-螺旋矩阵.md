---
title: Leecode-螺旋矩阵
categories: Leecode
---

![WechatIMG587.jpeg](https://upload-images.jianshu.io/upload_images/15325592-c3fb4e257d3c9eba.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第54题：[螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
![spiral1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-fa8349a8db02ffd6.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  解题方法

> 模拟
[参照题解](https://leetcode-cn.com/problems/spiral-matrix/solution/cxiang-xi-ti-jie-by-youlookdeliciousc-3/)

- 解题思路

> 获取矩阵`matrix`的行数`m`和列数`n`
模拟`matrix`按**右下左上**走过的路径
首先设定四个方向的边界`right,down,left,up`
按顺序在四个方向上遍历矩阵
创建数组`ans`来记录每次遍历的元素
向右遍历，重新设定上边界，若上边界大于下边界，跳出循环
向下遍历，重新设定右边界，若右边界小于左边界，跳出循环
向左遍历，重新设定下边界，若下边界小于上边界，跳出循环
向上遍历，重新设定左边界，若左边界大于右边界，跳出循环
最终在四个方向都没有可遍历的元素，表示遍历完成
得到的`ans`就是矩阵按照**顺时针螺旋顺序**返回的所有元素

- 复杂度

> 时间复杂度：O(mn)，m和n分别为矩阵的行数和列数
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def spiralOrder(self,matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        right,down,left,up = n-1,m-1,0,0
        result = []
        while True:
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up += 1
            if up > down:
                break

            for i in range(up,down+1):  
                result.append(matrix[i][right])
            right -= 1 
            if right < left:
                break

            for i in range(right,left-1,-1):
                result.append(matrix[down][i])
            down -= 1
            if down < up:
                break

            for i in range(down,up-1,-1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return result
```

> php

```
class Solution {
    function spiralOrder($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $right = $n-1; 
        $down = $m-1;
        $left = 0;
        $up = 0;
        $ans = [];
        while(true){
            for($i=$left;$i<=$right;$i++){
                array_push($ans,$matrix[$up][$i]);
            }
            $up++;
            if($up>$down) break;

            for($i=$up;$i<=$down;$i++){
                array_push($ans,$matrix[$i][$right]);
            }
            $right--;
            if($right<$left) break;

            for($i=$right;$i>=$left;$i--){
                array_push($ans,$matrix[$down][$i]);
            }
            $down--;
            if($down<$up) break;

            for($i=$down;$i>=$up;$i--){
                array_push($ans,$matrix[$i][$left]);
            }
            $left++;
            if($left>$right) break;
        }
        return $ans;
    }
}
```

