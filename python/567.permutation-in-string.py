#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.62%)
# Likes:    1723
# Dislikes: 66
# Total Accepted:    144.8K
# Total Submissions: 325.9K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# Constraints:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        right = len(s1)
        left = 0
        while right < len(s2):
            if count1 == count2:
                return True
            count2[s2[right]] += 1
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            right += 1
            left += 1
        if count1 == count2:
            return True
        return False

# @lc code=end
