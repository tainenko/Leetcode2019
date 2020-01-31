#
# @lc app=leetcode id=1154 lang=python
#
# [1154] Day of the Year
#
# https://leetcode.com/problems/day-of-the-year/description/
#
# algorithms
# Easy (51.48%)
# Likes:    56
# Dislikes: 107
# Total Accepted:    12.5K
# Total Submissions: 25.5K
# Testcase Example:  '"2019-01-09"\r'
#
# Given a string date representing a Gregorian calendar date formatted as
# YYYY-MM-DD, return the day number of the year.
# 
# 
# Example 1:
# 
# 
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# 
# 
# Example 2:
# 
# 
# Input: date = "2019-02-10"
# Output: 41
# 
# 
# Example 3:
# 
# 
# Input: date = "2003-03-01"
# Output: 60
# 
# 
# Example 4:
# 
# 
# Input: date = "2004-03-01"
# Output: 61
# 
# 
# 
# Constraints:
# 
# 
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
# 
#

# @lc code=start
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
# @lc code=end
