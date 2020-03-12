#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (38.07%)
# Likes:    987
# Dislikes: 192
# Total Accepted:    63.3K
# Total Submissions: 160K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, pacific, m, n, i, 0, -1)
            self.dfs(matrix, atlantic, m, n, i, n - 1, -1)
        for j in range(n):
            self.dfs(matrix, pacific, m, n, 0, j, -1)
            self.dfs(matrix, atlantic, m, n, m - 1, j, -1)
        res = []
        for i in range(m):
            for j in range(n):
                if True == pacific[i][j] == atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, visited, m, n, x, y, prev):
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < prev:
            return
        visited[x][y] = True
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(matrix, visited, m, n, x + i, y + j, matrix[x][y])

# @lc code=end
