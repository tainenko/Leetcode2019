"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        [559] Maximum Depth of N-ary Tree

        https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

        * algorithms
        * Easy (64.87%)
        * Source Code:       559.maximum-depth-of-n-ary-tree.py
        * Total Accepted:    39.7K
        * Total Submissions: 61.1K
        * Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'

        Given a n-ary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        For example, given a 3-ary tree:

        We should return its max depth, which is 3.

        Note:

            The depth of the tree is at most 1000.
            The total number of nodes is at most 5000.

        """
        if not root:
            return 0
        if not root.children:
            return 1
        height=1
        for child in root.children:
            height=max(height,self.maxDepth(child)+1)
        return height
