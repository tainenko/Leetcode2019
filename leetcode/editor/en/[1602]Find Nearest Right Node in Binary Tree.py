# Given the root of a binary tree and a node u in the tree, return the nearest 
# node on the same level that is to the right of u, or return null if u is the 
# rightmost node in its level. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,null,4,5,6], u = 4
# Output: 5
# Explanation: The nearest node on the same level to the right of node 4 is 
# node 5.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [3,null,4,2], u = 2
# Output: null
# Explanation: There are no nodes to the right of 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁵]. 
#  1 <= Node.val <= 10⁵ 
#  All values in the tree are distinct. 
#  u is a node in the binary tree rooted at root. 
#  
# 
#  Related Topics Tree Breadth-First Search Binary Tree 👍 315 👎 10


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = [root]
        while q:
            next_ = []
            for i, node in enumerate(q):
                if node == u:
                    if i + 1 < len(q):
                        return q[i + 1]
                    else:
                        return None
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            q = next_
        return None

# leetcode submit region end(Prohibit modification and deletion)
