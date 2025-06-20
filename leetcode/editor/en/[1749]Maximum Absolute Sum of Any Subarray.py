# You are given an integer array nums. The absolute sum of a subarray [numsl, 
# numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr). 
# 
#  Return the maximum absolute sum of any (possibly empty) subarray of nums. 
# 
#  Note that abs(x) is defined as follows: 
# 
#  
#  If x is a negative integer, then abs(x) = -x. 
#  If x is a non-negative integer, then abs(x) = x. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) =
#  8.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming 👍 1914 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        f = g = 0
        ans = 0
        for i in range(len(nums)):
            f = max(f, 0) + nums[i]
            g = min(g, 0) + nums[i]
            ans = max(ans, f, abs(g))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
