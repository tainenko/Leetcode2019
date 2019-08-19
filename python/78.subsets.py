#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.35%)
# Total Accepted:    400.5K
# Total Submissions: 735.7K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def getconbination(nums, arr, k):
            if k == 0:
                res.append(arr)
            for i in range(len(nums)):
                getconbination(nums[i + 1:], arr + [nums[i]], k - 1)

        for i in range(len(nums) + 1):
            getconbination(nums, [], i)
        return res
