'''
[300] Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/description/

* algorithms
* Medium (40.43%)
* Source Code:       300.longest-increasing-subsequence.py
* Total Accepted:    215.3K
* Total Submissions: 529.8K
* Testcase Example:  '[10,9,2,5,3,7,101,18]'

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:


Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:


        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n^2) complexity.


Follow up: Could you improve it to O(n log n) time complexity?

'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
