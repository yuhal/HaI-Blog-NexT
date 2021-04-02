---
title: Leecode-子集-II
categories: Leecode
---
![WechatIMG625.jpeg](https://upload-images.jianshu.io/upload_images/15325592-2298cd8e4e21d48c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
#  题目描述

> leecode第90题：[子集 II](https://leetcode-cn.com/problems/subsets-ii/)
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
示例：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

#  解题方法

> DFS
[参照题解](https://leetcode-cn.com/problems/subsets-ii/solution/hui-su-fa-mo-ban-tao-lu-jian-hua-xie-fa-y4evs/)

- 解题思路

> 获取整数数组`nums`的长度`n`
因为整数数组是无序的，需要先对整数数组排序
对整数数组进行DFS，**起始索引**`index`从0开始，初始子集`path`为空数组
如果当前子集**不存在**于解集`res`中，进行**插入**
在`[index,n)`区间继续遍历整数数组
如果当前索引`i`**大于**起始索引，且`nums[i]`**等于**`nums[i-1]`，**跳过**
然后进行下一次DFS，直到解集中包含所有情况的子集

- 复杂度

> 时间复杂度：O(n*2^n)
空间复杂度：O(n*2^n)

- 代码实现

> python3

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index,path):
            if path not in res:
                res.append(path)
            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]:
                    continue
                dfs(i+1,path+[nums[i]])
        n = len(nums)
        nums.sort()
        res = []
        dfs(0,[])
        return res
```

> php

```
class Solution {
    function subsetsWithDup($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        sort($this->nums);
        $this->res = [];
        $this->dfs(0,[]);
        return $this->res;
    }

    function dfs($index,$path){
        if(!in_array($path,$this->res)){
            array_push($this->res,$path);
        }
        for($i=$index;$i<$this->n;$i++){
            if($i>$index && $this->nums[$i]==$this->nums[$i-1]){
                continue;
            }
            $this->dfs($i+1,array_merge($path,[$this->nums[$i]]));
        }
    }
}
```

