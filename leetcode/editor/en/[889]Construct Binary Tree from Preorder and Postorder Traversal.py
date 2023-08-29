# Given two integer arrays, preorder and postorder where preorder is the 
# preorder traversal of a binary tree of distinct values and postorder is the postorder 
# traversal of the same tree, reconstruct and return the binary tree. 
# 
#  If there exist multiple answers, you can return any of them. 
# 
#  
#  Example 1: 
#  
#  
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [1], postorder = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 30 
#  1 <= preorder[i] <= preorder.length 
#  All the values of preorder are unique. 
#  postorder.length == preorder.length 
#  1 <= postorder[i] <= postorder.length 
#  All the values of postorder are unique. 
#  It is guaranteed that preorder and postorder are the preorder traversal and 
# postorder traversal of the same binary tree. 
#  
# 
#  Related Topics Array Hash Table Divide and Conquer Tree Binary Tree 👍 2603 ?
# ? 104


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(val=preorder[0])

        n = len(preorder)
        if n == 1:
            return root
        
        left_node = preorder[1]
        length = postorder.index(left_node) + 1

        left = self.constructFromPrePost(preorder[1:length + 1], postorder[:length])
        right = self.constructFromPrePost(preorder[length + 1:], postorder[length:-1])
        root.left = left
        root.right = right
        return root
# leetcode submit region end(Prohibit modification and deletion)
