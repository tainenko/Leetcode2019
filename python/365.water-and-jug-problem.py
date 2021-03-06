#
# @lc app=leetcode id=365 lang=python
#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (29.26%)
# Likes:    210
# Dislikes: 599
# Total Accepted:    33K
# Total Submissions: 110.9K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities x and y litres. There is an infinite
# amount of water supply available. You need to determine whether it is
# possible to measure exactly z litres using these two jugs.
# 
# If z liters of water is measurable, you must have z liters of water contained
# within one or both buckets by the end.
# 
# Operations allowed:
# 
# 
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or
# the first jug itself is empty.
# 
# 
# Example 1: (From the famous "Die Hard" example)
# 
# 
# Input: x = 3, y = 5, z = 4
# Output: True
# 
# 
# Example 2:
# 
# 
# Input: x = 2, y = 6, z = 5
# Output: False
# 
#

# @lc code=start
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0 or (z <= x + y and z % self.__gcd(x, y) == 0):
            return True
        return False

    def __gcd(self, x, y):
        if y == 0:
            return x
        return self.__gcd(y, x % y)
# @lc code=end
