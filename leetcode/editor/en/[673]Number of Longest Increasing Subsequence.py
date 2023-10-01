# Given an integer array nums, return the number of longest increasing 
# subsequences. 
# 
#  Notice that the sequence has to be strictly increasing. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 
# 3, 5, 7].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there 
# are 5 increasing subsequences of length 1, so output 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  -10⁶ <= nums[i] <= 10⁶ 
#  
# 
#  Related Topics Array Dynamic Programming Binary Indexed Tree Segment Tree 👍 
# 6439 👎 257


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        res = 0
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        longest = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > longest:
                longest = dp[i]
                res = cnt[i]
            elif dp[i] == longest:
                res += cnt[i]

        return res
# leetcode submit region end(Prohibit modification and deletion)
