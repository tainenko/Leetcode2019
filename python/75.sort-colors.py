#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (42.91%)
# Total Accepted:    343.6K
# Total Submissions: 800.5K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def heapify(nums, root, n):
            left = 2 * root + 1
            right = 2 * root + 2

            if left < n and nums[root] < nums[left]:
                largest = left
            else:
                largest = root
            if right < n and nums[largest] < nums[right]:
                largest = right

            if root != largest:
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(nums, largest, n)

        def buildheap(nums, n):
            for i in range(n, -1, -1):
                heapify(nums, i, n)

        n = len(nums)
        buildheap(nums, n)

        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, 0, i)

    def quicksortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def partition(nums, left, right):
            i = left - 1
            pivot = nums[right]
            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            return i + 1

        def quicksort(nums, left, right):
            if left < right:
                i = partition(nums, left, right)
                quicksort(nums, left, i - 1)
                quicksort(nums, i + 1, right)

        quicksort(nums, 0, len(nums) - 1)

    def mergesortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            self.mergesortColors(left)
            self.mergesortColors(right)
            i = j = k = 0
            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            while k < len(right):
                nums[i] = right[k]
                i += 1
                k += 1

    def insertsortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        else:
            for i in range(1, len(nums)):
                key = nums[i]
                j = i - 1
                while nums[j] > key and j >= 0:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = key
        return nums

    def bubblesortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
