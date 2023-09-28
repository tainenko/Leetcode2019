# Given an array of integers nums and an integer k, return the number of 
# contiguous subarrays where the product of all the elements in the subarray is strictly 
# less than k. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly 
# less than k.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3], k = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 10⁶ 
#  
# 
#  Related Topics Array Sliding Window 👍 5783 👎 177


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        total = 1
        j = 0
        for i, v in enumerate(nums):
            total *= v
            while total >= k and j <= i:
                total //= nums[j]
                j += 1
            res += i - j + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
