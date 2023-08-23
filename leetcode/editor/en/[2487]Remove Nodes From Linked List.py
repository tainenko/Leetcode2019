# You are given the head of a linked list. 
# 
#  Remove every node which has a node with a strictly greater value anywhere to 
# the right side of it. 
# 
#  Return the head of the modified linked list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the given list is in the range [1, 10⁵]. 
#  1 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Linked List Stack Recursion Monotonic Stack 👍 1048 👎 33


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=float('inf'), next=head)
        stack = [dummy]
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
        return stack[0].next
# leetcode submit region end(Prohibit modification and deletion)
