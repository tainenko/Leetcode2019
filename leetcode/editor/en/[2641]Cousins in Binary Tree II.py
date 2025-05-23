# Given the root of a binary tree, replace the value of each node in the tree 
# with the sum of all its cousins' values. 
# 
#  Two nodes of a binary tree are cousins if they have the same depth with 
# different parents. 
# 
#  Return the root of the modified tree. 
# 
#  Note that the depth of a node is the number of edges in the path from the 
# root node to it. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary 
# tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary 
# tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁵]. 
#  1 <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Hash Table Tree Depth-First Search Breadth-First Search 
# Binary Tree 👍 447 👎 6


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while q:
            t = []
            total = 0
            for node in q:
                if node.left:
                    t.append(node.left)
                    total += node.left.val
                if node.right:
                    t.append(node.right)
                    total += node.right.val
            for node in q:
                sub = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = total - sub
                if node.right:
                    node.right.val = total - sub
            q = t
        return root
# leetcode submit region end(Prohibit modification and deletion)
