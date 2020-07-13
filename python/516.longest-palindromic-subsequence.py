#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (51.49%)
# Likes:    1948
# Dislikes: 178
# Total Accepted:    117.5K
# Total Submissions: 222.9K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# 
# 
# "bbbab"
# 
# Output:
# 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# 
# Example 2:
# Input:
# 
# 
# "cbbd"
# 
# Output:
# 
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        L = [[0 for x in range(n)] for x in range(n)]
        for i in range(n):
            L[i][i] = 1
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    L[i][j] = 2
                elif s[i] == s[j]:
                    L[i][j] = L[i + 1][j - 1] + 2
                else:
                    L[i][j] = max(L[i + 1][j], L[i][j - 1])
        return L[0][n - 1]
# @lc code=end
