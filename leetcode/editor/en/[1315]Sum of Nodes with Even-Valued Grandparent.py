# Given the root of a binary tree, return the sum of values of nodes with an 
# even-valued grandparent. If there are no nodes with an even-valued grandparent, 
# return 0. 
# 
#  A grandparent of a node is the parent of its parent if it exists. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while 
# the blue nodes are the even-value grandparents.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  1 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 25
# 29 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0

        def dfs(g, p):
            if not p:
                return None
            nonlocal total
            if g.val % 2 == 0:
                if p.left:
                    total += p.left.val
                if p.right:
                    total += p.right.val
            dfs(p, p.left)
            dfs(p, p.right)

        dfs(root, root.left)
        dfs(root, root.right)
        return total
# leetcode submit region end(Prohibit modification and deletion)
