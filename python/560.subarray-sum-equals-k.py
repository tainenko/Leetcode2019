#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.76%)
# Likes:    5093
# Dislikes: 168
# Total Accepted:    343.3K
# Total Submissions: 782.8K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        d[0] = 1
        total = 0
        res = 0
        for num in nums:
            total += num
            if total - k in d:
                res += d[total - k]
            d[total] += 1
        return res

# @lc code=end
