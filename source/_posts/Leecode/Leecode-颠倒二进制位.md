---
title: Leecode-颠倒二进制位
categories: Leecode
---
![6131616988698_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-a733a6dbf38b6af4.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第190题：[颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)
颠倒给定的 32 位无符号整数的二进制位。
提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
示例 1：
输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。

#  解题方法

> 位运算
[参照题解](https://leetcode-cn.com/problems/reverse-bits/solution/fu-xue-ming-zhu-xun-huan-yu-fen-zhi-jie-hoakf/)

- 解题思路

> 定义变量`ret`拼接颠倒后的二进制位
在[0,32)的区间内遍历二进制位`n`
每次迭代，`ret`逐步**左移**，得到二进制位的末尾数字
将末尾数字拼接到`ret`的末尾，再将`n`逐步**右移**

- 复杂度

> 时间复杂度：O(1)
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for _ in range(32):
            ret = (ret<<1)+(n&1)
            n>>=1
        return ret
```

> php

```
class Solution {
    function reverseBits($n) {
        $ret = 0;
        for($i=0;$i<32;$i++){
            $ret = ($ret<<1)+($n&1);
            $n>>=1;
        }
        return $ret;
    }
}
```

