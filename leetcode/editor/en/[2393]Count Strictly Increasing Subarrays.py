# You are given an array nums consisting of positive integers. 
# 
#  Return the number of subarrays of nums that are in strictly increasing order.
#  
# 
#  A subarray is a contiguous part of an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,4,4,6]
# Output: 10
# Explanation: The strictly increasing subarrays are the following:
# - Subarrays of length 1: [1], [3], [5], [4], [4], [6].
# - Subarrays of length 2: [1,3], [3,5], [4,6].
# - Subarrays of length 3: [1,3,5].
# The total number of subarrays is 6 + 3 + 1 = 10.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: Every subarray is strictly increasing. There are 15 possible 
# subarrays that we can take.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁶ 
#  
# 
#  Related Topics Array Math Dynamic Programming 👍 76 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] > nums[j - 1]:
                j += 1
            cnt = j - i
            res += (1 + cnt) * cnt // 2
            i = j
        return res
# leetcode submit region end(Prohibit modification and deletion)
