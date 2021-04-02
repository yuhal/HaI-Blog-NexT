---
title: Leecode-猜字谜
categories: Leecode
---

![WechatIMG521.jpeg](https://upload-images.jianshu.io/upload_images/15325592-5d59cb083b50a0dd.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1178题：[猜字谜](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/)
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
单词 word 中包含谜面 puzzle 的第一个字母。
单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
示例：
输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。

#  解题方法

> 字典树
[参照题解](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/solution/cai-zi-mi-by-leetcode-solution-345u/)

- 解题思路

> 创建字典数root
遍历数组words，将每个word去重并按字典排序后存入root，并记录每个字母出现的次数
定义数组ans，存储每个谜面puzzle对应的谜底word
遍历数组puzzles，根据首字母fletter和按字典排序后的puzzle在root递归查找谜底的数目ret
将ret逐个存储ans返回

- 代码实现

> python3

```
class Trie:
    def __init__(self):
        self.next = {}
        self.count = 0
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        root = Trie()
        def addWord(word):
            tree = root
            for c in word:
                idx = ord(c)-ord('a')
                if idx not in tree.next:
                    tree.next[idx] = Trie()
                tree = tree.next[idx]
            tree.count += 1
        for word in words:
            addWord(sorted(set(word)))
        def find(fletter,puzzle,tree,pos):
            if not tree:
                return 0
            if pos==7:
                return tree.count
            ret = 0
            idx = ord(puzzle[pos])-ord('a')
            if idx in tree.next:
                ret += find(fletter,puzzle,tree.next[idx],pos+1)
            if fletter!=puzzle[pos]:
                ret += find(fletter,puzzle,tree,pos+1)
            return ret
        ans = []
        for puzzle in puzzles:
            fletter = puzzle[0]
            puzzle = sorted(puzzle)
            ans.append(find(fletter,puzzle,root,0))
        return ans
```

> php

```
class Trie {
    public $next = [];
    public $count = 0;
}
class Solution {
    function findNumOfValidWords($words, $puzzles) {
        $this->root = new Trie();
        array_map([$this,'addWord'],$words);
        $ans = [];
        foreach($puzzles as $puzzle){
            $fletter = $puzzle[0];
            $puzzle = $this->sorted($puzzle);
            array_push($ans,$this->find($fletter,$puzzle,$this->root,0));
        }
        return $ans;
    }

    function addWord($word){
        $word = $this->sorted($this->set($word));
        $tree = $this->root;
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            $idx = ord($c)-ord('a');
            if(!isset($tree->next[$idx])){
                $tree->next[$idx] = new Trie();
            }
            $tree = $tree->next[$idx];
        }
        $tree->count++;
    }

    function find($fletter,$puzzle,$tree,$pos){
        if(!$tree){
            return 0;
        }
        print($pos);
        if($pos==7){
            return $tree->count;
        }
        $ret = 0;
        $idx = ord($puzzle[$pos])-ord('a');
        if(isset($tree->next[$idx])){
            $ret += $this->find($fletter,$puzzle,$tree->next[$idx],$pos+1);
        }
        if($puzzle[$pos]!=$fletter){
            $ret += $this->find($fletter,$puzzle,$tree,$pos+1);
        }
        return $ret;
    }

    function sorted($word){
        $arr = str_split($word);
        asort($arr);
        return implode($arr);
    }

    function set($word){
        $arr = array_unique(str_split($word));
        return implode($arr);
    }
}
```
