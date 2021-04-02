---
title: Leecode-用栈实现队列
categories: Leecode
---
![WechatIMG552.jpeg](https://upload-images.jianshu.io/upload_images/15325592-9e547830c273535e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第232题：[用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/)
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
进阶：
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
示例：
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]
解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

#  解题方法

> 栈
[参照题解](https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/dong-hua-jiang-jie-ru-he-shi-yong-liang-6g7ub/)

- 解题思路 
 
> 创建输入栈stack1和输出栈stack2来实现队列
每次push，把元素x依次存入stack1
调用pop或peek时，把stack1中的元素逐个弹出并依次存入stack2
这样stack2就实现了先进先出，再返回stack2每次pop或peek的元素即可
当stack1和stack2中都为空时，表示队列为空

- 复杂度

> 时间复杂度：push时为O(1)，peek/pop时为O(1)，最坏为O(n)
空间复杂度：O(n)

- 代码实现

> python3

```
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2
```

> php

```
class MyQueue {
    function __construct() {
        $this->stack1 = [];
        $this->stack2 = [];
    }

    function push($x) {
        array_push($this->stack1,$x);
    }

    function pop() {
        if(empty($this->stack2)){
            while($this->stack1){
                array_push($this->stack2,array_pop($this->stack1));
            }
        }
        return array_pop($this->stack2);
    }

    function peek() {
        if(empty($this->stack2)){
            while($this->stack1){
                array_push($this->stack2,array_pop($this->stack1));
            }
        }
        return end($this->stack2);
    }

    function empty() {
        return empty($this->stack1) && empty($this->stack2);
    }
}
```


