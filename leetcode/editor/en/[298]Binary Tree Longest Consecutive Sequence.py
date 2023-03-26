# Given the root of a binary tree, return the length of the longest consecutive
# sequence path.
#
#  The path refers to any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections. The longest consecutive path
# needs to be from parent to child (cannot be the reverse).
#
#
#  Example 1:
#
#
# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
#
#
#  Example 2:
#
#
# Input: root = [2,null,3,2,null,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
#
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [1, 3 * 10⁴].
#  -3 * 10⁴ <= Node.val <= 3 * 10⁴
#
#  Related Topics Tree Depth-First Search Binary Tree 👍 872 👎 211


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root, 1, 1)

    def dfs(self, prev: Optional[TreeNode], node: Optional[TreeNode], curr: int, longest: int) -> int:
        if not node:
            return longest
        if prev.val == node.val - 1:
            curr += 1
            longest = max(curr, longest)
        else:
            curr = 1
        return max(self.dfs(node, node.left, curr, longest), self.dfs(node, node.right, curr, longest))
# leetcode submit region end(Prohibit modification and deletion)
