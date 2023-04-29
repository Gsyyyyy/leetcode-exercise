'''
35行return head 会造成heap = heap所以while循环一直下去，不能将节点保存在list里面
因为用lst[0].next容易会造成不存在类型 不能使用.next

给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：



输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]


'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = heap = ListNode(next = head)
        '''def reverseNextKNodes(head, k):
            testNode = head
            for _ in range(k):
                if not testNode.next:
                    return testNode
                testNode = testNode.next
            newTail = head.next
            prev, cur = head.next, head.next.next
            for _ in range(k - 1):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            head.next = prev
            newTail.next = cur
            return newTail'''
        def reverseK(head,k):
            ar = head
            
            for i in range(k):
                if not ar.next:
                    # If there are less than k nodes, return head
                    return ar
                ar = ar.next
            
            ar1,ar2 = head.next,head.next.next
            for i in range(k-1):
                temp = ar2.next
                ar2.next = ar1
                ar1 = ar2
                ar2 = temp
            pp = head.next
            head.next = ar1
            pp.next = ar2
            return pp

        while heap.next:
            heap = reverseK(heap,k)
            
        return result.next
    