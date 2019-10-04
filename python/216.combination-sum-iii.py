#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (52.53%)
# Likes:    720
# Dislikes: 39
# Total Accepted:    136.3K
# Total Submissions: 256.3K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, res, [], 1)
        return res

    def dfs(self, k, n, res, arr, start):
        if k < 0 or n < 0:
            return
        if 0 == k and n == 0:
            if arr not in res:
                res.append(arr)
            return
        for i in range(start, 10):
            self.dfs(k - 1, n - i, res, arr + [i], i + 1)
# @lc code=end
