# You are given the root of a binary tree with n nodes. Each node is uniquely 
# assigned a value from 1 to n. You are also given an integer startValue 
# representing the value of the start node s, and a different integer destValue representing 
# the value of the destination node t. 
# 
#  Find the shortest path starting from node s and ending at node t. Generate 
# step-by-step directions of such path as a string consisting of only the uppercase 
# letters 'L', 'R', and 'U'. Each letter indicates a specific direction: 
# 
#  
#  'L' means to go from a node to its left child node. 
#  'R' means to go from a node to its right child node. 
#  'U' means to go from a node to its parent node. 
#  
# 
#  Return the step-by-step directions of the shortest path from node s to node 
# t. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is n. 
#  2 <= n <= 10⁵ 
#  1 <= Node.val <= n 
#  All the values in the tree are unique. 
#  1 <= startValue, destValue <= n 
#  startValue != destValue 
#  
# 
#  Related Topics String Tree Depth-First Search Binary Tree 👍 2042 👎 100


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path = []
        dest_path = []

        def dfs(node, path):
            if node.val == startValue:
                nonlocal start_path
                start_path = path[:]
            if node.val == destValue:
                nonlocal dest_path
                dest_path = path[:]
            if node.left:
                path.append(node.left)
                dfs(node.left, path)
                path.pop()
            if node.right:
                path.append(node.right)
                dfs(node.right, path)
                path.pop()

        dfs(root, [root])
        p = min(len(start_path), len(dest_path)) - 1
        while start_path[p] != dest_path[p]:
            p -= 1
        start_path = start_path[p:]
        dest_path = dest_path[p:]
        res = "U" * (len(start_path) - 1)
        for i in range(len(dest_path) - 1):
            if dest_path[i].left == dest_path[i + 1]:
                res += "L"
            else:
                res += "R"
        return res
# leetcode submit region end(Prohibit modification and deletion)
