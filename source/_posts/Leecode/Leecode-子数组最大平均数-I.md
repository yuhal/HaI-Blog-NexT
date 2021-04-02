---
title: Leecode-子数组最大平均数-I
categories: Leecode
---
![WechatIMG499.jpeg](https://upload-images.jianshu.io/upload_images/15325592-962fcba925e27d02.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第643号题目：[子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i/)
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

#  解题方法

> 滑动窗口
[参照题解](https://leetcode-cn.com/problems/maximum-average-subarray-i/solution/zi-shu-zu-zui-da-ping-jun-shu-i-by-leetc-us1k/)

- 解题思路

> 把每个子数组当作一个滑窗
定义total计算第一个滑窗的值，此时子数组的最大元素和
maxTotal=total
定义n存储nums的长度
在[k,n)区间遍历nums，计算每次移动窗口后的值total，与maxTotal相比较取最大值
遍历完成后，子数组最大平均数即为maxTotal/k

- 复杂度

>时间复杂度：O(n)，n是数组nums的长度
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)
        for i in range(k,n):
            total = total-nums[i-k]+nums[i]
            maxTotal = max(maxTotal,total)
        return maxTotal/k
```

> php

```
class Solution {
    function findMaxAverage($nums, $k) {
        $n = count($nums);
        $maxTotal = $total = array_sum(array_slice($nums,0,$k));
        for($i=$k;$i<$n;$i++){
            $total = $total-$nums[$i-$k]+$nums[$i];
            $maxTotal = max($maxTotal,$total);
        }
        return $maxTotal/$k;
    }
}
```

- 文字草稿

> nums=[1,12,-5,-6,50,3]
k=4
第1个滑窗的值：1+12+(-5)+(-6)=2
第2个滑窗的值：12+(-5)+(-6)+50=51
第3个滑窗的值：(-5)+(-6)+50+3=42
最大平均数：51
