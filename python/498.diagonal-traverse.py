#
# @lc app=leetcode id=498 lang=python
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (47.17%)
# Likes:    710
# Dislikes: 327
# Total Accepted:    80.7K
# Total Submissions: 169.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        dirs = [(-1, 1), (1, -1)]
        row, col = 0, 0
        k = 0
        for i in range(len(matrix) * len(matrix[0])):
            res.append(matrix[row][col])
            row += dirs[k][0]
            col += dirs[k][1]
            if row >= len(matrix):
                row = len(matrix) - 1
                col += 2
                k = 1 - k
            if col >= len(matrix[0]):
                col = len(matrix[0]) - 1
                row += 2
                k = 1 - k
            if row < 0:
                row = 0
                k = 1 - k
            if col < 0:
                col = 0
                k = 1 - k

        return res

# @lc code=end
