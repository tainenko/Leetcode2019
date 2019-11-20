#
# @lc app=leetcode id=324 lang=python
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (28.31%)
# Likes:    769
# Dislikes: 431
# Total Accepted:    70K
# Total Submissions: 242.9K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
# 
# Example 1:
# 
# 
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Example 2:
# 
# 
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
# @lc code=end
