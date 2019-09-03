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
        
