# Given the root of a binary tree, find the largest subtree, which is also a 
# Binary Search Tree (BST), where the largest means subtree has the largest number 
# of nodes. 
# 
#  A Binary Search Tree (BST) is a tree in which all the nodes follow the below-
# mentioned properties: 
# 
#  
#  The left subtree values are less than the value of their parent (root) 
# node's value. 
#  The right subtree values are greater than the value of their parent (root) 
# node's value. 
#  
# 
#  Note: A subtree must include all of its descendants. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [10,5,15,1,8,null,7]
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one. The 
# return value is the subtree's size, which is 3. 
# 
#  Example 2: 
# 
#  
# Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  
#  Follow up: Can you figure out ways to solve it with O(n) time complexity? 
# 
#  Related Topics Dynamic Programming Tree Depth-First Search Binary Search 
# Tree Binary Tree 👍 1379 👎 110


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MIN = -2147483647
MAX = 2147483647


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[2]

    def helper(self, node):
        if not node:
            return MAX, MIN, 0
        l_min, l_max, l_depth = self.helper(node.left)
        r_min, r_max, r_depth = self.helper(node.right)
        if l_max < node.val < r_min:
            return min(l_min, node.val), max(r_max, node.val), l_depth + r_depth + 1
        return MIN, MAX, max(l_depth, r_depth)

# leetcode submit region end(Prohibit modification and deletion)
