# Given an integer array nums and an integer k, return the maximum length of a 
# subarray that sums to k. If there is not one, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#  
# 
#  Example 2: 
#
#  
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  -10⁹ <= k <= 10⁹ 
#  
# 
#  Related Topics Array Hash Table Prefix Sum 👍 1898 👎 57


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import accumulate


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res, mapping = 0, dict()
        for idx, val in enumerate(accumulate(nums)):
            if val == k:
                res = idx + 1
            elif val - k in mapping:
                res = max(res, idx - mapping[val - k])
            if val not in mapping:
                mapping[val] = idx
        return res

# leetcode submit region end(Prohibit modification and deletion)
