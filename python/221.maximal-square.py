#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (33.75%)
# Likes:    1647
# Dislikes: 41
# Total Accepted:    153.8K
# Total Submissions: 449.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1

# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
        for i in range(n):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '0':
                    continue
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return max(map(max, dp)) ** 2

# @lc code=end
