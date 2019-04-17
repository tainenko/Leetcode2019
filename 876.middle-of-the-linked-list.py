'''
[876] Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/description/

* algorithms
* Easy (63.53%)
* Source Code:       876.middle-of-the-linked-list.py
* Total Accepted:    54.5K
* Total Submissions: 85.8K
* Testcase Example:  '[1,2,3,4,5]'

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 


Example 1:


Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.



Example 2:


Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


 

Note:


        The number of nodes in the given list will be between 1 and 100.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        解題思路：暴力法。
        從頭開始遍歷並計算linked list的長度，找完後再回頭遍歷middle node
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        count=0
        while node:
            count+=1
            node=node.next
        node=head
        for _ in range(count//2):
            node=node.next

        return node

    def middleNode2(self,head):
        """
        解題思路：
        例用兩個指標fast和slow從頭遍歷，當fast走完linked list時，slow會剛好停在middle node
        時間複雜度: O(N)
        空間複雜度: O(1)

        :param head:
        :return:
        """
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
