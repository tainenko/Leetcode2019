# Given an integer array nums and an integer k, return true if it is possible 
# to divide this array into k non-empty subsets whose sums are all equal. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2
# ,3) with equal sums.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,4], k = 3
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 16 
#  1 <= nums[i] <= 10⁴ 
#  The frequency of each element is in the range [1, 4]. 
#  
# 
#  Related Topics Array Dynamic Programming Backtracking Bit Manipulation 
# Memoization Bitmask 👍 7344 👎 531


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if not nums or len(nums) < k:
            return False

        total = sum(nums)
        div, mod = divmod(total, k)
        if mod != 0 or max(nums) > div:
            return False

        nums.sort(reverse=True)
        target = [div] * k
        return self.dfs(nums, k, 0, target)

    def dfs(self, nums, k, index, target):

        if index == len(nums):
            return True

        num = nums[index]
        seen = set()
        for i in range(k):
            if target[i] < num or target[i] in seen:
                continue
            target[i] -= num
            if self.dfs(nums, k, index + 1, target):
                return True
            target[i] += num
            seen.add(target[i])
        return False

# leetcode submit region end(Prohibit modification and deletion)
