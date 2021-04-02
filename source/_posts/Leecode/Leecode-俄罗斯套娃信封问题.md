---
title: Leecode-俄罗斯套娃信封问题
categories: Leecode
---
![WechatIMG550.jpeg](https://upload-images.jianshu.io/upload_images/15325592-5a67a0dfcb231e50.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第354题：[俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/)
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
说明:
不允许旋转信封。
示例:
输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3 
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

#  解题方法

> 动态规划
[参照题解](https://leetcode-cn.com/problems/russian-doll-envelopes/solution/liang-ge-wei-du-de-zui-chang-di-zeng-zi-ctbmd/)

- 解题思路

> 先对数组envelopes进行第一维(信封的高度)递增，(信封的宽度)递减的排序
定义n获取envelopes的长度
定义长度为n的数组dp，假如最多能有1个信封，初始化都为1
在[i,n)和[j,i)中嵌套循环
当前一个信封的宽度是否小于后一个信封的宽度时
每轮迭代，累加信封的数量并取最大值dp[i]
最后返回所有轮中最大的信封的数量

- 复杂度

>时间复杂度：O(N^2) 
空间复杂度：O(N)

- 代码实现

> python3

```
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        n = len(envelopes)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
```

> php

```
class Solution {
    function maxEnvelopes($envelopes) {
        if(!$envelopes){
            return 0;
        }
        usort($envelopes, function ($a, $b) {
            if($a[0]>$b[0]){
                return 1;
            }elseif($a[0]<$b[0]){
                return -1;
            }else{
                return ($a[1]>$b[1]) ? -1 : 1;
            }
        });
        $n = count($envelopes);
        $dp = array_fill(0,$n,1);
        for($i=0;$i<$n;$i++){
            for($j=0;$j<$i;$j++){
                if($envelopes[$j][1]<$envelopes[$i][1]){
                    $dp[$i] = max($dp[$i],$dp[$j]+1);
                }
            }
        }
        return max($dp);
    }
}
```

