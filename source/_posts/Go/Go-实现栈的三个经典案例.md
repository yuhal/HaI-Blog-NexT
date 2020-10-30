---
title: Go-实现栈的三个经典案例
categories: Go
---

![WechatIMG9.jpeg](https://upload-images.jianshu.io/upload_images/15325592-88dd8f315e456b98.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  环境配置

- 创建目录

```
$ mkdir -p /home/go/src/mystack
```

- 设置 HOME 路径

```
$ export HOME=/home
$ echo $HOME
/home
```

- 设置 GOPATH 路径

```
$ export GOPATH=$HOME/go
$ echo $GOPATH
/home/go
```


#  栈

- 创建 /home/go/src/mystack/mystack.go，内容如下：

```
package mystack

import (
    "fmt"
)

// 栈：先进后出，从栈顶取数据，栈低固定
type Stack struct {
    // 栈顶
    Top int
    // 栈容量
    Capacity int
    // 指向栈指针
    Prt *[]interface{} 
}

// 初始化栈
func (mystack *Stack) StackInitial(capacity  int){
    mystack.Capacity = capacity
    mystack.Top = 0
    // 使用interface类型，所有数据类型都能兼容
    m := make([]interface{},capacity)
    mystack.Prt = &m
}

// 元素入栈，栈顶上升
func (mystack *Stack) StackPush(em interface{})bool{
    // 判满
    if mystack.StackIsFull(){
        fmt.Println("The stack is full")
        return false
    }else {
        // 放入栈顶
        (*mystack.Prt)[mystack.Top] = em
        mystack.Top++
        return true
    }
}
// 元素出栈，栈顶下降
func (mystack *Stack) StackPop()(interface{},bool){
    // 判空
    if mystack.StackIsEmpty(){
        fmt.Println("The stack is empty")
        return  nil,false
    }else {
        // 取栈顶
        mystack.Top--
        em:= (*mystack.Prt)[mystack.Top]
        return em, true
    }
}

// 判空
func (mystack *Stack) StackIsEmpty()bool{
    if mystack.Top==0 {
        return  true
    }else {
        return false
    }
}

// 判满
func (mystack *Stack) StackIsFull()bool{
    if mystack.Top== mystack.Capacity{
        return  true
    }else {
        return false
    }
}

// 栈清空
func (mystack *Stack) StackClear(){
    // 直接将栈顶置0
    mystack.Top=0
}

// 栈遍历,从栈顶先出
func (mystack *Stack) StackTraverse(){
    for i:=mystack.Top-1;i>=0;i--{
        fmt.Println((*mystack.Prt)[i])
    }
}
```

#  括号匹配 

- 创建 /home/go/matchBrackets.go，内容如下：

```
package main

import (
    "fmt"
    "mystack"
)

func isLegal(str string) bool {
    var stack mystack.Stack
    var strLen = len(str)
    var result = false

    // 初始化栈的容量
    stack.StackInitial(strLen)

    // 从左到右顺序遍历字符串
    for i := 0; i < strLen; i++ {
        var curr = str[i]
        // 当出现左括号时，压栈
        if (isLeft(curr)) {
            stack.StackPush(curr)
            fmt.Println("入栈的元素：",string(curr))
        } else {
            // 判断栈是否为空
            if stack.StackIsEmpty() {
                // 返回不合法
                result = false
            }
            // 当出现右括号时，出栈
            p,_ := stack.StackPop()
            fmt.Println("出栈的元素：",string(curr))
            // 判断当前右括号，和被出栈的左括号是否是互相匹配的一对
            if (isPair(p.(byte), curr) == false) {
                // 返回不合法
                result = false
            }
        }
    }

    // 判断栈是否为空
    if stack.StackIsEmpty() {
        result = true
    }
    return result
}

// 判断是否是做括号
func isLeft(c byte) bool {
    if c == '{' || c == '(' || c == '[' {
        return true
    } else {
        return false
    }
}

// 判断左括号与右括号是否是互相匹配的一对
func isPair(p byte, curr byte) bool {
    if (p == '{' && curr == '}') || (p == '[' && curr == ']') || (p == '(' && curr == ')') {
        return true
    } else {
        return false
    }
}

func main() {
    var str = "{[(())]}"
    fmt.Println("输入字符串：",str)
    fmt.Println("是否合法：",isLegal(str))
}
```

- 执行

```
$ go run matchBrackets.go
输入字符串： {[(())]}
入栈的元素： {
入栈的元素： [
入栈的元素： (
入栈的元素： (
出栈的元素： )
出栈的元素： )
出栈的元素： ]
出栈的元素： }
是否合法： true
```

#  浏览器的前进和后退

- 创建 /home/go/browserHB.go，内容如下：

```
package main

import (
    "fmt"
    "mystack"
)

// 新页面
func new(backStack *mystack.Stack, headStack *mystack.Stack, page string) {
    backStack.StackPush(page)
    fmt.Println("后退栈入栈的元素：",page)
}

// 前进
func head(backStack *mystack.Stack, headStack *mystack.Stack) {
    page,_ := headStack.StackPop()
    fmt.Println("前进栈出栈的元素：",page.(string))
    backStack.StackPush(page)
    fmt.Println("后退栈入栈的元素：",page)
}

// 后退
func back(backStack *mystack.Stack, headStack *mystack.Stack) {
    page,_ := backStack.StackPop()
    fmt.Println("后退栈出栈的元素：",page.(string))
    headStack.StackPush(page)
    fmt.Println("前进栈入栈的元素：",page)
}

func main() {
    // 后退栈
    var backStack mystack.Stack
    // 前进栈
    var headStack mystack.Stack
    
    fmt.Println("连续访问访问3个页面")
    pageList := [3]string{
        "百度",
        "阿里",
        "腾讯"}
    // 初始化后退栈的容量
    backStack.StackInitial(3)
    // 初始化前进栈的容量
    headStack.StackInitial(3)
    for _, page := range pageList {

        new(&backStack, &headStack, page)
    }
    fmt.Println("后退栈:")
    backStack.StackTraverse()
    fmt.Println("前进栈:")
    headStack.StackTraverse()

    fmt.Println("-----------------\n当前页为腾讯，后退到百度")
    back(&backStack, &headStack)
    back(&backStack, &headStack)
    fmt.Println("后退栈:")
    backStack.StackTraverse()
    fmt.Println("前进栈:")
    headStack.StackTraverse()
    fmt.Println("-----------------\n当前页为百度，前进到阿里")

    head(&backStack, &headStack)
    fmt.Println("后退栈:")
    backStack.StackTraverse()
    fmt.Println("前进栈:")
    headStack.StackTraverse()
}
```

- 执行

```
$ go run browserHB.go
连续访问访问3个页面
后退栈入栈的元素： 百度
后退栈入栈的元素： 阿里
后退栈入栈的元素： 腾讯
后退栈:
腾讯
阿里
百度
前进栈:
-----------------
当前页为腾讯，后退到百度
后退栈出栈的元素： 腾讯
前进栈入栈的元素： 腾讯
后退栈出栈的元素： 阿里
前进栈入栈的元素： 阿里
后退栈:
百度
前进栈:
阿里
腾讯
-----------------
当前页为百度，前进到阿里
前进栈出栈的元素： 阿里
后退栈入栈的元素： 阿里
后退栈:
阿里
百度
前进栈:
腾讯
```

- 图示

![浏览器的前进和后退.gif](https://upload-images.jianshu.io/upload_images/15325592-803b186937206785.gif?imageMogr2/auto-orient/strip)

#  反转字符串中的单词

- 创建 /home/go/reverse.go，内容如下：

```
package main

import (
    "fmt"
    "strings"
    "mystack"
)

// 反转字符串中的单词
func reverseWords(str string) string{
    var stack mystack.Stack
    var strLen = len(str)
    var temp,result = "",""

    // 初始化栈的容量
    stack.StackInitial(strLen)

    // 入栈操作
    for i := 0; i < strLen; i++ {
        if str[i] != ' ' {
            temp += string(str[i])
        } else if temp != "" {
            stack.StackPush(temp)
            fmt.Println("入栈的元素：",temp)
            temp = ""
        } else {
            continue
        }
    }
    if temp != ""{
        stack.StackPush(temp)
        fmt.Println("入栈的元素：",temp)
    }

    // 出栈操作
    for {
        // 判断栈是否为空，为空则跳出循环，反之出栈
        if stack.StackIsEmpty() {
            break
        }
        em,_ := stack.StackPop()
        fmt.Println("出栈的元素：",em)
        result += em.(string)+" "
    }

    // 去除尾部多余的空格
    result = strings.TrimRight(result, " ")
    return result
}

func main(){
    var str = "Tom and  Jerry"
    fmt.Println("输入字符串：",str)
    fmt.Println("反转后输出：",reverseWords(str))
}
```

- 执行

```
$ go run reverse.go
输入字符串： Tom and  Jerry
入栈的元素： Tom
入栈的元素： and
入栈的元素： Jerry
出栈的元素： Jerry
出栈的元素： and
出栈的元素： Tom
反转后输出： Jerry and Tom
```
