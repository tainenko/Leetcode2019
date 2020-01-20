#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (26.97%)
# Likes:    1301
# Dislikes: 76
# Total Accepted:    81.7K
# Total Submissions: 298.4K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
# 
# 
# Note:
# 
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# 
# 
# 
# 
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
#

# @lc code=start
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return "0"
        nums = list(num)
        res = []
        keep = len(num) - k
        for num in nums:
            while k and res and res[-1] > num:
                res.pop()
                k -= 1
            res.append(num)
        res = res[:keep]
        zero = 0
        while res[zero] == '0' and zero < len(res) - 1:
            zero += 1
        return ''.join(res[zero:])

# @lc code=end
