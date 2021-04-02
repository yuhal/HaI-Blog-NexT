---
title: Leecode-笨阶乘
categories: Leecode
---
![WechatIMG631.jpeg](https://upload-images.jianshu.io/upload_images/15325592-5ddfa80b2f8ac5f2.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。
示例：
输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

#  解题方法

> 栈
[原址题解](https://leetcode-cn.com/problems/clumsy-factorial/solution/ben-jie-cheng-by-yohannzhang-7y3j/)

- 解题思路

> 先把正整数`n`以固定顺序的操作符转为表达式`s`
在使用[基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/)的思路求值即可

- 复杂度

> 时间复杂度：O(2n)
空间复杂度：O(2n)

- 代码实现

> python3

```
class Solution:
    def clumsy(self, N: int) -> int:
        s = ""
        for i in range(N,0,-4):
            s += str(i)+"*"
            if i-1>0:     
                s += str(i-1)+"/"
            if i-2>0:
                s += str(i-2)+"+"
            if i-3>0:
                s += str(i-3)+"-"
        s = s[:-1]
        return self.calculate(s)
    
    def calculate(self, s: str) -> int:
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
    function clumsy($N) {
        $s = "";
        for($i=$N;$i>0;$i-=4){
            $s .= $i."*";
            if($i-1>0){
                $s .= ($i-1)."/";
            }
            if($i-2>0){
                $s .= ($i-2)."+";
            }
            if($i-3>0){
                $s .= ($i-3)."-";
            }
        }
        $s = substr($s,0,-1);
        return $this->calculate($s);
    }

    function calculate($s) {
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
