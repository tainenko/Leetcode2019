#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (38.06%)
# Total Accepted:    174.3K
# Total Submissions: 457.3K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(None)
        h2 = ListNode(None)
        l2 = h2
        h1.next = head
        head = h1
        while head and head.next:
            if head.next.val >= x:
                l2.next = head.next
                l2 = l2.next
                head.next = head.next.next
                continue
            head = head.next
        l2.next = None
        head.next = h2.next
        head = h1.next
        del h1
        del h2
        return head
