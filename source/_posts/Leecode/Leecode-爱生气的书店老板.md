---
title: Leecode-爱生气的书店老板
categories: Leecode
---
![WechatIMG511.jpeg](https://upload-images.jianshu.io/upload_images/15325592-286af0906d981c98.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->


#  题目描述

> leecode第1052题：[爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
示例：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

#  解题方法

> 滑动窗口
[原址题解](https://leetcode-cn.com/problems/grumpy-bookstore-owner/solution/ai-sheng-qi-de-shu-dian-lao-ban-by-yohan-y6rm/)

- 解题思路

> 定义n存储数组customers的长度，它与数组grumpy的长度相等
枚举遍历customers
当老板不生气时，统计顾客满意的总数sumC，并把原数组对应顾客数清零
当遍历索引小于[秘密技巧X]时，统计第一组分钟内顾客满意的总数total
遍历完成后，先认为total就是某一组分钟内顾客满意的最大总数maxTotal
在[X,n)区间遍历customers，计算每次移动分钟后的值total，与maxTotal相比较取最大值
遍历完成后，感到满意的最大客户数量即为maxTotal+sumC

- 代码实现

> python3

```
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        maxTotal = total = sumC = 0
        for i,customer in enumerate(customers):
            if grumpy[i]==0:
                sumC += customer
                customers[i] = 0
            elif i<X:
                total += customer
        maxTotal = total
        for i in range(X,n):
            total += customers[i]-customers[i-X]
            maxTotal = max(maxTotal,total)
        return maxTotal+sumC
```

> php

```
class Solution {
    function maxSatisfied($customers, $grumpy, $X) {
        $n = count($customers);
        $maxTotal = $total = $sumC = 0;
        foreach($customers as $i=>$customer){
            if($grumpy[$i]==0){
                $sum+=$customer;
                $customers[$i] = 0;
            }elseif($i<$X){
                $total+=$customer;
            }
        }
        $maxTotal = $total;
        for($i=$X;$i<$n;$i++){
            $total += $customers[$i]-$customers[$i-$X];
            $maxTotal = max($maxTotal,$total);
        }
        return $maxTotal+$sum;
    }
}
```

- 文字草稿
> customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
当老板不生气时，感到满意的客户数量为1+1+1+7=10
使用秘密技巧时，
第1组分钟内能让顾客满意的数量增加0=0+0+0
第2组分钟内能让顾客满意的数量增加2=0+0+2
第3组分钟内能让顾客满意的数量增加2=0+2+0
第4组分钟内能让顾客满意的数量增加3=2+0+1
第5组分钟内能让顾客满意的数量增加1=0+0+1
第6组分钟内能让顾客满意的数量增加6=1+0+5
最终感到满意的最大客户数量为10+6=16

