# Given an integer array nums, return 0 if the sum of the digits of the minimum 
# integer in nums is odd, or 1 otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: The minimal element is 1, and the sum of those digits is 1 which 
# is odd, so the answer is 0.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [99,77,33,66,55]
# Output: 1
# Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 =
#  6 which is even, so the answer is 1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  1 <= nums[i] <= 100 
#  
#  Related Topics Array Math 👍 73 👎 132


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        num = min(nums)
        return 1 if sum([int(s) for s in str(num)]) % 2 == 0 else 0
# leetcode submit region end(Prohibit modification and deletion)
