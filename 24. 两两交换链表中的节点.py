'''
self.next.next用于等式左边会超出时间限制

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = result = ListNode(0)
        a.next = head
        if head == None:
            return None
        while a.next and a.next.next:
            heap1 = a.next
            heap2 = a.next.next
            heap1.next = heap2.next
            heap2.next = heap1
            a.next = heap2
            a = a.next.next
        return result.next

