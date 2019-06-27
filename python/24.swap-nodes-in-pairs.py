'''
[24] Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/description/

* algorithms
* Medium (44.98%)
* Source Code:       24.swap-nodes-in-pairs.py
* Total Accepted:    323.7K
* Total Submissions: 718.4K
* Testcase Example:  '[1,2,3,4]'

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:


Given 1->2->3->4, you should return the list as 2->1->4->3.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        first=ListNode(0)
        first.next=head
        prev=first
        curr=head
        while curr and curr.next:
            keep = curr.next.next
            curr.next.next=curr
            prev.next=curr.next
            curr.next=keep
            prev=curr
            curr=curr.next
        return first.next
        
