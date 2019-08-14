#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.05%)
# Total Accepted:    374K
# Total Submissions: 663.6K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.DFS(n, n, "", res)
        return res

    def DFS(self, left, right, str, res):
        if left > right:
            return
        elif 0 == left == right:
            res.append(str)
        else:
            if left > 0:
                self.DFS(left - 1, right, str + '(', res)
            if right > 0:
                self.DFS(left, right - 1, str + ')', res)
