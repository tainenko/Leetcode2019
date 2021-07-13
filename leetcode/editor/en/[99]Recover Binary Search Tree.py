# You are given the root of a binary search tree (BST), where exactly two nodes 
# of the tree were swapped by mistake. Recover the tree without changing its struc
# ture. 
# 
#  Follow up: A solution using O(n) space is pretty straight forward. Could you 
# devise a constant space solution? 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 mak
# es the BST valid.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 a
# nd 3 makes the BST valid.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 1000]. 
#  -231 <= Node.val <= 231 - 1 
#  
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 
#  👍 2776 👎 105


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        vals = []
        self.inorder_traverse(root, nodes, vals)
        vals.sort()
        for node, val in zip(nodes, vals):
            node.val = val

    def inorder_traverse(self, root, nodes, vals):
        if not root:
            return
        self.inorder_traverse(root.left, nodes, vals)
        nodes.append(root)
        vals.append(root.val)
        self.inorder_traverse(root.right, nodes, vals)

# leetcode submit region end(Prohibit modification and deletion)
