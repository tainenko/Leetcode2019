# You are given two integers m and n, which represent the dimensions of a 
# matrix. 
# 
#  You are also given the head of a linked list of integers. 
# 
#  Generate an m x n matrix that contains the integers in the linked list 
# presented in spiral order (clockwise), starting from the top-left of the matrix. If 
# there are remaining empty spaces, fill them with -1. 
# 
#  Return the generated matrix. 
# 
#  
#  Example 1: 
#  
#  
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
# 
# Note that the remaining spaces in the matrix are filled with -1.
#  
# 
#  Example 2: 
#  
#  
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to 
# right in the matrix.
# The last space in the matrix is set to -1. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 10⁵ 
#  1 <= m * n <= 10⁵ 
#  The number of nodes in the list is in the range [1, m * n]. 
#  0 <= Node.val <= 1000 
#  
# 
#  Related Topics Array Linked List Matrix Simulation 👍 622 👎 22


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        while top <= bottom and left <= right:
            for i in range(left, right):
                matrix[top][i] = head.val
                head = head.next
                if not head:
                    return matrix
            for j in range(top + 1, bottom - 1):
                matrix[j][right - 1] = head.val
                head = head.next
                if not head:
                    return matrix
            for k in range(right - 1, left, -1):
                matrix[bottom - 1][k] = head.val
                head = head.next
                if not head:
                    return matrix
            for l in range(bottom - 1, top, -1):
                matrix[l][left] = head.val
                head = head.next
                if not head:
                    return matrix
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
