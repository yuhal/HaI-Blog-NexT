---
title: Leecode-单词的压缩编码
categories: Leecode
---
![WechatIMG573.jpeg](https://upload-images.jianshu.io/upload_images/15325592-1f539b64f28dce90.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  题目描述

> leecode第820题：[单词的压缩编码](https://leetcode-cn.com/problems/short-encoding-of-words/)
单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：
words.length == indices.length
助记字符串 s 以 '# ' 字符结尾
对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '# ' 字符结束（但不包括 '# '）的 子字符串 恰好与 words[i] 相等
给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。
示例：
输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time# bell# " 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '# ' 结束的子字符串，如加粗部分所示 "time# bell# "
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '# ' 结束的子字符串，如加粗部分所示 "time# bell# "
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '# ' 结束的子字符串，如加粗部分所示 "time# bell# "

#  解题方法一

> 字典树
[原址题解](https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-yohannzhang-mone/)

- 解题思路

> 构建字典树root
遍历单词数组words，将每个单词反转后存入root，构建后缀树
记录最小助记单词的长度minl
二次遍历words，查找一个单词是否存在于root
若存在时，minl累加当前单词的长度

- 复杂度

> 时间复杂度：O(n)，n为单词数组words中的总字符数
空间复杂度：O(n)

- 代码实现

> python3

```
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = {}
        def addWord(word):
            tree = root
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
        def search(word):
            tree = root
            for c in word:
                tree = tree[c]
            return len(tree) == 0
        words = set(words)
        for word in words:
            addWord(word[::-1])
        minl = 0
        for word in words:
            if search(word[::-1]):
                minl += len(word)+1
        return minl
```

> php

```
class Trie {
    public $next = [];
}
class Solution {
    function minimumLengthEncoding($words) {
        $this->root = new Trie();
        $words = array_unique($words);
        array_map([$this,'addWord'],$words);
        $minl = 0;
        foreach($words as $word){
            if($this->search($word)){
                $minl += strlen($word) + 1;
            }
        }
        return $minl;
    }

    function search($word){
        $tree = $this->root;
        $word = strrev($word);
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            $tree = $tree->next[$c];
        }
        return count($tree->next) == 0;
    }

    function addWord($word){
        $tree = $this->root;
        $word = strrev($word);
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            if(!isset($tree->next[$c])){
                $tree->next[$c] = new Trie();
            }
            $tree = $tree->next[$c];
        }
    }
}
```



#  解题方法二

> 哈希表
[参照题解](https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-leetcode-solution/)

- 解题思路

> 将单词数组words存入哈希表hashW
遍历words，如果words存在单词word1是word2的后缀，那么word2就不用考虑
所以我们从下标为1的位置循环截取word
当截取的单词是否存在于hashW时，就从hashW中删除单词
遍历完成后，计算一下hashW剩余的单词字符个数
对于hashW剩余的每个单词，还需计算助记字符'# '的个数

- 复杂度

> 时间复杂度：O(n^2)
空间复杂度：o(n)

- 代码实现

> python3

```
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        hashW = set(words)
        for word in words:
            for i in range(1,len(word)):
                if word[i:] in hashW:
                    hashW.discard(word[i:])
        return sum(len(word)+1 for word in hashW)
```

> php

```
class Solution {
    function minimumLengthEncoding($words) {
        $hashW = array_unique($words);
        foreach($words as $word){
            for($i=1;$i<strlen($word);$i++){
                $c = substr($word,$i);
                if(in_array($c,$hashW)){
                    $hashW = array_diff($hashW,[$c]);
                }
            }
        }
        $minl = 0;
        foreach($hashW as $word){
            $minl += strlen($word)+1;
        }
        return $minl;
    }
}
```

