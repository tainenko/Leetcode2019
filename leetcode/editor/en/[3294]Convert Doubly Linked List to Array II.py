# You are given an arbitrary node from a doubly linked list, which contains 
# nodes that have a next pointer and a previous pointer. 
# 
#  Return an integer array which contains the elements of the linked list in 
# order. 
# 
#  
#  Example 1: 
# 
#  
#  Input: head = [1,2,3,4,5], node = 5 
#  
# 
#  Output: [1,2,3,4,5] 
# 
#  Example 2: 
# 
#  
#  Input: head = [4,5,6,7,8], node = 8 
#  
# 
#  Output: [4,5,6,7,8] 
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given list is in the range [1, 500]. 
#  1 <= Node.val <= 1000 
#  All nodes have unique Node.val. 
#  
# 
#  Related Topics Array Linked List Doubly-Linked List 👍 7 👎 5


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        head = []
        tail = []
        curr = node
        while curr:
            tail.append(curr.val)
            curr = curr.next
        prev = node.prev
        while prev:
            head.append(prev.val)
            prev = prev.prev
        return head[::-1] + tail
# leetcode submit region end(Prohibit modification and deletion)
