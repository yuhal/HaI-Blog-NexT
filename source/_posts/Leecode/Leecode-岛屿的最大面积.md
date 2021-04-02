---
title: Leecode-岛屿的最大面积
categories: Leecode
---

![WechatIMG545.jpeg](https://upload-images.jianshu.io/upload_images/15325592-75ff3e428cc0bb65.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第695题：[岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
示例：
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

#  解题方法

> DFS
[参照题解](https://leetcode-cn.com/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/)

- 解题思路

> 定义maxArea表示最大的岛屿面积，初始为0
枚举遍历二维数组grid，DFS访问每一块土地的坐标(cur_x,cur_y)
每次DFS，直到当前访问的坐标是土地，并且在grid范围内
将当前土地的值置为0，并记录岛屿面积area为1
再访问上下左右相邻的坐标(next_x,next_y)
累加area，直到无土地访问，返回当前土地所在的area
遍历过程中，记录每次返回的area并取最大值返回

- 复杂度

> 时间复杂度：O(R×C)，R是给定网格grid中的行数，C是列数
空间复杂度：O(R×C)

- 代码实现

> python3

```
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(cur_x,cur_y):
            if cur_x<0 or cur_y<0 or cur_x==len(grid) or cur_y==len(grid[0]) or grid[cur_x][cur_y]!=1:
                return 0
            grid[cur_x][cur_y] = 0
            area = 1
            for i,j in [[0,1],[0,-1],[-1,0],[1,0]]:
                next_x = cur_x+i
                next_y = cur_y+j
                area += dfs(next_x,next_y)
            return area
        maxArea = 0
        for i,m in enumerate(grid):
            for j,n in enumerate(m):
                maxArea = max(maxArea,dfs(i,j))
        return maxArea
```

> php

```
class Solution {
    function maxAreaOfIsland($grid) {
        $this->grid = $grid;
        $maxArea = 0;
        foreach($this->grid as $i=>$m){
            foreach($m as $j=>$n){
                $maxArea = max($maxArea,$this->dfs($i,$j));
            }
        }
        return $maxArea;
    }

    function dfs($cur_x,$cur_y){
        if($cur_x<0 || $cur_y<0 || $cur_x==count($this->grid) || $cur_y==count($this->grid[0]) || $this->grid[$cur_x][$cur_y]!=1){
            return 0;
        }
        $this->grid[$cur_x][$cur_y] = 0;
        $area = 1;
        foreach([[1,0],[-1,0],[0,1],[0,-1]] as [$i,$j]){
            $next_x = $cur_x+$i;
            $next_y = $cur_y+$j;
            $area += $this->dfs($next_x,$next_y);
        }
        return $area;
    }
}
```
