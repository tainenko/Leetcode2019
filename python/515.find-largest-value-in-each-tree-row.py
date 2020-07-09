#
# @lc app=leetcode id=515 lang=python
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (60.17%)
# Likes:    859
# Dislikes: 61
# Total Accepted:    99.6K
# Total Submissions: 163.5K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            highest = float('-inf')
            next = []
            for node in q:
                highest = max(highest, node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(highest)
            q = next
        return res

# @lc code=end
