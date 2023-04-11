# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''两数相加给你
两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

'''
from typing import List
class Solution:
    def addTwoNumbers(self, l1: List[int], l2: List[int]) -> List[int]:
        l3 = []
        
        if len(l1)>len(l2):
          length = len(l1)
          gap = len(l1) - len(l2)
          for i in range(gap):
              l2.append(0)
        else:
          length = len(l2)
          gap = len(l2) - len(l1)
          for i in range(gap):
              l2.append(0)
        
        for i in range(length):
          l3_len = len(l3)-1
          if l3:
           if l3[l3_len]>=10:
              a = l3[l3_len] - 10
              del l3[l3_len]
              l3.append(a)
              sum = l1[i]+l2[i]+1
              l3.append(sum)
           else:
              sum = l1[i]+l2[i]
              l3.append(sum)
          else:
             sum = l1[i]+l2[i]
             l3.append(sum)
        l3_len = len(l3)-1
        if l3[l3_len]>=10:
              a = l3[l3_len] - 10
              del l3[l3_len]
              l3.append(a)
              l3.append(1)
        return l3
    
    
    
    
if __name__ =='__main__':
  s = Solution()
  a = [0,0,5]
  b = [0,0,5]
  print(s.addTwoNumbers(a,b))
