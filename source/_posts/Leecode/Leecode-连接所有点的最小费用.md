---
title: Leecode-连接所有点的最小费用
categories: Leecode
---
![WechatIMG522.jpeg](https://upload-images.jianshu.io/upload_images/15325592-3e0c47679b2fdbf0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1584题：[连接所有点的最小费用](https://leetcode-cn.com/problems/min-cost-to-connect-all-points/)
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
示例：
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
[图片上传失败...(image-e0024b-1614563688539)]
输出：20
解释：
[图片上传失败...(image-5673f3-1614563688540)]
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

#  解题方法

> 贪心算法
[参照题解](https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/python-ji-yu-bao-po-de-you-hua-si-lu-jian-dan-shi-/)

- 解题思路

> 定义连接所有点的最小费用cost初始为0
创建数组p2v，每个点的坐标值作为k，剩余点上次计算距离的最小值作为v，初始为0
创建数组done记录每次经过的点，第一个点默认被记录
循环p2v，每次迭代，更新p2v中每个点对应剩余点上次计算距离的最小值
把更新后的p2v中，获取距离最小的点point及两点之间的最小距离dist
将point添加到done中并从p2v中移除，然后cost累加dist
最终返回cost作为连接所有点的最小费用

- 复杂度

> 时间复杂度：O(n^2)
空间复杂度：O(n)

- 代码实现

> python3

```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        p2v = {(x,y):math.inf for x,y in points}
        done = [p2v.popitem()[0]]
        while p2v:
            for point,value in p2v.items():
                x,y = point
                i,j = done[-1]
                dist = abs(x-i)+abs(y-j)
                p2v[point] = min(value,dist)
            dist,point = min((j,i) for i,j in p2v.items())
            done.append(point)
            del(p2v[point])
            cost += dist
        return cost
```

> php

```
class Solution {
    function minCostConnectPoints($points) {
        $cost = 0;
        $p2v = [];
        foreach($points as $v){
            array_push($p2v,[$v,INF]);
        }
        $done = [array_pop($p2v)[0]];
        $minp2v = function($p2v){
            $arr = [];
            foreach($p2v as [$i,$j]){
                array_push($arr,[$j,$i]);
            }
            return min($arr);
        };
        $delp2v = function($p2v,$point){
            foreach($p2v as $key => [$i,$j]){
                if($i==$point) unset($p2v[$key]);
            }
            return $p2v;
        };
        while($p2v){
            foreach($p2v as $key => [$point,$value]){
                list($x,$y) = $point;
                list($i,$j) = end($done);
                $dist = abs($x-$i)+abs($y-$j);
                $p2v[$key][1] = min($value,$dist);
            }
            list($dist,$point) = $minp2v($p2v);
            array_push($done,$point);
            $p2v = $delp2v($p2v,$point);
            $cost += $dist;
        }
        return $cost;
    }
}
```
