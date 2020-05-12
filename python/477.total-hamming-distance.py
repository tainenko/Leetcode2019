#
# @lc app=leetcode id=477 lang=python
#
# [477] Total Hamming Distance
#
# https://leetcode.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (50.22%)
# Likes:    750
# Dislikes: 51
# Total Accepted:    59.9K
# Total Submissions: 119.2K
# Testcase Example:  '[4,14,2]'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Now your job is to find the total Hamming distance between all pairs of the
# given numbers.
# 
# 
# Example:
# 
# Input: 4, 14, 2
# 
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
# 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
# 
# 
# 
# Note:
# 
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4. 
# 
# 
#

# @lc code=start
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        n = len(nums)
        for i in range(32):
            cnt = 0
            for num in nums:
                if num & (1 << i):
                    cnt += 1
            total += cnt * (n - cnt)
        return total

# @lc code=end
