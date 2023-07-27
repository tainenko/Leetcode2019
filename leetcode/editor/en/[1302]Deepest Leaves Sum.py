# Given the root of a binary tree, return the sum of values of its deepest 
# leaves.
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
#  
# 
#  Example 2: 
# 
#  
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
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
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 43
# 92 👎 113


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        while True:
            nexts = []
            for node in nodes:
                if node.left:
                    nexts.append(node.left)
                if node.right:
                    nexts.append(node.right)
            if not nexts:
                return sum(node.val for node in nodes)
            nodes = nexts

# leetcode submit region end(Prohibit modification and deletion)
