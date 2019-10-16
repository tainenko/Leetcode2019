#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (32.78%)
# Likes:    1061
# Dislikes: 124
# Total Accepted:    115K
# Total Submissions: 345.1K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        b = 0
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == a:
                cnt1 += 1
            elif num == b:
                cnt2 += 1
            elif cnt1 == 0:
                a = num
                cnt1 = 1
            elif cnt2 == 0:
                b = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == a:
                cnt1 += 1
            elif num == b:
                cnt2 += 1
        res = []
        if cnt1 > len(nums) // 3:
            res.append(a)
        if cnt2 > len(nums) // 3:
            res.append(b)
        return res

    def outerspace_majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # space complexity: O(n)
        # time complexity: O(n)
        res = []
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] > len(nums) // 3 and num not in res:
                res.append(num)
        return res

# @lc code=end
