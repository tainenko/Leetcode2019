#
# @lc app=leetcode id=395 lang=python
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (39.21%)
# Likes:    1125
# Dislikes: 98
# Total Accepted:    66.3K
# Total Submissions: 164.6K
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#

# @lc code=start
import collections


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

# @lc code=end
