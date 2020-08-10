#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (38.92%)
# Likes:    1544
# Dislikes: 108
# Total Accepted:    90.5K
# Total Submissions: 227.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# 
# Example 1: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
# 
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
# 
# 
# Example 2: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
# 
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
# 
# 
# 
# 
# Note:
# 
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i][j] != 0 and res[i][j] != 1:
                    if i < m - 1:
                        res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                    if j < n - 1:
                        res[i][j] = min(res[i][j], res[i][j + 1] + 1)
        return res

# @lc code=end
