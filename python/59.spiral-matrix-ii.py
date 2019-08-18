#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (47.74%)
# Total Accepted:    145K
# Total Submissions: 303.4K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
import math


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[None] * n for _ in range(n)]

        left = top = 0
        right = bottom = n - 1

        num = 1
        while left < right and bottom > top:
            for i in range(left, right):
                res[top][i] = num
                num += 1
            for i in range(top, bottom):
                res[i][right] = num
                num += 1
            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][left] = num
                num += 1
            bottom -= 1
            top += 1
            left += 1
            right -= 1
        if bottom == top:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
        elif right == left:
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
        return res
