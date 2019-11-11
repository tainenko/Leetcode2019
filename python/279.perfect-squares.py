#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (42.76%)
# Likes:    1837
# Dislikes: 156
# Total Accepted:    220.5K
# Total Submissions: 507.8K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
import math


# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return dp[-1]

    def math_numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = n
        while tmp & 3 == 0:
            tmp >>= 2
        if tmp % 8 == 7:
            return 4

        index = int(math.sqrt(n))
        while index:
            tmp = n - index ** 2
            sqrt_tmp = int(math.sqrt(tmp))
            if n == sqrt_tmp ** 2 + index ** 2:
                return 1 if sqrt_tmp == 0 else 2
            index -= 1
        return 3
# @lc code=end
