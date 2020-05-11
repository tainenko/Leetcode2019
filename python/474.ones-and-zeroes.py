#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (42.23%)
# Likes:    869
# Dislikes: 215
# Total Accepted:    44.4K
# Total Submissions: 105.2K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# Given an array, strs, with strings consisting of only 0s and 1s. Also two
# integers m and n.
# 
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are "10","0001","1","0".
# 
# 
# Example 2:
# 
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for _str in strs:
            zero = 0
            one = 0
            for s in _str:
                if s == "0":
                    zero += 1
                else:
                    one += 1
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[-1][-1]

# @lc code=end
