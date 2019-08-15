#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (31.07%)
# Total Accepted:    254.5K
# Total Submissions: 819K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top < bottom and left < right:
            res += matrix[top][left:right]
            for i in range(top, bottom):
                res.append(matrix[i][right])
            res += matrix[bottom][right:left:-1]
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            top, bottom, right, left = top + 1, bottom - 1, right - 1, left + 1

        if top == bottom:
            res += matrix[top][left:right + 1]
        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
        return res
