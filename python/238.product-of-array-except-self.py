#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (56.04%)
# Likes:    2995
# Dislikes: 259
# Total Accepted:    331.5K
# Total Submissions: 578.7K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        res = [None] * len(nums)
        res[0] = 1
        right = 1
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right = nums[i + 1] * right
            res[i] *= right

        return res

# @lc code=end
