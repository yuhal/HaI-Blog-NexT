---
title: Leecode-转置矩阵
categories: Leecode
---
![5171614317535_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-427db0f20c8beb7d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第867题：[转置矩阵](https://leetcode-cn.com/problems/transpose-matrix/)
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
![hint_transpose.png](https://upload-images.jianshu.io/upload_images/15325592-bd70ae3f7e9d2daf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
示例：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]

#  解题方法

> 暴力法
[原址题解](https://leetcode-cn.com/problems/transpose-matrix/solution/zhuan-zhi-ju-zhen-by-yohannzhang-wtkn/)

- 解题思路

> 定义m和n分别存储矩阵matrix的行数和列数
创建数组tmatrix，存储转置后的矩阵
在[0,n)和[0,m)区间中嵌套遍历matrix
根据转置的规则对tmatrix每个元素赋值

- 复杂度

> 时间复杂度：O(mn)，m和n分别是矩阵matrix的行数和列数
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        tmatrix = [0]*n
        for i in range(n):
            tmatrix[i] = [0]*m
            for j in range(m): 
                tmatrix[i][j] = matrix[j][i]
        return tmatrix
```

> php

```
class Solution {
    function transpose($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $tmatrix = [];
        for($i=0;$i<$n;$i++){
            $tmatrix[$i] = [];
            for($j=0;$j<$m;$j++){
                $tmatrix[$i][$j] = $matrix[$j][$i];
            }
        }
        return $tmatrix;
    }
}
```


