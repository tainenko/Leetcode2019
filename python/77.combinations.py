#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (49.10%)
# Total Accepted:    219.8K
# Total Submissions: 447K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1, n + 1)]
        res = []

        def addpossible(nums, arr, k):
            if k == 0:
                res.append(arr)
                return
            for i in range(len(nums)):
                addpossible(nums[i + 1:], arr + [nums[i]], k - 1)

        addpossible(nums, [], k)
        return res
