#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (56.06%)
# Likes:    2089
# Dislikes: 139
# Total Accepted:    278.5K
# Total Submissions: 482.2K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnts = {}
        for num in nums:
            cnts[num] = cnts.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in cnts.items():
            buckets[val].append(key)
        res = []
        for ele in buckets[::-1]:
            if len(res) >= k:
                break
            res += ele
        return res

# @lc code=end
