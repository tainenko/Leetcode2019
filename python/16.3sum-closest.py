#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.79%)
# Total Accepted:    371.9K
# Total Submissions: 812.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        close = nums[0] + nums[1] + nums[2]
        diff = abs(target - close)
        nums.sort()
        N = len(nums)
        for i in range(N - 2):
            left = i + 1
            right = N - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                newdiff = abs(target - tmp)
                if newdiff < diff:
                    diff = newdiff
                    close = tmp
                if tmp < target:
                    left += 1
                else:
                    right -= 1
        return close
