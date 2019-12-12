#
# @lc app=leetcode id=357 lang=python
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (47.28%)
# Likes:    304
# Dislikes: 713
# Total Accepted:    68.9K
# Total Submissions: 144.5K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10^n.
# 
# 
# Example:
# 
# 
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99
# 
# 
#

# @lc code=start
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        product = 1
        res = 1
        for i in range(min(n, 10)):
            product *= nums[i]
            res += product
        return res

# @lc code=end
