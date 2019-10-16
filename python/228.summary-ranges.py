#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (36.57%)
# Likes:    438
# Dislikes: 428
# Total Accepted:    142.9K
# Total Submissions: 385.3K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = 0
        end = 0
        while start < len(nums):
            while end < len(nums) - 1 and (nums[end] + 1 == nums[end + 1]):
                end += 1
            if end == start:
                res.append(str(nums[end]))
            else:
                res.append("{start}->{end}".format(start=nums[start], end=nums[end]))
            end += 1
            start = end
        return res
# @lc code=end
