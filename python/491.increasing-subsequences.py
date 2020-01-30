#
# @lc app=leetcode id=491 lang=python
#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (42.62%)
# Likes:    546
# Dislikes: 95
# Total Accepted:    39.3K
# Total Submissions: 90K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2.
# 
# 
# 
# Example:
# 
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
# 
# 
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = set()
        for num in nums:
            for ele in list(dp):
                if num >= ele[-1]:
                    dp.add(ele + (num,))
            dp.add((num,))
        return [ele for ele in dp if len(ele) > 1]

# @lc code=end
