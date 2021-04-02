---
title: Leecode-查找常用字符
categories: Leecode
---

![WechatIMG582.jpeg](https://upload-images.jianshu.io/upload_images/15325592-2360f495698eec05.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1002题：[查找常用字符](https://leetcode-cn.com/problems/find-common-characters/)
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
示例：
输入：["bella","label","roller"]
输出：["e","l","l"]

#  解题方法

> 哈希表
[参照题解](https://leetcode-cn.com/problems/find-common-characters/solution/cha-zhao-chang-yong-zi-fu-by-leetcode-solution/)

- 解题思路

> 由于数组`A`中的字符串只包含小写字母
先统计26个小写字母中，每个字母`c`在所有字符串中最小出现的次数`minfreq[c]`，初始为无限大
遍历`A`中的每个字符串`word`，使用`freq[c]`统计每个字母`c`在当前`word`中出现的次数`freq[c]`
统计完成后，对于每个`c`在每个`word`中出现的次数`freq[c]`，一定不小于它在所有字符串中出现的次数`minfreq[c]`
所以将每个`minfreq[c]`与`freq[c]`做比较取最小值
最终将`minfreq`中**每个字母乘以它出现的次数**依次存入列表`ans`返回

- 复杂度

> 时间复杂度：O(m(n+Z))，m为数组A的长度，n为字符串的平均长度，Z为小写字母的长度
空间复杂度：0(Z)，Z为小写字母的长度

- 代码实现

> python3

```
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        minfreq = [float('inf')]*26
        for word in A:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i],freq[i])
        ans = []
        for i in range(26):
            ans.extend([chr(i+ord('a'))]*minfreq[i])
        return ans
```

> php

```
class Solution {
    function commonChars($A) {
        $minfreq = array_fill(0,26,INF);
        foreach($A as $word){
            $freq = array_fill(0,26,0);
            for($i=0;$i<strlen($word);$i++){
                $c = $word[$i];
                $freq[ord($c)-ord('a')]++;
            }
            for($i=0;$i<26;$i++){
                $minfreq[$i] = min($minfreq[$i],$freq[$i]);
            }
        }
        $ans = [];
        for($i=0;$i<26;$i++){
            if($minfreq[$i]){
                foreach(array_fill(0,$minfreq[$i],chr($i+ord('a'))) as $v){
                    array_push($ans,$v);
                }
            }
        }
        return $ans;
    }
}
```
