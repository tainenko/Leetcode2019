#
# @lc app=leetcode id=993 lang=python
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.22%)
# Total Accepted:    21.8K
# Total Submissions: 41.7K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
# 
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        res = dict()
        res[root.val] = (None, 0)

        def get_node_info(root, depth):
            if not root:
                return
            if root.left:
                res[root.left.val] = (root.val, depth + 1)
            if root.right:
                res[root.right.val] = (root.val, depth + 1)
            get_node_info(root.left, depth + 1)
            get_node_info(root.right, depth + 1)

        get_node_info(root, 0)
        return res[x][1] == res[y][1] and res[x][0] != res[y][0]
