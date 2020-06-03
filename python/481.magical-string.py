#
# @lc app=leetcode id=481 lang=python
#
# [481] Magical String
#
# https://leetcode.com/problems/magical-string/description/
#
# algorithms
# Medium (47.20%)
# Likes:    107
# Dislikes: 661
# Total Accepted:    21.8K
# Total Submissions: 46.1K
# Testcase Example:  '1'
#
# 
# A magical string S consists of only '1' and '2' and obeys the following
# rules:
# 
# 
# The string S is magical because concatenating the number of contiguous
# occurrences of characters '1' and '2' generates the string S itself.
# 
# 
# 
# The first few elements of string S is the following:
# S = "1221121221221121122……"
# 
# 
# 
# If we group the consecutive '1's and '2's in S, it will be:
# 
# 
# 1   22  11  2  1  22  1  22  11  2  11  22 ......
# 
# 
# and the occurrences of '1's or '2's in each group are:
# 
# 
# 1   2       2    1   1    2     1    2     2    1    2    2 ......
# 
# 
# 
# You can see that the occurrence sequence above is the S itself. 
# 
# 
# 
# Given an integer N as input, return the number of '1's in the first N number
# in the magical string S.
# 
# 
# Note:
# N will not exceed 100,000.
# 
# 
# 
# Example 1:
# 
# Input: 6
# Output: 3
# Explanation: The first 6 elements of magical string S is "12211" and it
# contains three 1's, so return 3.
# 
# 
#

# @lc code=start
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        ms = [1, 2, 2]
        pos = 2
        while len(ms) < n:
            ms += [3 ^ ms[-1]] * ms[pos]
            pos += 1
        return ms[:n].count(1)

# @lc code=end
