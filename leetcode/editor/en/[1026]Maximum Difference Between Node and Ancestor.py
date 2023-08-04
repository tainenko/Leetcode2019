# Given the root of a binary tree, find the maximum value v for which there 
# exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b. 
# 
#  A node a is an ancestor of b if either: any child of a is equal to b or any 
# child of a is an ancestor of b. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are 
# given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| 
# = 7. 
# 
#  Example 2: 
#  
#  
# Input: root = [1,null,2,null,0,3]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 5000]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 4094 👎 97


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, high, low):
            if not root:
                return
            nonlocal res

            high = max(root.val, high)
            low = min(root.val, low)
            
            res = max(abs(high - root.val), abs(low - root.val), res)
            dfs(root.left, high, low)
            dfs(root.right, high, low)

        dfs(root, root.val, root.val)
        return res

# leetcode submit region end(Prohibit modification and deletion)
