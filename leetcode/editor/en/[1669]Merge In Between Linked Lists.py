# You are given two linked lists: list1 and list2 of sizes n and m respectively.
#  
# 
#  Remove list1's nodes from the aᵗʰ node to the bᵗʰ node, and put list2 in 
# their place. 
# 
#  The blue edges and nodes in the following figure indicate the result: 
#  
#  Build the result list and return its head. 
# 
#  
#  Example 1: 
#  
#  
# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their 
# place. The blue edges and nodes in the above figure indicate the result.
#  
# 
#  Example 2: 
#  
#  
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002
# ,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= list1.length <= 10⁴ 
#  1 <= a <= b < list1.length - 1 
#  1 <= list2.length <= 10⁴ 
#  
# 
#  Related Topics Linked List 👍 1379 👎 174


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = tail = list1
        for _ in range(a - 1):
            head = head.next
        for _ in range(b):
            tail = tail.next
        head.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = tail.next
        return list1
# leetcode submit region end(Prohibit modification and deletion)
