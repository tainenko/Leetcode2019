# Given a non-negative integer represented as a linked list of digits, plus one 
# to the integer. 
# 
#  The digits are stored such that the most significant digit is at the head of 
# the list. 
# 
#  
#  Example 1: 
#  Input: head = [1,2,3]
# Output: [1,2,4]
#  
#  Example 2: 
#  Input: head = [0]
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  The number of nodes in the linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  The number represented by the linked list does not contain leading zeros 
# except for the zero itself. 
#  
# 
#  Related Topics Linked List Math 👍 866 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
# leetcode submit region end(Prohibit modification and deletion)
