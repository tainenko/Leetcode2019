# Given an array consists of non-negative integers, your task is to count the nu
# mber of triplets chosen from the array that can make triangles if we take them a
# s side lengths of a triangle.
# 
#  Example 1: 
#  
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#  
#  
# 
#  Note: 
#  
#  The length of the given array won't exceed 1000. 
#  The integers in the given array are in the range of [0, 1000]. 
#  
#  
#  Related Topics Array 
#  👍 1385 👎 106


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
