# The product difference between two pairs (a, b) and (c, d) is defined as (a * 
# b) - (c * d). 
# 
#  
#  For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2
#  * 7) = 16. 
#  
# 
#  Given an integer array nums, choose four distinct indices w, x, y, and z 
# such that the product difference between pairs (nums[w], nums[x]) and (nums[y], 
# nums[z]) is maximized. 
# 
#  Return the maximum such product difference. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and 
# indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,2,5,9,7,4,8]
# Output: 64
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and 
# indices 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.
#  
# 
#  
#  Constraints: 
# 
#  
#  4 <= nums.length <= 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Sorting 👍 538 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxs = [0, 0]
        mins = [float("inf"), float("inf")]
        for num in nums:
            if num >= maxs[0]:
                maxs[1] = maxs[0]
                maxs[0] = num

            elif num > maxs[1]:
                maxs[1] = num

            if num <= mins[0]:
                mins[1] = mins[0]
                mins[0] = num

            elif num < mins[1]:
                mins[1] = num

        return maxs[0] * maxs[1] - mins[0] * mins[1]
# leetcode submit region end(Prohibit modification and deletion)
