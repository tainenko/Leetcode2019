#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (47.06%)
# Likes:    615
# Dislikes: 29
# Total Accepted:    47.4K
# Total Submissions: 99.6K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are a number of spherical balloons spread in two-dimensional space. For
# each balloon, provided input is the start and end coordinates of the
# horizontal diameter. Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice. Start is
# always smaller than end. There will be at most 10^4 balloons.
# 
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps travelling up infinitely. The problem is to find the
# minimum number of arrows that must be shot to burst all balloons.
# 
# Example:
# 
# 
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# 
# Output:
# 2
# 
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points = sorted(points, key=lambda x: (x[0], x[1]))
        res = 0
        start = points[0][0]
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                res += 1
                start = points[i][0]
                end = points[i][1]
            else:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
        return res + 1

# @lc code=end
