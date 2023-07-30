# Given an integer n, return a list of all possible full binary trees with n 
# nodes. Each node of each tree in the answer must have Node.val == 0. 
# 
#  Each element of the answer is the root node of one possible tree. You may 
# return the final list of trees in any order. 
# 
#  A full binary tree is a binary tree where each node has exactly 0 or 2 
# children. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,
# 0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: [[0,0,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  
# 
#  Related Topics Dynamic Programming Tree Recursion Memoization Binary Tree 👍 
# 4671 👎 312


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
# leetcode submit region end(Prohibit modification and deletion)
