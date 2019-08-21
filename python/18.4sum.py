#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (31.21%)
# Total Accepted:    254.8K
# Total Submissions: 814.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            arr = self.threeSum(nums[i + 1:], target - nums[i])
            for ele in arr:
                if [nums[i]] + ele not in res:
                    res.append([nums[i]] + ele)
        return res

    def threeSum(self, nums, target):
        N = len(nums)
        res = []
        for i in range(N):
            left = i + 1
            right = N - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    res.append([nums[i], nums[left], nums[right]])
                if total < target:
                    left += 1
                else:
                    right -= 1
        return res
