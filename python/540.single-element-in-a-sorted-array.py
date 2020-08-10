#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.66%)
# Likes:    1746
# Dislikes: 80
# Total Accepted:    154.2K
# Total Submissions: 266.3K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
# 
# Follow up: Your solution should run in O(log n) time and O(1) space.
# 
# 
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) / 2
        while lo < hi:
            m = lo + (hi - lo) / 2
            if nums[2 * m] != nums[2 * m + 1]:
                hi = m
            else:
                lo = m + 1
        return nums[2 * lo]

# @lc code=end
