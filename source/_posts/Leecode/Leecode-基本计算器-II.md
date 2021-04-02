---
title: Leecode-基本计算器-II
categories: Leecode
---

![WechatIMG581.jpeg](https://upload-images.jianshu.io/upload_images/15325592-71d535666f79147d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第227题：[基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/)
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
示例：
输入：s = " 3+5 / 2 "
输出：5

#  解题方法

> 栈
[参照题解](https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/)

- 解题思路

> 由于字符串表达式`s`中存在空格，需要先**去除空格**，这时`s`中仅存在数字、加减乘除号
然后定义变量`sign`来标示每个数前面的运算符
对于`s`，第一个数前面的符号一定为**正**，3+5看作0+3+5，所以`sign`默认为`+`，
**先计算乘除后整体转换为加法运算**，创建栈`stack`存储每次需要相加的数值
获取`s`的长度`n`，在`[0,n)`的范围内循环得到当前字符`s[i]`
如果`s[i]`为数字，计算当前数字的数值`num`
如果`s[i]`为运算符或者下标`i`等于`n-1`(**保证末尾数字参与运算**)时
分别考虑以下情况：
`s[i]`为`+`号，`num`压栈
`s[i]`为`-`号，负的`num`压栈
`s[i]`为`*`号，计算`num`与栈顶元素相乘的结果后压栈
`s[i]`为`/`号，计算`num`与栈顶元素相除的结果后压栈
每次压栈后，更新`sign`为当前的运算符并将`num`**清零**
最后将栈`stack`中元素求和，即为`s`计算后的值

- 复杂度

> 时间复杂度：O(n)，n为字符串s的长度
空间复杂度：O(n)，n为字符串s的长度

> python3

```
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        n = len(s)
        sign = "+"
        stack = []
        i = num = 0
        while i<n:
            if s[i].isdigit():
                num = num*10+int(s[i])
            if not s[i].isdigit() or i==n-1:
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="*":
                    stack.append(stack.pop()*num)
                elif sign=="/":
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
            i+=1
        return sum(stack)
```

> php

```
class Solution {
    function calculate($s) {
        $s = str_replace(" ","",$s);
        $n = strlen($s);
        $sign = "+";
        $stack = [];
        $i = $num = 0;
        while($i<$n){
            if(is_numeric($s[$i])){
                $num = $num*10+$s[$i];
            }
            if(!is_numeric($s[$i]) || $i==$n-1){
                if($sign=="+"){
                    array_push($stack,$num);
                }elseif($sign=="-"){
                    array_push($stack,-$num);
                }elseif($sign=="*"){
                    array_push($stack,array_pop($stack)*$num);
                }elseif($sign=="/"){
                    array_push($stack,(int) (array_pop($stack)/$num));
                }
                $num = 0;
                $sign = $s[$i];
            }
            $i++;
        }
        return array_sum($stack);
    }
}
```
