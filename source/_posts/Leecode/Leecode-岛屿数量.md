---
title: Leecode-岛屿数量
categories: Leecode
---

![WechatIMG580.jpeg](https://upload-images.jianshu.io/upload_images/15325592-f43ac46a14c58eaf.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第200题：[岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

#  解题方法

> DFS
[参照题解](https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/)

- 解题思路

> 题中的岛屿`grid`是由二维网格组成的，也就是二维矩阵
首先获取`grid`的行数`m`和列数`n`
定义变量`num`，存储岛屿数量，初始为0
在[0,m)和[0,n)区间内嵌套遍历`grid`
如果当前位置`grid[i][j]`是土地，`num`累加1，然后以当前位置开始进行DFS
在DFS过程中，将访问过的土地标为**0**，再对其**上下左右**的位置进行DFS，直至访问不到土地
最后的岛屿数量就是`num`

- 复杂度

> 时间复杂度：O(mn)，m和n分别为岛屿grid的行数和列数。
空间复杂度：O(mn)

- 代码实现

> python3

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(cur_x,cur_y):
            grid[cur_x][cur_y] = 0
            for i,j in [[-1,0],[1,0],[0,-1],[0,1]]:
                next_x,next_y = cur_x+i,cur_y+j
                if 0<=next_x<m and 0<=next_y<n and grid[next_x][next_y]=="1":
                    dfs(next_x,next_y)
        m,n = len(grid),len(grid[0])
        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    num += 1
                    dfs(i,j)
        return num
```

> php

```
class Solution {
    function numIslands($grid) {
        $this->grid = $grid;
        $this->m = count($this->grid);
        $this->n = count($this->grid[0]);
        $num = 0;
        for($i=0;$i<$this->m;$i++){
            for($j=0;$j<$this->n;$j++){
                if($this->grid[$i][$j]=="1"){
                    $num++;
                    $this->dfs($i,$j);
                }
            }
        }
        return $num;
    }

    function dfs($cur_x,$cur_y){
        $this->grid[$cur_x][$cur_y] = 0;
        foreach([[-1,0],[1,0],[0,-1],[0,1]] as [$i,$j]){
            $next_x = $cur_x+$i;
            $next_y = $cur_y+$j;
            if(0<=$next_x && $next_x<$this->m && 0<=$next_y && $next_y<$this->n && $this->grid[$next_x][$next_y]=="1"){
                $this->dfs($next_x,$next_y);
            }
        }
    }
}
```
