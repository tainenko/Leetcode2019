#
# @lc app=leetcode id=556 lang=python
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (31.20%)
# Likes:    690
# Dislikes: 195
# Total Accepted:    42.9K
# Total Submissions: 135.3K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1:
# 
# 
# Input: 12
# Output: 21
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 21
# Output: -1
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        size = len(nums)
        for i in range(size - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                break
        if i > 0:
            for j in range(size - 1, -1, -1):
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        for k in range((size - i) / 2):
            nums[i + k], nums[size - k - 1] = nums[size - k - 1], nums[i + k]
        ans = int(''.join(nums))
        if ans > 1 << 31 or ans <= n:
            return -1
        return ans

# @lc code=end
