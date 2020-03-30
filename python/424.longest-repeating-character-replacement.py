#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (44.70%)
# Likes:    983
# Dislikes: 64
# Total Accepted:    54.5K
# Total Submissions: 119.6K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string s that consists of only uppercase English letters, you can
# perform at most k operations on that string.
# 
# In one operation, you can choose any character of the string and change it to
# any other uppercase English character.
# 
# Find the length of the longest sub-string containing all repeating letters
# you can get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 10^4.
# 
# Example 1:
# 
# 
# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        max_cnt = 0
        start = 0
        cnts = {}
        for i in range(len(s)):
            cnts[s[i]] = cnts.get(s[i], 0) + 1
            max_cnt = max(max_cnt, cnts[s[i]])
            while i - start + 1 - max_cnt > k:
                cnts[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res
# @lc code=end
