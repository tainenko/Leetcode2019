#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (38.03%)
# Total Accepted:    158.7K
# Total Submissions: 414.4K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
# 
# 
# 
# 
# 
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
# 
# 
# 
# 
# 
# Algorithm of Insertion Sort:
# 
# 
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.val < curr.next.val:
                curr = curr.next
            else:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                next = curr.next
                curr.next = curr.next.next
                next.next = pre.next
                pre.next = next
        return dummy.next
