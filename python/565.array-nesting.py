#
# @lc app=leetcode id=565 lang=python
#
# [565] Array Nesting
#
# https://leetcode.com/problems/array-nesting/description/
#
# algorithms
# Medium (54.85%)
# Likes:    853
# Dislikes: 94
# Total Accepted:    54.1K
# Total Submissions: 97.5K
# Testcase Example:  '[5,4,0,3,1,6,2]'
#
# A zero-indexed array A of length N contains all integers from 0 to N-1. Find
# and return the longest length of set S, where S[i] = {A[i], A[A[i]],
# A[A[A[i]]], ... } subjected to the rule below.
# 
# Suppose the first element in S starts with0  the selection of element A[i] of
# index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By
# that analogy, we stop adding right before a duplicate element occurs in
# S.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [5,4,0,3,1,6,2]
# Output: 4
# Explanation: 
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
# 
# One of the longest S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# 
# 
# 
# 
# Note:
# 
# 
# N is an integer within the range [1, 20,000].
# The elements of A are all distinct.
# Each element of A is an integer within the range [0, N-1].
# 
# 
#

# @lc code=start
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        visited = [False] * len(nums)
        res = 0
        for i in range(len(nums)):
            if visited[i]:
                continue
            cnt = self.helper(nums, visited, i, 0)
            res = max(cnt, res)
        return res

    def helper(self, nums, visited, i, cnt):
        if visited[i]:
            return cnt
        visited[i] = True
        return self.helper(nums, visited, nums[i], cnt + 1)

# @lc code=end
