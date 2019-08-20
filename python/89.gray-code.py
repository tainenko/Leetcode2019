#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (46.44%)
# Total Accepted:    140.6K
# Total Submissions: 302.5K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
# 
# 
#
class Solution(object):
    def grayCode(self, n):
        def getgrays(n):
            if n == 0:
                res = ['0']
            elif n == 1:
                res = ['0', '1']
            else:
                res = ['0' + x for x in getgrays(n - 1)] + ['1' + x for x in getgrays(n - 1)[::-1]]
            return res

        return map(lambda x: int(x, 2), getgrays(n))

    def grayCode_iter(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        grays = ['0', '1']
        for n in range(n - 1):
            curr = []
            for code in grays:
                curr.append('0' + code)
            for code in grays[::-1]:
                curr.append('1' + code)
            grays = curr

        return map(lambda x: int(x, 2), grays)
