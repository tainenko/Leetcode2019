# Given the root of a binary tree, return the length of the longest consecutive 
# path in the tree. 
# 
#  A consecutive path is a path where the values of the consecutive nodes in 
# the path differ by one. This path can be either increasing or decreasing. 
# 
#  
#  For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path 
# [1,2,4,3] is not valid. 
#  
# 
#  On the other hand, the path can be in the child-Parent-child order, where 
# not necessarily be parent-child order. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3]
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
#  
# 
#  Example 2: 
#  
#  
# Input: root = [2,1,3]
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 10⁴]. 
#  -3 * 10⁴ <= Node.val <= 3 * 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 1089 👎 87


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max((self.dfs(root, 1) + self.dfs(root, -1) + 1), self.longestConsecutive(root.left),
                   self.longestConsecutive(root.right))

    def dfs(self, node, diff):
        if not node:
            return 0
        left, right = 0, 0
        if node.left and (node.val - node.left.val) == diff:
            left = 1 + self.dfs(node.left, diff)
        if node.right and (node.val - node.right.val) == diff:
            right = 1 + self.dfs(node.right, diff)
        return max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
