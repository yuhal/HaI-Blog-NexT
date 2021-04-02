---
title: Leecode-数组的度
categories: Leecode
---
![5021613804894_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-a0f67c816c5bc47e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第697题：[数组的度](https://leetcode-cn.com/problems/degree-of-an-array/)
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
示例：
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2。
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

#  解题方法

> 哈希表
[参照题解](https://leetcode-cn.com/problems/degree-of-an-array/solution/shu-zu-de-du-by-leetcode-solution-ig97/)

- 解题思路

> 创建哈希表unums
枚举遍历数组nums，记录每一个元素出现的次数、起始位置，并存入unums
记录完所有信息后，遍历unums，找到起始位置相差最短的长度

- 复杂度

> 时间复杂度：O(n)，n是数组nums的长度
空间复杂度：O(n)，n是数组nums的长度

- 代码实现

> python3

```
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        unums = {}
        for i,num in enumerate(nums):
            if num in unums:
                unums[num][0] += 1
                unums[num][2] = i
            else:
                unums[num] = [1,i,i]
        maxn = minl = 0
        for count,left,right in unums.values():
            if maxn<count:
                maxn = count
                minl = right-left+1
            elif maxn==count:
                minl = min(minl,right-left+1)
        return minl
```

> php

```
class Solution {
    function findShortestSubArray($nums) {
        $unums = [];
        foreach($nums as $i=>$num){
            if(in_array($num,array_keys($unums))){
                $unums[$num][0]++;
                $unums[$num][2] = $i;
            }else{
                $unums[$num] = [1,$i,$i];
            }
        }
        $maxn = $minl = 0;
        foreach(array_values($unums) as [$count,$left,$right]){
            if($maxn<$count){
                $maxn = $count;
                $minl = $right-$left+1;
            }elseif($maxn==$count){
                $minl = min($minl,$right-$left+1);
            }
        }
        return $minl;
    }
}
```

- 文字草稿

> nums = [1, 2, 2, 3, 1]
元素1出现2次，起始位置为0和4，相差长度为5，out
元素2出现2次，起始位置为1和2，相差长度为2，pass
元素3出现1次，out
最短连续子数组的长度为2
