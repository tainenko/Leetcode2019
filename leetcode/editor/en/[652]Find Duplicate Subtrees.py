# Given the root of a binary tree, return all duplicate subtrees. 
# 
#  For each kind of duplicate subtrees, you only need to return the root node of
#  any one of them. 
# 
#  Two trees are duplicate if they have the same structure with the same node va
# lues. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,1]
# Output: [[1]]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the tree will be in the range [1, 10^4] 
#  -200 <= Node.val <= 200 
#  
#  Related Topics Tree 
#  👍 2016 👎 244


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        map = defaultdict(int)
        res = []
        self.helper(root, map, res)
        return res

    def helper(self, root, map, res):
        if not root:
            return "#"
        s = ','.join([str(root.val), self.helper(root.left, map, res), self.helper(root.right, map, res)])
        if map[s] == 1:
            res.append(root)
        map[s] += 1
        return s
# leetcode submit region end(Prohibit modification and deletion)
