#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (28.83%)
# Likes:    7933
# Dislikes: 1234
# Total Accepted:    748.5K
# Total Submissions: 2.5M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# Follow up: The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# 
# 
# Example 4:
# 
# 
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# 
# 
# Example 5:
# 
# 
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if (n + m) % 2 == 1:
            return self.getKth(nums1, nums2, (n + m) // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (n + m) // 2) + self.getKth(nums1, nums2, (n + m) // 2 + 1)) * 0.5

    def getKth(self, listA, listB, k):
        n = len(listA)
        m = len(listB)
        if n > m:
            return self.getKth(listB, listA, k)
        if n == 0:
            return listB[k - 1]
        if k == 1:
            return min(listA[0], listB[0])
        pa = min(k // 2, len(listA))
        pb = k - pa
        if listA[pa - 1] <= listB[pb - 1]:
            return self.getKth(listA[pa:], listB, pb)
        else:
            return self.getKth(listA, listB[pb:], pa)

# @lc code=end
