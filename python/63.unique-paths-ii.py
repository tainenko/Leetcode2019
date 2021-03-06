#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.61%)
# Total Accepted:    216.3K
# Total Submissions: 643.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        grid = [[0] * m for _ in range(n)]
        grid[0][0] = 1
        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    if row > 0:
                        grid[row][col] += grid[row - 1][col]
                    if col > 0:
                        grid[row][col] += grid[row][col - 1]
        return grid[-1][-1]
