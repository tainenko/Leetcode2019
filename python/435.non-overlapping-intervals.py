#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.83%)
# Likes:    640
# Dislikes: 26
# Total Accepted:    50.5K
# Total Submissions: 120.5K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
# 
# 
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        end = float('-inf')
        res = 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                res += 1
        return res

# @lc code=end
