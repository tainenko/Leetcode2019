#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (48.07%)
# Total Accepted:    251K
# Total Submissions: 522K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            for col in range(m):
                if row > 0 and col > 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
                elif row > 0:
                    grid[row][col] += grid[row - 1][col]
                elif col > 0:
                    grid[row][col] += grid[row][col - 1]
        return grid[-1][-1]
