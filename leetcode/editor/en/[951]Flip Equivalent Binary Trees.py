# For a binary tree T, we can define a flip operation as follows: choose any 
# node, and swap the left and right child subtrees. 
# 
#  A binary tree X is flip equivalent to a binary tree Y if and only if we can 
# make X equal to Y after some number of flip operations. 
# 
#  Given the roots of two binary trees root1 and root2, return true if the two 
# trees are flip equivalent or false otherwise. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,
# null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [], root2 = []
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: root1 = [], root2 = [1]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each tree is in the range [0, 100]. 
#  Each tree will have unique node values in the range [0, 99]. 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 2857 👎 119


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def compare(root1, root2):
            if root1 == root2 or (root1 is None and root2 is None):
                return True
            elif root1 is None or root2 is None or root1.val != root2.val:
                return False
            return (compare(root1.left, root2.left) and compare(root1.right, root2.right)) or (
                        compare(root1.left, root2.right) and compare(root1.right, root2.left))

        return compare(root1, root2)
# leetcode submit region end(Prohibit modification and deletion)
