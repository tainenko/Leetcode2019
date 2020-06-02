#
# @lc app=leetcode id=454 lang=python
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (52.63%)
# Likes:    1069
# Dislikes: 71
# Total Accepted:    103.8K
# Total Submissions: 196.9K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
# 
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is
# guaranteed to be at most 2^31 - 1.
# 
# Example:
# 
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        cnts = defaultdict(int)
        for a in A:
            for b in B:
                cnts[a + b] += 1
        for c in C:
            for d in D:
                res += cnts[-(c + d)]
        return res

# @lc code=end
