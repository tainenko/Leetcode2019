#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (42.11%)
# Total Accepted:    178.6K
# Total Submissions: 420.8K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        out = []
        self.helper(s, out, res)
        return res

    def helper(self, s, out, res):
        if not s:
            res.append(out)
        for i in range(1, len(s) + 1):
            sub = s[:i]
            if self.is_palindrome(sub):
                self.helper(s[i:], out + [sub], res)

    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
