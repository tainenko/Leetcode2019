#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (31.18%)
# Total Accepted:    217K
# Total Submissions: 693.2K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        pos=-1
        for char1 in num1[::-1]:
            tmp_pos=pos
            for char2 in num2[::-1]:
                res[tmp_pos]+=int(char1)*int(char2)
                tmp_pos-=1
            pos-=1

        carry=0
        for i in range(len(res))[::-1]:
            res[i]+=carry
            carry=res[i]//10
            res[i]%=10
        for idx,num in enumerate(res):
            if num!=0:
                res=res[idx:]
                break
        return ''.join(map(str,res))

