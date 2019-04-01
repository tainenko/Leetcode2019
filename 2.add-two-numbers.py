# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        target=(l1.val+l2.val)
        result=ListNode(target%10)
        result.next=self.addTwoNumbers(l1.next,l2.next)
        if target>9:
            result.next=self.addTwoNumbers(result.next,ListNode(1))
        l1=l1.next
        l2=l2.next
        return result


