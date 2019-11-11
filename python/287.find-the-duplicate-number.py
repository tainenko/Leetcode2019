#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (50.60%)
# Likes:    3087
# Dislikes: 360
# Total Accepted:    234.4K
# Total Submissions: 454.5K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(32):
            bit = 1 << i
            cnt1 = 0
            cnt2 = 0
            for j in range(n):
                if j & bit > 0:
                    cnt1 += 1
                if nums[j] & bit > 0:
                    cnt2 += 1
            if cnt2 > cnt1:
                res += bit
        return res

# @lc code=end
