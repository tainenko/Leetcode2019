#
# @lc app=leetcode id=473 lang=python
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (37.08%)
# Likes:    524
# Dislikes: 54
# Total Accepted:    34.1K
# Total Submissions: 91.5K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#

# @lc code=start
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
# @lc code=end
