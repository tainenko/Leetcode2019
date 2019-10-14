#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (35.68%)
# Likes:    1269
# Dislikes: 155
# Total Accepted:    150.4K
# Total Submissions: 399.7K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)

    def get_height(self, root):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def force_countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            count += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return count

# @lc code=end
