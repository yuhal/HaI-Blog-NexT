---
title: Leecode-二维区域和检索---矩阵不可变
categories: Leecode
---
![WechatIMG544.jpeg](https://upload-images.jianshu.io/upload_images/15325592-34385163c53ce58c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第304题：[二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
![304.png](https://upload-images.jianshu.io/upload_images/15325592-fed6b2fc34f5816e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
示例：
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

#  解题方法

> 前缀和
[原址题解](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/er-wei-qu-yu-he-jian-suo-ju-zhen-bu-ke-b-msox/)

- 解题思路

> 定义m和n分别表示二维矩阵matrix行和列
定义二维矩阵preSums，preSums[i][j]赋初始值为0，行和列的长度分别为m+1和n+1
在[i,m)[j,n)范围内嵌套遍历matrix，计算从[0,0]到[i,j]坐标内所有元素之和
每次调用sumRegion，即要求从[row1,col1]到[row2,col2]坐标内所有元素之和
参照下面的图解：
![WechatIMG543.png](https://upload-images.jianshu.io/upload_images/15325592-37054254551fe8cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
所要求得黄色区域元素和=黑色-蓝色-绿色+红色
得出公式：
sumRegion=preSums[row2+1][col2+1]-preSums[row1][col2+1]-preSums[row2+1][col1]+preSums[row1][col1]

- 复杂度

> 时间复杂度：初始化为O(mn)，m和n是二维矩阵preSums的行和列，每次调用是O(1)
空间复杂度：O(mn)

- 代码实现

> python3

```
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix),(len(matrix[0]) if matrix else 0)
        self.preSums = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.preSums[i+1][j+1] = self.preSums[i][j+1]+self.preSums[i+1][j]-self.preSums[i][j]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSums[row2+1][col2+1]-self.preSums[row1][col2+1]-self.preSums[row2+1][col1]+self.preSums[row1][col1]
```

> php

```
class NumMatrix {
    function __construct($matrix) {
        $m = count($matrix);
        $n = count($matrix[0]);
        $this->preSums = [];
        for($i=0;$i<$m;$i++){
            for($j=0;$j<$n;$j++){
                $this->preSums[$i+1][$j+1] = $this->preSums[$i][$j+1]+$this->preSums[$i+1][$j]-$this->preSums[$i][$j]+$matrix[$i][$j];
            }
        }
    }
    
    function sumRegion($row1, $col1, $row2, $col2) {
        return $this->preSums[$row2+1][$col2+1]-$this->preSums[$row1][$col2+1]-$this->preSums[$row2+1][$col1]+$this->preSums[$row1][$col1];
    }
}
```

