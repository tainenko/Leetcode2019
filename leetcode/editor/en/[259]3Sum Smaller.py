# Given an array of n integers nums and an integer target, find the number of 
# index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] 
# + nums[j] + nums[k] < target. 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [], target = 0
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [0], target = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  0 <= n <= 3500 
#  -100 <= nums[i] <= 100 
#  -100 <= target <= 100 
#  
#  Related Topics Array Two Pointers Binary Search Sorting 👍 1166 👎 120


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        total = 0
        for i in range(len(nums) - 2):
            total += self.twoSumSmaller(nums[i + 1:], target - nums[i])
        return total

    def twoSumSmaller(self, nums, target):
        left = 0
        right = len(nums) - 1
        total = 0
        while left < right:
            if nums[left] + nums[right] < target:
                total += right - left
                left += 1
            else:
                right -= 1
        return total

# leetcode submit region end(Prohibit modification and deletion)
