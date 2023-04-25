'''
left=right=result= ListNode(next = head)与left，right，result= ListNode(next = head)，ListNode(next = head)，ListNode(next = head)
是完全不一样的意思，前者表示三个参数同时对链表head进行处理，前面参数对链表进行的修改后面的参数将沿用

删除倒数第n个参数的方法。建立两个指针l,r，先将r遍历到顺序的第n个位置，然后l，r再同时遍历，
当r遍历到尽头，l也就来到了倒数第n个位置，然后再用第三个指针指向链表head，输出结果

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=right=result= ListNode(next = head)
        for _ in range(n):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next

        return result.next