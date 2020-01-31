#
# @lc app=leetcode id=421 lang=python
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (51.55%)
# Likes:    899
# Dislikes: 164
# Total Accepted:    44.8K
# Total Submissions: 85.3K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 2^31.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
# @lc code=end
