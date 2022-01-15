# Given the root of a binary tree, return the number of uni-value subtrees. 
# 
#  A uni-value subtree means all nodes of the subtree have the same value. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [5,1,5,5,5,null,5]
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: root = [5,5,5,5,5,null,5]
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the node in the tree will be in the range [0, 1000]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Depth-First Search Binary Tree 👍 870 👎 266


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def helper(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            left = helper(root.left)
            right = helper(root.right)
            if left is False or right is False:
                return False
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            nonlocal count
            count += 1
            return True

        helper(root)
        return count

# leetcode submit region end(Prohibit modification and deletion)
