---
title: Leecode-位1的个数
categories: Leecode
---

![WechatIMG602.jpeg](https://upload-images.jianshu.io/upload_images/15325592-7e62d092c5c43a76.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第191题：编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
示例：
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

#  解题方法一

> API
[参照题解](https://leetcode-cn.com/problems/number-of-1-bits/solution/fu-xue-ming-zhu-xiang-jie-wei-yun-suan-f-ci7i/)

- 解题思路

> 在 python 和 php 中，存在`bin`和`decbin`这样的库函数
使用库函数将十进制位的整数`n`转换为二进制位
然后统计二进制位中**1**出现的次数

- 复杂度

> 时间复杂度：O(k)，k为n的二进制位的长度
空间复杂度：O(k)，k为n的二进制位长度

- 代码实现

> python3

```
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
```

> php

```
class Solution {
    function hammingWeight($n) {
        return substr_count(decbin($n),1);
    }
}
```

#  解题方法二

> 位运算
[参照题解](https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode-solution-jnwf/)

- 解题思路

> 使用位运算中**与运算**的性质检查二进制位中的最低位是**0**还是**1**
举个例子：n=3；n-1=2，`n&=n-1`相当于`n=n&n-1`
3的二进制表示为11；2的二进制表示为10
&（与）的结果为10，就是2，所以`n=n&n-1`后，n为2
在本题中，重复把当前的`n`与`n−1`做**与运算**，直到`n`变为0
因为每次运算中，`n`的**最低位**从1变为0
所以运算次数`count`就等于`n`的二进制位中1出现的次数


- 复杂度

> 时间复杂度：O(logn)
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            count+=1
        return count
```

> php

```
class Solution {
    function hammingWeight($n) {
        $count = 0;
        while($n){
            $n &= $n-1;
            $count++;
        }
        return $count;
    }
}
```



