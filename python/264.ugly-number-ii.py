#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (37.08%)
# Likes:    1182
# Dislikes: 74
# Total Accepted:    120.6K
# Total Submissions: 318.4K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        t2 = 0
        t3 = 0
        t5 = 0
        res = [1]
        for i in range(n - 1):
            tmp = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(tmp)
            if res[-1] == res[t2] * 2:
                t2 += 1
            if res[-1] == res[t3] * 3:
                t3 += 1
            if res[-1] == res[t5] * 5:
                t5 += 1
        return res[-1]

# @lc code=end
