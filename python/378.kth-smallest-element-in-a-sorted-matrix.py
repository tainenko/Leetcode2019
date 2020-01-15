#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (50.33%)
# Likes:    1704
# Dislikes: 101
# Total Accepted:    147K
# Total Submissions: 283.6K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            mid = left + (right - left) // 2
            cnt = self.count_lower(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def count_lower(self, matrix, mid):
        i = len(matrix) - 1
        j = 0
        cnt = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] <= mid:
                cnt += i + 1
                j += 1

            else:
                i -= 1
        return cnt

# @lc code=end
