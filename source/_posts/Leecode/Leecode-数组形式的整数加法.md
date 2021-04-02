---
title: Leecode-数组形式的整数加法
categories: Leecode
---
![5181614317592_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-dbb23a119ee6a0fb.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第989题：[数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer/)
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
示例：
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234

#  解题方法

> API
[原址题解](https://leetcode-cn.com/problems/add-to-array-form-of-integer/solution/shu-zu-xing-shi-de-zheng-shu-jia-fa-by-y-6x7e/)

- 解题思路

> 定义字符串s，遍历数组A拼接每个数
将s转数值型后与K相加，相加结果再转为字符串型
最终将字符串型的结果转数组返回即可

- 复杂度

> 时间复杂度：O(n)，n是数组A的长度
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s = ""
        for a in A:
            s += str(a)
        return list(str(int(s)+K))
```
