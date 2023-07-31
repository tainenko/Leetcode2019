# Given the root of a binary search tree, return a balanced binary search tree 
# with the same node values. If there is more than one answer, return any of them. 
# 
# 
#  A binary search tree is balanced if the depth of the two subtrees of every 
# node never differs by more than 1. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also 
# correct.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [2,1,3]
# Output: [2,1,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  1 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Divide and Conquer Greedy Tree Depth-First Search Binary 
# Search Tree Binary Tree 👍 2752 👎 67


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            nodes.append(root.val)
            if root.right:
                dfs(root.right)

        def build(i, j):
            if i > j:
                return
            mid = i + (j - i) // 2
            root = TreeNode(nodes[mid])
            root.left = build(i, mid - 1)
            root.right = build(mid + 1, j)
            return root

        dfs(root)
        return build(0, len(nodes) - 1)
# leetcode submit region end(Prohibit modification and deletion)
