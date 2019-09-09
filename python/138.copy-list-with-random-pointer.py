#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (28.24%)
# Total Accepted:    273.2K
# Total Submissions: 954.8K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        p = head

        while p:
            tmp = Node(p.val, None, None)
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

        p = head
        q = head.next
        while p:
            if p.random:
                q.random = p.random.next
            p = p.next.next
            if q.next:
                q = q.next.next

        header = head.next
        p = head
        q = header

        while p:
            if not q.next:
                break
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = None
        return header

    def copyRandomList_outerspace(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        header = Node(0, None, None)
        p = header
        q = head
        dct = {}
        while q:
            tmp = Node(q.val, None, None)
            dct[q] = tmp
            p.next = tmp
            p = p.next
            q = q.next

        p = header.next
        q = head
        while q:
            if q.random:
                p.random = dct[q.random]
            p = p.next
            q = q.next
        return header.next
