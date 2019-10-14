#
# @lc app=leetcode id=227 lang=python
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (34.16%)
# Likes:    889
# Dislikes: 160
# Total Accepted:    132.4K
# Total Submissions: 381.2K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        prev_op = '+'
        num = 0
        for idx, each in enumerate(s):
            if each.isdigit():
                num = num * 10 + int(each)
            if idx == len(s) - 1 or each in '+-*/':
                if prev_op == '+':
                    stack.append(int(num))
                elif prev_op == '-':
                    stack.append(int(-num))
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // num))
                    else:
                        stack.append(top // num)
                prev_op = each
                num = 0
        return sum(stack)

# @lc code=end
