# You are given three positive integers: n, index, and maxSum. You want to 
# construct an array nums (0-indexed) that satisfies the following conditions: 
# 
#  
#  nums.length == n 
#  nums[i] is a positive integer where 0 <= i < n. 
#  abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1. 
#  The sum of all the elements of nums does not exceed maxSum. 
#  nums[index] is maximized. 
#  
# 
#  Return nums[index] of the constructed array. 
# 
#  Note that abs(x) equals x if x >= 0, and -x otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 
# 2 is the maximum nums[2].
#  
# 
#  Example 2: 
# 
#  
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= maxSum <= 10⁹ 
#  0 <= index < n 
#  
# 
#  Related Topics Binary Search Greedy 👍 2429 👎 394


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def total(x, cnt):
            return (
                (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1) * x // 2 + cnt - x
            )

        def fn(x):
            return total(x - 1, index) + total(x, n - index)

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if fn(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

# leetcode submit region end(Prohibit modification and deletion)
