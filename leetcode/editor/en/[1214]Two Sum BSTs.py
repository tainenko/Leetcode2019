# Given the roots of two binary search trees, root1 and root2, return true if 
# and only if there is a node in the first tree and a node in the second tree whose 
# values sum up to a given integer target. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
# Output: true
# Explanation: 2 and 3 sum up to 5.
#  
# 
#  Example 2: 
#  
#  
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each tree is in the range [1, 5000]. 
#  -10⁹ <= Node.val, target <= 10⁹ 
#  
# 
#  Related Topics Two Pointers Binary Search Stack Tree Depth-First Search 
# Binary Search Tree Binary Tree 👍 451 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        dct = set()

        def dfs(node):
            if not node:
                return
            dct.add(target - node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root1)

        def find(node):
            if not node:
                return False
            if node.val in dct:
                return True
            return find(node.left) or find(node.right)

        return find(root2)
# leetcode submit region end(Prohibit modification and deletion)
