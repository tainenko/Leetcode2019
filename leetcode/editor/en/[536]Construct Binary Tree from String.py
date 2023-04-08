# You need to construct a binary tree from a string consisting of parenthesis
# and integers.
#
#  The whole input represents a binary tree. It contains an integer followed by
# zero, one or two pairs of parenthesis. The integer represents the root's value
# and a pair of parenthesis contains a child binary tree with the same structure.
#
#  You always start to construct the left child node of the parent first if it
# exists.
#
#
#  Example 1:
#
#
# Input: s = "4(2(3)(1))(6(5))"
# Output: [4,2,6,3,1,5]
#
#
#  Example 2:
#
#
# Input: s = "4(2(3)(1))(6(5)(7))"
# Output: [4,2,6,3,1,5,7]
#
#
#  Example 3:
#
#
# Input: s = "-4(2(3)(1))(6(5)(7))"
# Output: [-4,2,6,3,1,5,7]
#
#
#
#  Constraints:
#
#
#  0 <= s.length <= 3 * 10⁴
#  s consists of digits, '(', ')', and '-' only.
#
#
#  Related Topics String Tree Depth-First Search Binary Tree 👍 985 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        val = ""
        i = 0
        for i in range(len(s)):
            if s[i] == "(":
                break
            val += s[i]
        root = TreeNode(val=int(val))
        if i != len(s) - 1:
            tmp = 0
            end = 0
            for j in range(i, len(s)):
                if s[j] == "(":
                    tmp += 1
                elif s[j] == ")":
                    tmp -= 1
                    if tmp == 0:
                        end = j
                        break
            root.left = self.str2tree(s[i + 1:end])
            root.right = self.str2tree(s[end + 2:-1])

        return root

# leetcode submit region end(Prohibit modification and deletion)
