#
# @lc app=leetcode id=539 lang=python
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (50.95%)
# Likes:    494
# Dislikes: 152
# Total Accepted:    51.3K
# Total Submissions: 99.6K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1
# 
# 
# 
# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# 
#

# @lc code=start
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) >= 1440:
            return 0
        time_points = sorted([self.get_minutes(x) for x in timePoints])
        return min([time_points[i] - time_points[i - 1] for i in range(1, len(time_points))] + [
            time_points[0] + 1440 - time_points[-1]])

    def get_minutes(self, str):
        min_, sec = str.split(":")
        return int(min_) * 60 + int(sec)

# @lc code=end
