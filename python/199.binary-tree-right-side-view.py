#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (48.96%)
# Total Accepted:    192.3K
# Total Submissions: 388.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            next = collections.deque()
            res.append(q[0].val)
            while q:
                curr = q.popleft()
                if curr.right:
                    next.append(curr.right)
                if curr.left:
                    next.append(curr.left)
            q = next
        return res
