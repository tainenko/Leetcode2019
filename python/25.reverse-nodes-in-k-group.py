#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (40.52%)
# Likes:    2647
# Dislikes: 370
# Total Accepted:    290.3K
# Total Submissions: 678.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        curr = head
        i = 0
        while curr != None:
            i += 1
            if i % k == 0:
                self.reverse_one_group(pre, curr.next)
                curr = pre.next
            else:
                curr = curr.next
        return dummy.next

    def reverse_one_group(self, pre, next):
        last = pre.next
        curr = last.next
        while curr != next:
            last.next = curr.next
            curr.next = pre.next
            pre.next = curr
            curr = last.next
        return last

# @lc code=end
