#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (42.44%)
# Total Accepted:    424.4K
# Total Submissions: 990.1K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.setzero_islands(grid, i, j)

        return count

    def setzero_islands(self, grid, i, j):
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid[i][j] = "0"
        for x, y in dir:
            if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][y + j] == "1":
                self.setzero_islands(grid, i + x, y + j)
