---
title: Leecode-托普利茨矩阵
categories: Leecode
---

![WechatIMG503.jpeg](https://upload-images.jianshu.io/upload_images/15325592-016a82de4d2b8893.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第766题：[托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix/)
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
示例：
![ex1.jpg](https://upload-images.jianshu.io/upload_images/15325592-d6031905e962fde2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为: 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 
各条对角线上的所有元素均相同, 因此答案是 True 。

#  解题方法

> 遍历
[原址题解](https://leetcode-cn.com/problems/toeplitz-matrix/solution/tuo-pu-li-ci-ju-zhen-by-yohannzhang-ykl3/)

- 解题思路

> 定义m，n分别存储矩阵matrix的行数和列数
在[0,m-1)区间遍历matrix
判断当前行去掉最后一个元素和下一行去掉第一个元素是否相等，不等返回false
遍历完成后，返回true

- 复杂度

> 时间复杂度：O(m-1)，m为矩阵matrix的行数。
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        if m == 1: return True
        for i in range(m-1):
            if matrix[i][:(n-1)] != matrix[i+1][1:]:
                return False
        return True
```

> php

```
class Solution {
    function isToeplitzMatrix($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        if($m==0) return true;
        for($i=0;$i<$m-1;$i++){
            if(array_slice($matrix[$i],0,$n-1)!=array_slice($matrix[$i+1],1)){
                return false;
            }
        }
        return true;
    }
}
```

- 文字草稿

> matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
第1次遍历，第1行去掉最后一个元素：[1,2,3]，第2行去掉第一个元素：[1,2,3]
第2次遍历，第2行去掉最后一个元素：[5,1,2]，第3行去掉第一个元素：[5,1,2]
遍历完成，该矩阵是托普利茨矩阵
