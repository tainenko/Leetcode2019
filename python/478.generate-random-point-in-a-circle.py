#
# @lc app=leetcode id=478 lang=python
#
# [478] Generate Random Point in a Circle
#
# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Medium (38.32%)
# Likes:    154
# Dislikes: 243
# Total Accepted:    10.3K
# Total Submissions: 26.9K
# Testcase Example:  '["Solution", "randPoint", "randPoint", "randPoint"]\n' +
'[[1.0, 0.0, 0.0], [], [], []]'
#
# Given the radius and x-y positions of the center of a circle, write a
# function randPoint which generates a uniform random point in the circle.
# 
# Note:
# 
# 
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class
# constructor.
# a point on the circumference of the circle is considered to be in the
# circle.
# randPoint returns a size 2 array containing x-position and y-position of the
# random point, in that order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has three arguments, the radius, x-position of the
# center, and y-position of the center of the circle. randPoint has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
# 
#

# @lc code=start
import math
import random


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.raidus = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = self.raidus * math.sqrt(random.random())
        theta = 2 * math.pi * random.random()
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end
