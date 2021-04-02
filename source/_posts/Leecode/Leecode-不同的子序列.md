---
title: Leecode-不同的子序列
categories: Leecode
---
![WechatIMG589.jpeg](https://upload-images.jianshu.io/upload_images/15325592-2f71cc394dcc131a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第115题：[不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/)
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。
示例：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

#  解题方法

> 动态规划
[参照题解](https://leetcode-cn.com/problems/distinct-subsequences/solution/bu-tong-de-zi-xu-lie-by-leetcode-solutio-urw3/)

- 状态转移方程

> `s[i] == s[j]` dp[i][j] = dp[i+1][j+1]+dp[i+1][j]
`s[i] != s[j]` dp[i][j] = dp[i+1][j]

- 临界条件

> dp[i][n] = 0

- 枚举状态

> dp[i][j]

- 解题思路

> 获取字符串`s`和`t`的长度分别的`m`和`n`
如果`m<n`，表示`t`一定不是`s`的子序列，直接返回0
接下来使用动态规划来计算`s`的子序列`t`出现的个数
创建二维数组`dp`，元素值都为0，考虑到边界，`dp`的行数和列数分别为`m+1`和`n+1`
`dp[i][j]`表示`s`中后`i`个字符串可以由`t`中后`j`个字符串组成的最多个数
当`j=n`时，`t[j:]`为空字符串，此时`s`中任何`s[i:]`都可以由`t[j]`组成，所以`dp[i][n]=1`
接着在`[m-1,-1)`和`[n-1,-1]`中倒序遍历
根据状态转移方程，当`s[i]`等于`t[j]`时，`dp[i][j]=dp[i+1][j+1]+dp[i+1][j]`
反之，`dp[i][j]=dp[i+1][j]`
最终得到`dp[0][0]`就是在`s`的子序列中`t`出现的个数

- 图解

![不同的子序列.jpg](https://upload-images.jianshu.io/upload_images/15325592-6f1aa99dc3d39715.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

- 复杂度
> 时间复杂度：O(mn)，m和n分别是字符串s和t的长度
空间复杂度：O(mn)，m和n分别是字符串s和t的长度

- 代码实现

> python3

```
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        if m<n:
            return 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j] = dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
```

> php

```
class Solution {
    function numDistinct($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        if($m<$n){
            return 0;
        }
        $dp = array_fill(0,$m+1,array_fill(0,$n+1,0));
        for($i=0;$i<=$m;$i++){
            $dp[$i][$n] = 1;
        }
        for($i=$m-1;$i>=0;$i--){
            for($j=$n-1;$j>=0;$j--){
                if($s[$i]==$t[$j]){
                    $dp[$i][$j] = $dp[$i+1][$j+1]+$dp[$i+1][$j];
                }else{
                    $dp[$i][$j] = $dp[$i+1][$j];
                }
            }               
        }
        return $dp[0][0];
    }
}
```
