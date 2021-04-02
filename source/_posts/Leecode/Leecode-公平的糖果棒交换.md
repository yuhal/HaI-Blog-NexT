---
title: Leecode-公平的糖果棒交换
categories: Leecode
---

![5011613804888_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-fd9586a2325162e2.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第888题：[公平的糖果棒交换](https://leetcode-cn.com/problems/fair-candy-swap/)
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。
因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
如果有多个答案，你可以返回其中任何一个。保证答案存在。
示例：
输入：A = [1,2,5], B = [2,4]
输出：[5,4]

#  解题方法

> 哈希表
[参照题解](https://leetcode-cn.com/problems/fair-candy-swap/solution/gong-ping-de-tang-guo-jiao-huan-by-leetc-tlam/)

- 解题思路

> 可以理解为两个数组交换一个元素后，数组元素总和相等
计算数组A元素总和为sumA
计算数组B元素总和为sumB
设A和B各自交换的元素大小为x和y，即sumA−x+y=sumB+x−y，化简得x=y+(sumA-sumB)/2
将A存于哈希表hashA，避免重复查找。对于B中存在的y，在hashA中找到对应的x即可

- 复杂度

> 时间复杂度：O(n+m)，n是数组A的长度，m是数组B的长度
空间复杂度：O(n)，n是数组A的长度

- 代码实现

> python3

```
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA,sumB = sum(A),sum(B)
        hashA = set(A)
        ans = []
        for y in B:
            x = y+(sumA-sumB)//2
            if x in hashA:
                ans = [x,y]
        return ans
```

> php

```
class Solution {
    function fairCandySwap($A, $B) {
        $sumA = array_sum($A);
        $sumB = array_sum($B);
        $hashA = array_unique($A);
        $ans = [];
        foreach($B as $y){
            $x = $y+($sumA-$sumB)/2;
            if(in_array($x,$hashA)){
                $ans = [$x,$y];
            }
        }
        return $ans;
    }
}
```

- 文字草稿

> A = [1,2,5]
B = [2,4]
爱丽丝糖果棒的总大小为8
鲍勃糖果棒的总大小为6
把爱丽丝相同大小的糖果棒进行去重，得到[1,2,5]
第1轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为1和2，交换后分别为[2,2,5]和[1,4]，out
第2轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为1和4，交换后分别为[4,2,5]和[1,4]，out
第3轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为2和2，交换后分别为[2,2,5]和[2,4]，out
第4轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为2和4，交换后分别为[4,2,5]和[2,4]，out
第5轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为5和2，交换后分别为[1,2,2]和[5,4]，out
第6轮交换，爱丽丝和鲍勃交换糖果棒的大小分别为5和4，交换后分别为[1,2,4]和[2,5]，pass
爱丽丝和鲍勃交换糖果棒的大小分别为5和4


