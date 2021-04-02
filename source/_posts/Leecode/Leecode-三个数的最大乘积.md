---
title: Leecode-三个数的最大乘积
categories: Leecode
---
![5191614317615_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-f5d59ef8de1364ec.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第628题：[三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers/)
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
示例：
输入：nums = [-100,-2,-3,1]
输出：300

#  解题方法

> 排序
[参照题解](https://leetcode-cn.com/problems/maximum-product-of-three-numbers/solution/san-ge-shu-de-zui-da-cheng-ji-by-leetcod-t9sb/)

- 解题思路

>将数组由小到大排序
求数组中三个最大数的乘积
求数组中两个最小数和一个最大数的乘积
最后求得三个数的最大乘积

- 复杂度

> 时间复杂度：O(nlogn)，n为数组长度
空间复杂度：O(logn)

- 代码实现

> python3

```
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
```

> php

```
class Solution {
    function maximumProduct($nums) {
        $n = count($nums);
        asort($nums);
        $nums = array_values($nums);
        return max($nums[$n-1]*$nums[$n-2]*$nums[$n-3],$nums[0]*$nums[1]*$nums[$n-1]);
    }
}
```

- 文字草稿

> nums = [-100,-2,-3,1]
正序排列后得到[-100,-3,-2,1]
最大三个最大数的乘积为6=(-3)*(-2)*1
两个最小数和一个最大数的乘积为300=(-100)*(-3)*1
三个数的最大乘积即为300
