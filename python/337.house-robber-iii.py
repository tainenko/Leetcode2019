#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (48.63%)
# Likes:    1892
# Dislikes: 38
# Total Accepted:    123.9K
# Total Submissions: 251.5K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# 
# Input: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
# @lc code=end
