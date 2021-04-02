---
title: Leecode-字符流
categories: Leecode
---



![WechatIMG553.jpeg](https://upload-images.jianshu.io/upload_images/15325592-f13b92a0b7ed907e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  题目描述

> leecode第1032题：[字符流](https://leetcode-cn.com/problems/stream-of-characters/)
按下述要求实现 StreamChecker 类：
StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，包括刚刚查询的字母）拼写出给定字词表中的某一字词时，返回 true。否则，返回 false。
示例：
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // 初始化字典
streamChecker.query('a');          // 返回 false
streamChecker.query('b');          // 返回 false
streamChecker.query('c');          // 返回 false
streamChecker.query('d');          // 返回 true，因为 'cd' 在字词表中
streamChecker.query('e');          // 返回 false
streamChecker.query('f');          // 返回 true，因为 'f' 在字词表中
streamChecker.query('g');          // 返回 false
streamChecker.query('h');          // 返回 false
streamChecker.query('i');          // 返回 false
streamChecker.query('j');          // 返回 false
streamChecker.query('k');          // 返回 false
streamChecker.query('l');          // 返回 true，因为 'kl' 在字词表中。

#  解题方法

> 字典树
部分代码语言可能存在超时
[参照题解](https://leetcode-cn.com/problems/stream-of-characters/solution/tong-su-yi-dong-trie1032-zi-fu-liu-by-fe-lucifer/)

- 解题思路

> 构建字典树root，创建双向队列stream
遍历数组words，将每个单词word反转后存入root
每次query时，向stream的左侧插入letter
遍历stream，在root中查询每次输入的letter是否存在

- 复杂度

> 时间复杂度：O(n)
空间复杂度：O(n)

- 代码实现

> python3

```
class Trie:
    def __init__(self):
        self.next = {}
        self.isWrod = False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Trie()
        self.stream = deque([])
        for word in words:
            self.addWord(word)
    
    def addWord(self, word):
        tree = self.root
        for c in word[::-1]:
            if c not in tree.next:
                tree.next[c] = Trie()
            tree = tree.next[c]
        if not tree.isWrod:
            tree.isWrod = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        tree = self.root
        for c in self.stream:
            if c not in tree.next:
                return False
            tree = tree.next[c]
            if tree.isWrod:
                return True
        return False
```

> php

```
class Trie {
    public $next = [];
    public $isWord = false;
}
class StreamChecker {
    function __construct($words) {
        $this->root = new Trie();
        $this->stream = [];
        array_map([$this,'addWord'],$words);
    }

    function addWord($word){
        $word = strrev($word);
        $tree = $this->root;
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            if(!isset($tree->next[$c])){
                $tree->next[$c] = new Trie();
            }
            $tree = $tree->next[$c];
        }
        if(!$tree->isWord){
            $tree->isWord = true;
        }
    }
  
    function query($letter) {
        array_unshift($this->stream,$letter);
        print_r($this->stream);
        $tree = $this->root;
        foreach($this->stream as $c){
            if(!isset($tree->next[$c])){
                return false;
            }
            $tree = $tree->next[$c];
            if($tree->isWord){
                return true;
            }
        }
        return false;
    }
}
```
