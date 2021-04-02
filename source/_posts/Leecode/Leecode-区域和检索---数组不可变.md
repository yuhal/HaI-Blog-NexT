---
title: Leecode-区域和检索---数组不可变
categories: Leecode
---

![5391614680513_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-12c4d463148d30ce.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第303题：[区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable/)
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

#  解题方法一

> 暴力法
[原址题解](https://leetcode-cn.com/problems/range-sum-query-immutable/solution/qu-yu-he-jian-suo-shu-zu-bu-ke-bian-by-y-pq5a/)

- 解题思路

> 每次遍历数组nums，累加从i到j之间的元素

- 复杂度

> 时间复杂度：O(n)
空间复杂度：O(1)

- 代码实现

> python3

```
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, i: int, j: int) -> int:
        sumN = 0
        while i<=j:
            sumN += self.nums[i]
            i += 1
        return sumN
```

> php

```
class NumArray {
    function __construct($nums) {
        $this->nums = $nums;
    }
    function sumRange($i, $j) {
        $sumN = 0;
        while($i<=$j){
            $sumN += $this->nums[$i];
            $i++;
        }
        return $sumN;
    }
}
```

#  解题方法二

> 前缀和
[参照题解](https://leetcode-cn.com/problems/range-sum-query-immutable/solution/presum-qian-zhui-he-xiang-xi-jiang-jie-b-nh23/)

- 解题思路

> 定义n获取数组nums的长度
定义数组preSums，长度为n+1，元素值初始都为0
在[i,n)范围内遍历nums，计算每一区间[i,j]内元素的和并存入preSums
每次调用sumRange，preSums中j+1下标的值与i下标的值相减就是返回的总和

- 复杂度

> 时间复杂度：初始为O(n)，每次调用为O(1)
空间复杂度：O(n)

- 代码实现

> python3

```
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.preSums = [0]*(n+1)
        for i in range(n):
            self.preSums[i+1] = self.preSums[i]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.preSums[j+1]-self.preSums[i]
```

> php

```
class NumArray {
    function __construct($nums) {
        $n = count($nums);
        $this->preSums = [0];
        for($i=0;$i<$n;$i++){
            $this->preSums[$i+1] = $this->preSums[$i]+$nums[$i];
        }
    }

    function sumRange($i, $j) {
        return $this->preSums[$j+1]-$this->preSums[$i];
    }
}
```






