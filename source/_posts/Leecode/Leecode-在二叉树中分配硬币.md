---
title: Leecode-在二叉树中分配硬币
categories: Leecode
---

![5401614680550_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-f4cf44d87b56fe9c.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第979题：[在二叉树中分配硬币](https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/)
给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。
返回使每个结点上只有一枚硬币所需的移动次数。
示例：
![tree1.png](https://upload-images.jianshu.io/upload_images/15325592-83a3e700308b7aaf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
输入：[3,0,0]
输出：2
解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。

#  解题方法

> DFS
[参照题解](https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/)

- 解题思路

> 定义所需的移动次数count，初始为0
后续遍历数组nums
DFS计算左右节点金币过载量L和R
累加当前节点需要移动金币的数量为abs(L)+abs(R)
返回当前节点的金币过载量=当前节点金币数量+L+R-1

- 复杂度

> 时间复杂度：O(n)，n是二叉树节点的数量
空间复杂度：O(h)，h是二叉树的深度

- 代码实现

> python3

```
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if not node: return 0
            L,R = dfs(node.left),dfs(node.right)
            self.count += abs(L)+abs(R)
            return node.val+L+R-1
        dfs(root)
        return self.count
```

> php

```
class Solution {
    function distributeCoins($root) {
        $this->count = 0;
        $this->dfs($root);
        return $this->count;
    }

    function dfs($node){
        if(!$node) return 0;
        $L = $this->dfs($node->left);
        $R = $this->dfs($node->right);
        $this->count += abs($L)+abs($R);
        return $node->val+$L+$R-1;
    }
}
```
