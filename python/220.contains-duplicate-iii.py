#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (19.99%)
# Likes:    770
# Dislikes: 773
# Total Accepted:    102.1K
# Total Submissions: 506.5K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dct = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dct.get(key - 1), dct.get(key), dct.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dct) == k:
                dct.popitem(False)
            dct[key] = n
        return False

# @lc code=end
