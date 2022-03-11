# Given an array of integers nums, return the number of good pairs. 
# 
#  A pair (i, j) is called good if nums[i] == nums[j] and i < j. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,2,3]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  1 <= nums[i] <= 100 
#  
#  Related Topics Array Hash Table Math Counting 👍 2257 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for val in cnt.values():
            res += (val - 1) * (val) // 2
        return res

# leetcode submit region end(Prohibit modification and deletion)
