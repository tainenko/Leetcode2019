#
# @lc app=leetcode id=310 lang=python
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (30.61%)
# Likes:    1264
# Dislikes: 76
# Total Accepted:    76.5K
# Total Submissions: 246.1K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
# Example 1 :
# 
# 
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3 
# 
# Output: [1]
# 
# 
# Example 2 :
# 
# 
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5 
# 
# Output: [3, 4]
# 
# Note:
# 
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
#

# @lc code=start
import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        leaves = [set() for _ in range(n)]
        for edge in edges:
            leaves[edge[0]].add(edge[1])
            leaves[edge[1]].add(edge[0])
        que = collections.deque()
        for i in range(len(leaves)):
            if len(leaves[i]) == 1:
                que.append(i)

        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                v = que.popleft()
                for leaf in leaves[v]:
                    leaves[leaf].remove(v)
                    if len(leaves[leaf]) == 1:
                        que.append(leaf)

        return list(que)
# @lc code=end
