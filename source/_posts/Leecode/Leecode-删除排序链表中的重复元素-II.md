---
title: Leecode-删除排序链表中的重复元素-II
categories: Leecode
---

![WechatIMG608.jpeg](https://upload-images.jianshu.io/upload_images/15325592-b6173dd071ef1c79.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第82题：[删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。
示例：
![linkedlist1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-b8e791aad1fe4205.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

#  解题方法一

> 栈
[原址题解](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-tvim/)

- 解题思路

> 使用栈`stack`来存储链表中的数字
定义变量`pop`来表示每次出栈数字，初始为None
遍历链表`head`
若当前节点数字`head.val`**存在于**栈中，**更新**出栈数字
若当前节点数字**不等于**出栈数字，将节点数字**压栈**
遍历完成，此时栈中都是**不重复**的数字，再将栈转为链表返回即可

- 复杂度

> 时间复杂度：O(n)，n为链表的长度
空间复杂度：O(n)，n为栈的大小

- 代码实现

```python3 []
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        stack = []
        pop = None
        while head:
            if head.val in stack:
                pop = stack.pop()
            if head.val!=pop:
                stack.append(head.val)
            head = head.next
        dummy = ListNode()
        cur = dummy
        for v in stack:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
```
```php []
class Solution {
    function deleteDuplicates($head) {
        if(!$head) return $head;
        $stack = [];
        $pop = null;
        while($head){
            if(in_array($head->val,$stack)){
                $pop = array_pop($stack);
            }
            if($pop!==$head->val){
                array_push($stack,$head->val);
            }
            $head = $head->next;
        }
        $dummy = new ListNode();
        $cur = $dummy;
        foreach($stack as $v){
            $cur->next = new ListNode($v);
            $cur = $cur->next;
        }
        return $dummy->next;
    }
}
```


#  解题方法二

> 链表
[参照题解](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-oayn/)

- 解题思路

> 由于链表`head`的头节点可能会被删除
添加一个**哑节点**指向链表的**头节点**，得到新的链表`dummy`
使用指针`cur`表示当前节点开始遍历链表
如果`cur.next.val`**等于**`cur.next.next.val`
记下`cur.next.val`为`temp`，**指针后移**，将等于`temp`的节点删除
反之将`cur`指向`cur.next`
遍历完成，此时链表中剩余**哑节点**和**不重复的节点**
跳过**哑节点**，直接返回`dummy.next`即可



- 复杂度

> 时间复杂度：O(n)，n为链表的长度
空间复杂度：O(1)

- 代码实现

```python3 []
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy = ListNode(0,head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                temp = cur.next.val
                while cur.next and temp==cur.next.val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```
```php []
class Solution {
    function deleteDuplicates($head) {
        if(!$head) return $head;
        $dummy = new ListNode(0,$head);
        $cur = $dummy;   
        while($cur->next && $cur->next->next){
            if($cur->next->val == $cur->next->next->val){
                $temp = $cur->next->val;
                while($cur->next && $temp==$cur->next->val){
                    $cur->next = $cur->next->next;
                }
            }else{
                $cur = $cur->next;
            }
        }
        return $dummy->next;
    }
}
```





