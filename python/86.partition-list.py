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
        if not head or not head.next:
            return head
        small = None
        big = None
        small_head = big_head = None
        first = head
        while head:
            if head.val < x:
                if not small:
                    small = head
                    small_head = head
                else:
                    small.next = head
                    small = small.next
            else:
                if not big:
                    big = head
                    big_head = big
                else:
                    big.next = head
                    big = big.next
            head = head.next
        if small:
            small.next = big_head
        if big:
            big.next = None
        return small_head if small_head else big_head
