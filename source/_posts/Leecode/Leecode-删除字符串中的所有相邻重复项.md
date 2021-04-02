---
title: Leecode-删除字符串中的所有相邻重复项
categories: Leecode
---

![WechatIMG577.jpeg](https://upload-images.jianshu.io/upload_images/15325592-d1515a0c4ac8adf8.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1047题：[删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

#  解题方法

> 栈
[原址题解](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/shan-chu-zi-fu-chuan-zhong-de-suo-you-xi-vshc/)

- 解题思路

> 这个题目可以理解为“俄罗斯方块”或者“消消乐”
把字符串逐个压栈，相同的字符抵消，最后剩余的就是答案

- 复杂度

> 时间复杂度：O(n)，n是字符串S的长度
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        n = len(S)
        for i in range(n):
            if stack and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return "".join(stack)
```

> php

```
class Solution {
    function removeDuplicates($S) {
        $stack = [];
        $n = strlen($S);
        for($i=0;$i<$n;$i++){
            if($stack && end($stack)==$S[$i]){
                array_pop($stack);
            }else{
                array_push($stack,$S[$i]);
            }
        }
        return implode("",$stack);
    }
}
```

- 文字草稿

> S = "abbaca"
第1个字符入栈，['a']
第2个字符入栈，['a','b']
第3个字符入栈，['a','b','b']，字符b被抵消，剩余['a']
第4个字符入栈，['a','a']，字符a被抵消，剩余[]
第5个字符入栈，['c']
第6个字符入栈，['c','a']
即最后的字符串为ca





