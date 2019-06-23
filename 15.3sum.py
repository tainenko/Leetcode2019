'''
[15] 3Sum

https://leetcode.com/problems/3sum/description/

* algorithms
* Medium (24.13%)
* Source Code:       15.3sum.py
* Total Accepted:    569.5K
* Total Submissions: 2.4M
* Testcase Example:  '[-1,0,1,2,-1,-4]'

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:


Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
