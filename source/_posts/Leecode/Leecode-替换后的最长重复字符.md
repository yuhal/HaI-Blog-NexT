---
title: Leecode-替换后的最长重复字符
categories: Leecode
---

![WechatIMG500.jpeg](https://upload-images.jianshu.io/upload_images/15325592-baa3df48395f462a.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第424题：[替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement/)
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
注意：字符串长度 和 k 不会超过 104。
示例：
输入：s = "AABABBA", k = 1
输出：4
解释：将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。子串 "BBBB" 有最长重复字母, 答案为 4。

#  解题方法

> 双指针+滑动窗口
[参照题解](https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-n6aza/)

- 解题思路

> 定义n存储字符串s的长度
使用一个长度为26的数组freq记录每一个字符出现的次数，初始都为0
定义左指针left和右指针right，初始为0
定义maxn来记录重复字符出现次数的最大值，初始为0
当right<n时，右指针所在字符的次数+1，并与maxn比较取最大值，右指针右移
当左右指针的区间>maxn+k时，左指针所在字符的次数-1，左指针右移
当right=n时，此时左右指针的区间就是重复字母的最长子串的长度

- 复杂度

> 时间复杂度：O(n)，n是字符串s的长度
空间复杂度：O(a)，a是字符串s出现的字符ASCII值的范围

- 代码实现

> python3

```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0]*26
        maxn = left = right = 0
        while right < n:
            freq[ord(s[right])-ord('A')] += 1
            maxn = max(maxn,freq[ord(s[right])-ord('A')])
            right += 1
            if right-left > maxn+k:
                freq[ord(s[left])-ord('A')] -= 1
                left += 1
        return right - left
```

> php

```
class Solution {
    function characterReplacement($s, $k) {
        $n = strlen($s);
        $maxn = $left = $right = 0;
        $freq = array_fill(0,26,0);
        while($right < $n){
            $freq[ord($s[$right])-ord('A')]++;
            $maxn = max($maxn,$freq[ord($s[$right])-ord('A')]);
            $right++;
            if($right-$left > $maxn+$k){
                $freq[ord($s[$left])-ord('A')]--;
                $left++;
            }
        }
        return $right-$left;
    }
}
```

- 文字草稿

> s = "AABABBA"
k = 1
左指针为0，右指针为0，替换前为A，替换后为A，右指针+1
左指针为0，右指针为1，替换前为AA，替换后为AA，右指针+1
左指针为0，右指针为2，替换前为AAB，替换后为AAA，右指针+1
左指针为0，右指针为3，替换前为AABA，替换后为AAAA，右指针+1
左指针为0，右指针为4，替换前为AABAB，替换后为AAAAB，右指针+1，左指针+1
左指针为1，右指针为5，替换前为ABABB，替换后为ABBBB，右指针+1，左指针+1
左指针为2，右指针为6，替换前为BABBA，替换后为BBBBA，遍历完毕
重复字母的最长子串的长度为4
