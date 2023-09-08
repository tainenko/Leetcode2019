# Given the root of a binary tree, return the maximum average value of a 
# subtree of that tree. Answers within 10⁻⁵ of the actual answer will be accepted. 
# 
#  A subtree of a tree is any node of that tree plus all its descendants. 
# 
#  The average value of a tree is the sum of its values, divided by the number 
# of nodes. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,6,1]
# Output: 6.00000
# Explanation: 
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0,null,1]
# Output: 1.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 777 👎 33


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0

        def dfs(root, total, n):
            if not root:
                return 0, 0
            l_total, l_n = dfs(root.left, total, n)
            r_total, r_n = dfs(root.right, total, n)
            nonlocal res
            res = max(res, (root.val + l_total + r_total) / (1 + l_n + r_n))
            return root.val + l_total + r_total, 1 + l_n + r_n

        dfs(root, 0, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
