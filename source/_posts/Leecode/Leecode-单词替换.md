---
title: Leecode-单词替换
categories: Leecode
---
![WechatIMG515.jpeg](https://upload-images.jianshu.io/upload_images/15325592-4f80e54463eac21b.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第648题：[单词替换](https://leetcode-cn.com/problems/replace-words/)
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。
示例：
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

#  解题方法一

> 字典树
[原址题解](https://leetcode-cn.com/problems/replace-words/solution/dan-ci-ti-huan-by-yohannzhang-oq6u/)

- 解题思路

> 创建字典树root
遍历数组dictionary，向root中存储每个单词，构建前缀树
分割字符串sentence，对分割后的每个单词在前缀树中进行查找替换
若存在，返回替换后的单词；若不存在，返回原来的单词
最后将替换的单词列表转为字符串作为结果返回

- 复杂度

> 时间复杂度：O(n)，n是字符串sentence的长度
空间复杂度：O(n)，前缀树的大小

- 代码实现

> python3

```
class Trie:
    def __init__(self):
        self.next={}
        self.word=""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.root = Trie()
        def addWord(word):
            tree = self.root
            for c in word:
                if c not in tree.next:
                    tree.next[c] = Trie()
                tree = tree.next[c]
            tree.word = word
        def replace(word):
            tree = self.root
            for c in word:
                if c not in tree.next:
                    break
                elif tree.next[c].word:
                    return tree.next[c].word
                tree = tree.next[c]
            return word
        for word in dictionary:
            addWord(word)
        return " ".join(map(replace,sentence.split()))
```

> php

```
class Trie{
    public $next=[];
    public $word="";
}

class Solution {
    function replaceWords($dictionary, $sentence) {
        $this->root = new Trie();
        array_map([$this,'addWord'],$dictionary);
        return implode(" ",array_map([$this,'replace'],explode(" ",$sentence)));
    }

    function replace($word){
        $tree = $this->root;
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            if(!isset($tree->next[$c])){
                $tree->next[$c] = new Trie();
                break;
            }elseif($tree->next[$c]->word){
                return $tree->next[$c]->word;
            }
            $tree = $tree->next[$c];
        }
    }
}
```

#  解题方法二

>哈希表
[参照题解](https://leetcode-cn.com/problems/replace-words/solution/dan-ci-ti-huan-by-leetcode/)

- 解题思路

> 将数组dictionary存储哈希表hashD
将字符串sentence转为数组并进行遍历，得到每个单词word
在hashD查找word是否存在与之对应的词根
若存在，返回词根；若不存在，返回原来的单词
最后将替换的单词列表转为字符串作为结果返回

- 复杂度

> 时间复杂度：O(wi^2)，wi是第i个单词的长度
空间复杂度：O(n)，n是句子的长度

- 代码实现

> python3

```
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hashD = set(dictionary)
        def replace(word):
            for i in range(len(word)):
                if word[:i] in hashD:
                    return word[:i]
            return word
        return " ".join(map(replace,sentence.split()))
```

> php

```
class Solution {
    function replaceWords($dictionary, $sentence) {
        $this->hashD = array_unique($dictionary);
        return implode(" ",array_map([$this,'replace'],explode(" ",$sentence)));
    }

    function replace($word){
        for($i=0;$i<strlen($word);$i++){
            $c = substr($word,0,$i);
            if(in_array($c,$this->hashD)){
                return $c;
            }
        }
        return $word;
    }
}
```

#  文字草稿

> dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
遍历第1个单词the，第1个字母t无前缀匹配，不做替换
遍历第2个单词cattle：
第1个字母c匹配前缀c，pass
第2个字母a匹配前缀ca，pass
第3个字母t匹配单词cat，pass
cattle替换后为cat
遍历第3个单词was，第1个字母w，无前缀匹配，不做替换
遍历第4个单词rattled：
第1个字母r匹配前缀r，pass
第2个字母a匹配前缀ra，pass
第3个字母t匹配单词rat，pass
rattled替换后为rat
遍历第5个单词by，第1个字母b，无前缀匹配，不做替换
遍历第6个单词the，第1个字母t无前缀匹配，不做替换
遍历第7个单词battery：
第1个字母b匹配前缀b，pass
第2个字母a匹配前缀ba，pass
第3个字母t匹配单词bat，pass
battery替换后为bat
替换之后的句子为：the cat was rat by the bat
