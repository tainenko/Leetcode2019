#
# @lc app=leetcode id=368 lang=python
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (35.18%)
# Likes:    695
# Dislikes: 36
# Total Accepted:    53.5K
# Total Submissions: 149.9K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j
            if max_dp < dp[i]:
                max_dp = dp[i]
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = index[max_index]
        return res

# @lc code=end
