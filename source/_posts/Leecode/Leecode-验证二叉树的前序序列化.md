---
title: Leecode-验证二叉树的前序序列化
categories: Leecode
---

![WechatIMG585.jpeg](https://upload-images.jianshu.io/upload_images/15325592-205d3303c67394c1.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第331题：[验证二叉树的前序序列化](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/)
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 # 。
![1615515074267.jpg](https://upload-images.jianshu.io/upload_images/15325592-5d0a45c3533fcb9d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
例如，上面的二叉树可以被序列化为字符串 "9,3,4,# ,# ,1,# ,# ,2,# ,6,# ,# "，其中 #  代表一个空节点。
给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '# ' 。
你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
示例:
输入: "9,3,4,# ,# ,1,# ,# ,2,# ,6,# ,# "
输出: true

#  解题方法

> 栈
[参照题解](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/solution/yan-zheng-er-cha-shu-de-qian-xu-xu-lie-h-jghn/)

- 解题思路

> 由于字符串`preorder`中每个字符以逗号分隔，先将`preorder`分割为数组
创建栈`stack`来存储每个节点处**占位的数量**，因为根节点自身需要占位，所以初始压栈1
获取`preorder`的长度`n`，在`[0,n)`的范围内循环得到当前节点`preorder[i]`
在当前节点下，有**左右两个子节点**
若遇到一个空节点，需要用`# `占位（栈顶元素减1）
若遇到一个非空节点，除了它本身需要占位（栈顶元素减1），还需要对它的左右两个子节点用`# `占位（压栈2）
**无论何时**，如果无需占位（栈顶元素变为0），就无需压栈
最终返回栈`stack`是否为空，为空表示二叉树的前序序列化正确

- 复杂度

> 时间复杂度：O(n)，n为二叉树的节点数
空间复杂度：O(n)

- 代码实现

> python3

```
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        n = len(preorder)
        stack = [1]
        i = 0
        while i<n:
            if not stack:
                return False
            if preorder[i]=="# ":
                top = stack.pop()-1
                if top>0:
                    stack.append(top)
                i += 1
            else:
                top = stack.pop()-1
                if top>0:
                    stack.append(top)
                stack.append(2)
                i += 1  
        return not stack
```

> php

```
class Solution {
    function isValidSerialization($preorder) {
        $preorder = explode(",",$preorder);
        $n = count($preorder);
        $stack = [1];
        $i = 0;
        while($i<$n){
            if(empty($stack)){
                return false;
            }
            if($preorder[$i]=="# "){
                $top = array_pop($stack)-1;
                if($top>0){
                    array_push($stack,$top);
                }
                $i++;
            }else{
                $top = array_pop($stack)-1;
                if($top>0){
                    array_push($stack,$top);
                }
                array_push($stack,2);
                $i++;
            }
        }
        return empty($stack);
    }
}
```
