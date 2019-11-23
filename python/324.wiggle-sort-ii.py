#
# @lc app=leetcode id=324 lang=python
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (28.31%)
# Likes:    769
# Dislikes: 431
# Total Accepted:    70K
# Total Submissions: 242.9K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
#
# Example 1:
#
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
#
# Example 2:
#
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = self.find_nth_element((n + 1) // 2, 0, n - 1, nums)

        left = 0
        right = n - 1
        i = 0
        while i <= right:
            if nums[self.new_index(i, n)] > median:
                nums[self.new_index(left, n)], nums[self.new_index(i, n)] = nums[self.new_index(i, n)], nums[
                    self.new_index(left, n)]
                left += 1
                i += 1
            elif nums[self.new_index(i, n)] < median:
                nums[self.new_index(right, n)], nums[self.new_index(i, n)] = nums[self.new_index(i, n)], nums[
                    self.new_index(right, n)]
                right -= 1
            else:
                i += 1

    def new_index(self, index, n):
        return (1 + 2 * index) % (n | 1)

    def partition(self, l, r, nums):
        pivot = nums[r]
        i = l
        while l < r:
            if nums[l] < pivot:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
            l += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def find_nth_element(self, n, l, r, nums):
        pos = self.partition(l, r, nums)
        if pos == n - 1:
            return nums[pos]
        elif pos > n - 1:
            return self.find_nth_element(n, l, pos - 1, nums)
        else:
            return self.find_nth_element(n, pos + 1, r, nums)

# @lc code=end
