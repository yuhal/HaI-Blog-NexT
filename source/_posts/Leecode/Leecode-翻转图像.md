---
title: Leecode-翻转图像
categories: Leecode
---
![5161614317530_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-d04a8b4d1b2e35f8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第832题：[翻转图像](https://leetcode-cn.com/problems/flipping-an-image/)
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
示例：
输入：[[1,1,0],[1,0,1],[0,0,0]]
输出：[[1,0,0],[0,1,0],[1,1,1]]
解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]

#  解题方法

> 暴力法
[原址题解](https://leetcode-cn.com/problems/flipping-an-image/solution/fan-zhuan-tu-xiang-by-yohannzhang-xopc/)

- 解题思路

> 遍历矩阵A
先对矩阵中每个行做翻转
再对行中的每个元素进行替换

- 复杂度

> 时间复杂度：O(n^2)，n是矩阵A的行数和列数
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def replace(n):
            if n==0:
                return 1
            return 0
        for i,a in enumerate(A):
            A[i] = list(map(replace,a[::-1]))
```

> php

```
class Solution {
    function flipAndInvertImage($A) {
        foreach($A as $i=>$a){
            krsort($a);
            $A[$i] = array_map([$this,'replace'],$a);
        }
        return $A;
    }

    function replace($n){
        if($n===0){
            return 1;
        }
        return 0;
    }
}
```

