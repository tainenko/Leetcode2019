# You are given a 0-indexed array nums comprising of n non-negative integers. 
# 
#  In one operation, you must: 
# 
#  
#  Choose an integer i such that 1 <= i < n and nums[i] > 0. 
#  Decrease nums[i] by 1. 
#  Increase nums[i - 1] by 1. 
#  
# 
#  Return the minimum possible value of the maximum integer of nums after 
# performing any number of operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,7,1,6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number 
# cannot be less than 5.
# Therefore, we return 5.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10,1]
# Output: 10
# Explanation:
# It is optimal to leave nums as is, and since 10 is the maximum value, we 
# return 10.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  2 <= n <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Binary Search Dynamic Programming Greedy Prefix Sum 👍 1
# 966 👎 504


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit):
            remain = 0
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > limit:
                    remain += nums[i] - limit
                else:
                    remain = max(0, remain - (limit - nums[i]))
            return nums[0] + remain <= limit

        l, r = 0, max(nums)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

# leetcode submit region end(Prohibit modification and deletion)
