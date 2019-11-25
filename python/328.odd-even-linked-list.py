#
# @lc app=leetcode id=328 lang=python
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (50.03%)
# Likes:    1032
# Dislikes: 251
# Total Accepted:    180.2K
# Total Submissions: 352.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        even = head
        odd = head.next
        odd_head = head.next
        while even.next and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        even.next = odd_head
        return head

# @lc code=end
