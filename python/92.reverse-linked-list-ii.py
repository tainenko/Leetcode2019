#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (35.71%)
# Total Accepted:    209.4K
# Total Submissions: 585.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or n == 1:
            return head
        h1 = ListNode(0)
        h1.next = head
        fast = h1
        for _ in range(n - m + 1):
            fast = fast.next
        slow = h1
        for _ in range(m - 1):
            slow = slow.next
            fast = fast.next
        next = fast.next
        fast.next = None
        newhead = slow.next
        slow.next = None
        slow.next, tail = self.reverselist(newhead)
        tail.next = next
        return h1.next

    def reverselist(self, head):

        prev = None
        tail = head

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev, tail
