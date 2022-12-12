# Given the root of a binary tree, return the vertical order traversal of its 
# nodes' values. (i.e., from top to bottom, column by column). 
# 
#  If two nodes are in the same row and column, the order should be from left 
# to right. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
#  
# 
#  Example 2: 
#  
#  
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
#  
# 
#  Example 3: 
#  
#  
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Hash Table Tree Depth-First Search Breadth-First Search 
# Binary Tree 👍 2830 👎 289


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dct = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            node, pos = q.popleft()
            dct[pos].append(node.val)
            if node.left:
                q.append((node.left, pos - 1))
            if node.right:
                q.append((node.right, pos + 1))
        res = [None] * len(dct)
        b = - min(dct.keys())
        for k, v in dct.items():
            res[k + b] = v
        return res
# leetcode submit region end(Prohibit modification and deletion)
