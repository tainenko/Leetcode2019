#
# @lc app=leetcode id=166 lang=python
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (19.77%)
# Total Accepted:    94.7K
# Total Submissions: 475.9K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# Example 1:
# 
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# 
# Example 2:
# 
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# 
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# 
#
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        sign = '-' if ((numerator > 0) ^ (denominator > 0)) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        div, mod = divmod(numerator, denominator)
        if not mod:
            return sign + str(div)
        res = sign + str(div) + '.'
        pos = dict()
        pos[mod] = len(res)
        while mod:
            mod *= 10
            div, mod = divmod(mod, denominator)
            res += str(div)
            if mod in pos:
                idx = pos[mod]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            else:
                pos[mod] = len(res)

        return res
