---
title: Leecode-删除排序链表中的重复元素
categories: Leecode
---
![6111616988667_.pic_hd.jpg](https://upload-images.jianshu.io/upload_images/15325592-7954a5d6209274d0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->

#  题目描述

> leecode第83题：[删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。
示例：
![list1.jpeg](https://upload-images.jianshu.io/upload_images/15325592-c054e8ac5b3ebba0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
输入：head = [1,1,2]
输出：[1,2]

#  解题方法

> 链表
[原址题解](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-jlhs/)

- 解题思路

> 使用指针`cur`表示当前节点开始遍历链表`head`
如果当前节点数字`cur.val`等于下一个节点数字`cur.next.val`
将`cur.next`指针`cur.next.next`，反之将`cur`指向`cur.next`
遍历完成，直接返回`head`即可

- 复杂度

> 时间复杂度：O(n)，n为链表的长度
空间复杂度：O(1)

- 代码实现

> python3

```
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        cur = head
        while cur.next:
            if cur.val==cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

> php

```
class Solution {
    function deleteDuplicates($head) {
        if(!$head) return $head;
        $cur = $head;
        while($cur->next){
            if($cur->val==$cur->next->val){
                $cur->next = $cur->next->next;
            }else{
                $cur = $cur->next;
            }
        }
        return $head;
    }
}
```
