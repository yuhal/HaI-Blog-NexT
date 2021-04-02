---
title: Leecode-扁平化嵌套列表迭代器
categories: Leecode
---
![WechatIMG603.jpeg](https://upload-images.jianshu.io/upload_images/15325592-c2fdfaaedec4ed81.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第341题：[扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
示例:
输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

#  解题方法

> 栈
[参照题解](https://leetcode-cn.com/problems/flatten-nested-list-iterator/solution/python-zhan-dai-ma-jian-dan-yi-li-jie-by-hsyv5897/)

- 解题思路

> 创建栈`stack`来存储整型列表`nestedList`中的所有整数
因为返回整数的顺序是**从左到右**，所以需要将`nestedList`反转后压栈
在`hasNext`中，当`stack`有值，且栈顶元素是**列表**时
**弹出**栈顶元素，反转后再**依次**压栈，直到栈顶元素为**整数**
每次调用`hasNext`时，就能保证栈顶元素是**整数**，直到栈为空
每次调用`next`时，弹出栈顶的整数即可

- 复杂度

> 时间复杂度：初始化和next为O(1)，hasNext为均摊O(1)
空间复杂度：O(n)

- 代码实现

> python3

```
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.stack += self.stack.pop().getList()[::-1]
        return self.stack
```

> php

```
class NestedIterator {
    function __construct($nestedList) {
        krsort($nestedList);
        $this->stack = $nestedList;
    }  
    
    function next() {
        return array_pop($this->stack)->getInteger();
    }
    
    function hasNext() {
        while($this->stack && !end($this->stack)->isInteger()){
            $list = array_pop($this->stack)->getList();
            krsort($list);
            $this->stack = array_merge($this->stack,$list);
        }
        return $this->stack;
    }
}
```
