# Given a binary array nums and an integer goal, return the number of non-empty 
# subarrays with a sum goal. 
# 
#  A subarray is a contiguous part of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  nums[i] is either 0 or 1. 
#  0 <= goal <= nums.length 
#  
# 
#  Related Topics Array Hash Table Sliding Window Prefix Sum 👍 4453 👎 151


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum1, sum2 = 0, 0
        head, tail = 0, 0
        ans = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            sum2 += nums[i]
            while sum1 > goal:
                sum1 -= nums[head]
                head += 1
            while sum2 >= goal and tail <= i:
                sum2 -= nums[tail]
                tail += 1
            ans += tail - head
        return ans
# leetcode submit region end(Prohibit modification and deletion)
