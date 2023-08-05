# Given the head of a linked list head, in which each node contains an integer 
# value. 
# 
#  Between every pair of adjacent nodes, insert a new node with a value equal 
# to the greatest common divisor of them. 
# 
#  Return the linked list after insertion. 
# 
#  The greatest common divisor of two numbers is the largest positive integer 
# that evenly divides both numbers. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1ˢᵗ diagram denotes the initial linked list and the 2ⁿᵈ 
# diagram denotes the linked list after inserting the new nodes (nodes in blue are the 
# inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1ˢᵗ and 
# the 2ⁿᵈ nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2ⁿᵈ and 
# the 3ʳᵈ nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3ʳᵈ and 
# the 4ᵗʰ nodes.
# There are no more adjacent nodes, so we return the linked list.
#  
# 
#  Example 2: 
#  
#  
# Input: head = [7]
# Output: [7]
# Explanation: The 1ˢᵗ diagram denotes the initial linked list and the 2ⁿᵈ 
# diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 5000]. 
#  1 <= Node.val <= 1000 
#  
# 
#  👍 34 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            bcd = self.bcd(curr.val, curr.next.val)
            new = ListNode(val=bcd, next=curr.next)
            curr.next = new
            curr = curr.next.next
        return head

    def bcd(self, a, b):
        if a % b == 0:
            return b
        return self.bcd(b, a % b)
# leetcode submit region end(Prohibit modification and deletion)
