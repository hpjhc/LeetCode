"""
source: https://leetcode.com/problems/merge-two-sorted-lists/
author: hpjhc
date: 2018/10/17
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        last = ListNode(0)
        while l1 or l2:
            if not l1:
                nxt = l2
                l2 = l2.next
            elif not l2:
                nxt = l1
                l1 = l1.next
            elif l1.val < l2.val:
                nxt = l1
                l1 = l1.next
            else:
                nxt = l2
                l2 = l2.next                 
            if not head:
                head = nxt
                last = head
            else:
                last.next = nxt
                last = nxt
        return head
