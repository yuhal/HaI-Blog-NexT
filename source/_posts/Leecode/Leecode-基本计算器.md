---
title: Leecode-基本计算器
categories: Leecode
---

![WechatIMG579.jpeg](https://upload-images.jianshu.io/upload_images/15325592-89cb05679f5c8ae3.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第224题：[基本计算器](https://leetcode-cn.com/problems/basic-calculator/)
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
示例：
输入：s = " (1+(4+5+2)-3)+(6+8) "
输出：23

#  解题方法

> 栈
[参照题解](https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/)

- 解题思路

> 由于字符串表达式`s`中存在空格，需要先**去除空格**，这时`s`中仅存在数字、加减号、括号
将`s`整体转换为加法运算，**减去一个数**可以理解为**加上这个数的负数**，1-1看作1+(-1)
然后定义变量`sign`来标示每个数前面的**正负符号**{-1,+1}
对于`s`，第一个数前面的符号一定为**正**，1-1看作0+1-1，所以`sign`默认为1并压栈
定义变量`sumS`，存储`s`计算后的值，初始为0
获取`s`的长度`n`，在`[0,n)`的范围内循环得到当前字符`s[i]`
如果`s[i]`为`+`号，则更新`sign`为栈顶元素
如果`s[i]`为`-`号，则更新`sign`为栈顶元素的负数
如果`s[i]`为`（`号，将当前的`sign`压栈
如果`s[i]`为`）`号，弹出栈顶元素
如果`s[i]`为数字，`sumS`累加当前数字的数值`sign*num`
最后`s`计算后的值就是`sumS`

- 复杂度

> 时间复杂度：O(n)，n为字符串s的长度
空间复杂度：O(n)，n为字符串s的长度

- 代码实现

> python3

```
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        n = len(s)
        sign = 1
        stack = [sign]
        i = sumS = 0
        while i<n:
            if s[i]=="(":
                stack.append(sign)
                i+=1
            elif s[i]==")":
                stack.pop()
                i+=1
            elif s[i]=="+":
                sign = stack[-1]
                i+=1
            elif s[i]=="-":
                sign = -stack[-1]
                i+=1
            else:
                num = 0
                while i<n and s[i].isdigit():
                    num = num*10+int(s[i])
                    i += 1
                sumS += sign*num
        return sumS
```

> php

```
class Solution {
    function calculate($s) {
        $s = str_replace(" ","",$s);
        $n = strlen($s);
        $sign = 1;
        $stack = [$sign];
        $i = $sumS = 0;
        while($i<$n){
            if($s[$i]=="+"){
                $sign = end($stack);
                $i++;
            }elseif($s[$i]=="-"){
                $sign = -end($stack);
                $i++;
            }elseif($s[$i]=="("){
                array_push($stack,$sign);
                $i++;
            }elseif($s[$i]==")"){
                array_pop($stack);
                $i++;
            }else{
                $num = 0;
                while($i<$n && is_numeric($s[$i])){
                    $num = $num*10+$s[$i];
                    $i++;
                }
                $sumS += $sign*$num;
            }
        }
        return $sumS;
    }
}
```
