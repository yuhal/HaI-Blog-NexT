---
title: Leecode-比特位计数
categories: Leecode
---

![WechatIMG549.jpeg](https://upload-images.jianshu.io/upload_images/15325592-88abad1046c5672a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第338题：[比特位计数](https://leetcode-cn.com/problems/counting-bits/)
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
示例:
输入: 5
输出: [0,1,1,2,1,2]

#  解题方法

> 动态规划
[参照题解](https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/)

- 解题思路

> 定义数组dp记录每个数字转二进制数后1的个数
因为0的二进制中，1个数为0，所以dp初始插入0
在[1,num]区间内遍历数字i
每次迭代，dp记录i中二进制数中1的个数
如果i是奇数，那它的二进制数一定比前面那个偶数多一个1
如果i是偶数，那它的二进制数中1的个数一定等于除以2之后的那个数中1的个数
遍历完成后返回dp即可

- 复杂度

> 时间复杂度：O(num)
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1,num+1):
            if i%2==1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp
```

> php

```
class Solution {
    function countBits($num) {
        $dp = [0];
        for($i=1;$i<=$num;$i++){
            if($i%2==1){
                array_push($dp,$dp[$i-1]+1);
            }else{
                array_push($dp,$dp[$i/2]);
            }
        }
        return $dp;
    }
}
```

- 文字草稿

> num=5
偶数0，1出现的次数=0
奇数1，1出现的次数=偶数0中1出现的次数0+1=1
偶数2，1出现的次数=奇数1中1出现的次数1
奇数3，1出现的次数=偶数2中1出现的次数1+1=2
偶数4，1出现的次数=奇数3中1出现的次数1
奇数5，1出现的次数=偶数4中1出现的次数1+1=2
最终返回[0,1,1,2,1,2]
