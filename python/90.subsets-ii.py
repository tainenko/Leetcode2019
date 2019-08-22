#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (43.27%)
# Total Accepted:    217.8K
# Total Submissions: 502.5K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if not nums:
            return []
        res = [[]]
        size = 1
        last = nums[0]
        for num in nums:
            if last != num:
                last = num
                size = len(res)
            newsize = len(res)
            curr = []
            for i in range(newsize - size, len(res)):
                curr.append(res[i] + [num])
            res += curr
        return res
