#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (33.77%)
# Total Accepted:    195.1K
# Total Submissions: 576.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = ListNode(None)
        prev.next = head
        newhead = prev
        while prev and prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                while prev.next.next and prev.next.val == prev.next.next.val:
                    prev.next.next = prev.next.next.next
                prev.next = prev.next.next
                continue
            prev = prev.next
        return newhead.next
