# Given the root of a binary tree, return true if you can partition the tree 
# into two trees with equal sums of values after removing exactly one edge on the 
# original tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,10,10,null,null,2,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,10,null,null,2,20]
# Output: false
# Explanation: You cannot split the tree into two trees with equal sums after 
# removing exactly one edge on the tree.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 475 👎 37


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)
