---
title: Leecode-长度最小的子数组
categories: Leecode
---

![5201614317622_.pic.jpg](https://upload-images.jianshu.io/upload_images/15325592-292b5d01c7d464bf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第209题：[长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
示例：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

#  解题方法
> 滑动窗口
[参照题解](https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/)

- 解题思路
> 定义n存储数组nums的长度
定义左右指针left和right，初始都为0
定义sumN统计每组子数组的和，初始为0
为求得最小子数组的长度minl，先赋值一个比n要大的数n+1
当right<n时，将right对应数值累加到sumN，并右移right
当sumN>=正整数target时，计算此时子数组的长度，与minl相比取最小值
然后将left对应数值从sumN中减去，并右移left
若最终得到的minl与初始值相等，说明不存在符合条件的子数组，返回0
反之，返回minl

- 复杂度

> 时间复杂度：O(n)，n是数组的长度
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = sumN = 0
        minl = n+1
        while right<n:
            sumN += nums[right]
            right += 1
            while sumN>=target:
                minl = min(minl,right-left)
                sumN -= nums[left]
                left += 1
        return 0 if minl==n+1 else minl
```

> php

```
class Solution {
    function minSubArrayLen($target, $nums) {
        $n = count($nums);
        $left = $right = $sumN = 0;
        $minl = $n+1;
        while($right<$n){
            $sumN += $nums[$right];
            while($sumN>=$target){
                $minl = min($minl,$right-$left+1);
                $sumN -= $nums[$left];
                $left++;
            }
            $right++;
        }
        if($minl==$n+1){
            return 0;
        }else{
            return $minl;
        }
    }
}
```

- 文字草稿

> target = 7
nums = [2,3,1,2,4,3]
第1组连续子数组和为2=2，out
第2组连续子数组和为5=2+3，out
第3组连续子数组和为6=2+3+1，out
第4组连续子数组和为8=2+3+1+2，长度为4
第5组连续子数组和为10=3+1+2+4，长度为4
第6组连续子数组和为10=1+2+4+3，长度为4
第7组连续子数组和为9=2+4+3，长度为3
第8组连续子数组和为7=4+3，长度为2
最小子数组的长度为2
