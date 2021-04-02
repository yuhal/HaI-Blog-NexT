---
title: Leecode-搜索二维矩阵
categories: Leecode
---
#  题目描述

> leecode第74题：[搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例：
![mat.jpeg](https://upload-images.jianshu.io/upload_images/15325592-82f2a0c011db1ba7.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

![WechatIMG615.png](https://upload-images.jianshu.io/upload_images/15325592-74be4869d8f04034.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  解题方法

> 暴力法
[原址题解](https://leetcode-cn.com/problems/search-a-2d-matrix/solution/sou-suo-er-wei-ju-zhen-by-yohannzhang-vvql/)

- 解题思路

> 遍历二维矩阵`matrix`的每个元素
查找`target`是否存在

- 复杂度

> 时间复杂度： O(mn)
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for v in matrix:
            if target in v:
                return True
        return False
```

> php

```
class Solution {
    function searchMatrix($matrix, $target) {
        foreach($matrix as $v){
            if(in_array($target,$v)){
                return true;
            }
        }
        return false;
    }
}
```

