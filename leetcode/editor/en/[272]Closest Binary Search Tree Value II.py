# Given the root of a binary search tree, a target value, and an integer k, 
# return the k values in the BST that are closest to the target. You may return the 
# answer in any order. 
# 
#  You are guaranteed to have only one unique set of k values in the BST that 
# are closest to the target. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1], target = 0.000000, k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is n. 
#  1 <= k <= n <= 10⁴. 
#  0 <= Node.val <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  
#  Follow up: Assume that the BST is balanced. Could you solve it in less than 
# O(n) runtime (where n = total nodes)? 
# 
#  Related Topics Two Pointers Stack Tree Depth-First Search Binary Search Tree 
# Heap (Priority Queue) Binary Tree 👍 1248 👎 41
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = deque()

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if len(res) < k:
                res.append(root.val)
            else:
                if abs(target - root.val) > abs(target - res[0]):
                    return
                else:
                    res.append(root.val)
                    res.popleft()
            dfs(root.right)

        dfs(root)
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)
