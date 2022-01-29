# Given an integer array nums, return the largest integer that only occurs once.
#  If no integer occurs once, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The 
# number 8 occurs only once, so it is the answer. 
# 
#  Example 2: 
# 
#  
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics Array Hash Table Sorting 👍 221 👎 16


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max([num for num, val in cnt.items() if val == 1], default=-1)
# leetcode submit region end(Prohibit modification and deletion)
