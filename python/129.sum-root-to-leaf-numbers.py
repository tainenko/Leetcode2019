#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/total-root-to-leaf-numbers/description/
#
# algorithms
# Medium (43.35%)
# Total Accepted:    198.8K
# Total Submissions: 456.5K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total total of all root-to-leaf numbers.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, total = 12 + 13 = 25.
# 
# Example 2:
# 
# 
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, total = 495 + 491 + 40 = 1026.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root,total):
            if not root:
                return 0
            total=total*10+root.val
            if not root.left and not root.right:
                return total
            return helper(root.left,total)+helper(root.right,total)
        return helper(root,0)

    def bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total = 0
        q = [(root, root.val)]
        while q:
            curr, tmp = q.pop(0)
            if not curr.left and not curr.right:
                total += tmp
            if curr.left:
                q.append((curr.left, tmp * 10 + curr.left.val))
            if curr.right:
                q.append((curr.right, tmp * 10 + curr.right.val))
        return total
