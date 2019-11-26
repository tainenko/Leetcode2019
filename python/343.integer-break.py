#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (48.30%)
# Likes:    713
# Dislikes: 193
# Total Accepted:    91.4K
# Total Submissions: 186.9K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
# 
# Example 1:
# 
# 
# 
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# Note: You may assume that n is not less than 2 and not larger than 58.
# 
# 
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
# @lc code=end
