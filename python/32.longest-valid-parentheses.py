#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.70%)
# Likes:    3956
# Dislikes: 148
# Total Accepted:    309.8K
# Total Submissions: 1.1M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# 
# 
# Example 2:
# 
# 
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# 
# 
# Example 3:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
# 
# 
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        start, res = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            if not stack:
                start = i + 1
            else:
                stack.pop()
                res = max(res, i - stack[-1] if stack else i - start + 1)
        return res
# @lc code=end
