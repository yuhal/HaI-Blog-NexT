---
title: Leecode-搜索推荐系统
categories: Leecode
---

![WechatIMG504.jpeg](https://upload-images.jianshu.io/upload_images/15325592-a4d62ab4a19ee759.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第1268题：[搜索推荐系统](https://leetcode-cn.com/problems/search-suggestions-system/)
你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。
请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。
请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。
示例：
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]

#  解题方法

> 字典树
[参照题解](https://leetcode-cn.com/problems/search-suggestions-system/solution/suo-tui-jian-xi-tong-by-leetcode-solution/)

- 解题思路

> 构建字典树root
遍历数组products中的每个单词，存储所有字符串及字符串前缀对应的单词列表words
当words的长度>3时，弹出超出的单词
遍历完成后，创建数组ans，记录输入searchWord时，存储匹配的单词
立一个旗帜flag默认状态为false，表示一定能匹配到单词
遍历searchWord，判断输入的字符c在root中匹配的节点
若c不存在root中，向ans存储空数组，并更新flag状态为true
反之，向ans存储c在root中匹配的节点对应的单词
遍历完成后，返回ans就是所推荐单词的列表

- 复杂度

> 时间复杂度：O(∑L+S)，L∑L是所有字符串的长度之和，S是字符串searchWord的长度。
空间复杂度：O(∑L)。

- 代码实现

> python3

```
class Trie:
    def __init__(self):
        self.next = {}
        self.words = []

class Solution:
    def __init__(self):
        self.root = Trie()
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def addWord(word):
            tree = self.root
            for c in word:
                if c not in tree.next:
                    tree.next[c] = Trie()
                tree = tree.next[c]
                tree.words.append(word)
                tree.words.sort()
                if len(tree.words)>3:
                    tree.words.pop()
        for word in products:
            addWord(word)
        tree = self.root
        ans = []
        flag = False
        for c in searchWord:
            if flag or c not in tree.next:
                ans.append([])
                flag = True
            else:
                tree = tree.next[c]
                ans.append(tree.words)
        return ans
```

> php

```
class Solution {
    private $root;

    function __construct(){
        $this->root = new Trie();
    }

    function suggestedProducts($products, $searchWord) {
        array_map([$this,'addWord'],$products);
        $flag = false;
        $ans = [];
        $tree = $this->root;
        for($i=0;$i<strlen($searchWord);$i++){
            $c = $searchWord[$i];
            if($flag || !isset($tree->next[$c])){
                array_push($ans,[]);
                $flag = true;
            }else{
                $tree = $tree->next[$c];
                array_push($ans,$tree->words);
            }
        }
        return $ans;
    }

    function addWord($word){
        $tree = $this->root;
        for($i=0;$i<strlen($word);$i++){
            $c = $word[$i];
            if(!isset($tree->next[$c])){
                $tree->next[$c] = new Trie();
            }
            $tree = $tree->next[$c];
            array_push($tree->words,$word);
            asort($tree->words);
            if(count($tree->words)>3){
                array_pop($tree->words);
            }
        }
    }
}

class Trie {
    public $next;
    public $words;
    
    function __construct(){
        $this->next = [];
        $this->words = [];
    }
}
```

- 文字草稿

> products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
输入字符m，推荐产品的列表为[['mobile', 'moneypot', 'monitor']]
输入字符o，推荐产品的列表为[['mobile', 'moneypot', 'monitor']]
输入字符u，推荐产品的列表为[['mouse', 'mousepad']]
输入字符s，推荐产品的列表为[['mouse', 'mousepad']]
输入字符e，推荐产品的列表为[['mouse', 'mousepad']]
记录每个字母后相应的推荐产品的列表为：
[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
