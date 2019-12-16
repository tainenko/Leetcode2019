#
# @lc app=leetcode id=368 lang=python
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (35.18%)
# Likes:    695
# Dislikes: 36
# Total Accepted:    53.5K
# Total Submissions: 149.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
# @lc code=end
