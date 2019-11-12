#
# @lc app=leetcode id=304 lang=python
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (33.40%)
# Likes:    611
# Dislikes: 149
# Total Accepted:    87.1K
# Total Submissions: 249.2K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
'[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'


#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# 
# 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
# 
# 
# Example:
# 
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# Note:
# 
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = [[]]
        else:
            self.matrix = self.compute_sum_matrix(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        area1 = self.matrix[row2][col2]
        area2 = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        area3 = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        area4 = self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return area1 - area2 - area3 + area4

    def compute_sum_matrix(self, matrix):
        if not matrix:
            return [0]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            matrix[i][0] += matrix[i - 1][0]
        for j in range(1, n):
            matrix[0][j] += matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        return matrix

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
