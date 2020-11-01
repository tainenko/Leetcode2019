#
# @lc app=leetcode id=44 lang=python
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (24.28%)
# Likes:    2425
# Dislikes: 117
# Total Accepted:    268.2K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input: s = "acdcb", p = "a*c?b"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
# 
# 
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]

# @lc code=end
