# You are given an array nums, where each number in the array appears either 
# once or twice. 
# 
#  Return the bitwise XOR of all the numbers that appear twice in the array, or 
# 0 if no number appears twice. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,2,1,3] 
#  
# 
#  Output: 1 
# 
#  Explanation: 
# 
#  The only number that appears twice in nums is 1. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,3] 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  No number appears twice in nums. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [1,2,2,1] 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  Numbers 1 and 2 appeared twice. 1 XOR 2 == 3. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 50 
#  1 <= nums[i] <= 50 
#  Each number in nums appears either once or twice. 
#  
# 
#  Related Topics Array Hash Table Bit Manipulation 👍 71 👎 5
import collections

from functools import reduce


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        nums = [k for k, v in cnt.items() if v == 2]
        if not nums:
            return 0
        return reduce(lambda a, b: a ^ b, nums)
# leetcode submit region end(Prohibit modification and deletion)
