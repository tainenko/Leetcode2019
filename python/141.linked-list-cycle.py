# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        [141] Linked List Cycle

        https://leetcode.com/problems/linked-list-cycle/description/

        * algorithms
        * Easy (36.27%)
        * Source Code:       141.linked-list-cycle.py
        * Total Accepted:    381.8K
        * Total Submissions: 1.1M
        * Testcase Example:  '[3,2,0,-4]\n1'

        Given a linked list, determine if it has a cycle in it.

        To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

        Example 1:

        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the second node.

        Example 2:

        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the first node.

        Example 3:

        Input: head = [1], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.

        Follow up:

        Can you solve it using O(1) (i.e. constant) memory?
        """
        visited=set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head=head.next
        return False

    def hasCycle2(self, head):
        '''
        方法二，用分別用快慢指針去traverse linked list，快指針(fast)每次走兩個節點，慢指針(slow)每次走一個節點，
        如果有circle則快指針會追上慢指針，return True，如果沒有circle則遍歷到Null時while loop會停止，return False
        :param head:
        :return:
        '''
        fast=head.next
        slow=head
        while fast and slow:
            if fast == slow:
                return True
            fast=fast.next.next
            slow=slow.next
        return head
