#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.83%)
# Likes:    167
# Dislikes: 641
# Total Accepted:    31.4K
# Total Submissions: 86.8K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
# 
# Example 1:
# 
# 
# 
# Input: a = 2, b = [3]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a = a % 1337
        res = pow(a, b[0]) % 1337
        for x in b[1:]:
            res = (pow(res, 10) * pow(a, x)) % 1337
        return res

# @lc code=end
