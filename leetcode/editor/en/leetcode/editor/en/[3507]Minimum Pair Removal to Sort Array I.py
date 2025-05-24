# Given an array nums, you can perform the following operation any number of 
# times: 
# 
#  
#  Select the adjacent pair with the minimum sum in nums. If multiple such 
# pairs exist, choose the leftmost one. 
#  Replace the pair with their sum. 
#  
# 
#  Return the minimum number of operations needed to make the array non-
# decreasing. 
# 
#  An array is said to be non-decreasing if each element is greater than or 
# equal to its previous element (if it exists). 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [5,2,3,1] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  
#  The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4]. 
#  The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6]. 
#  
# 
#  The array nums became non-decreasing in two operations. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,2] 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  The array nums is already sorted. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 50 
#  -1000 <= nums[i] <= 1000 
#  
# 
#  Related Topics Array Hash Table Linked List Heap (Priority Queue) Simulation 
# Doubly-Linked List Ordered Set 👍 56 👎 14


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while not self.is_decreasing(nums):
            idx, total = self.find_min_sum(nums)
            nums = nums[:idx] + [total] + nums[idx + 2:]
            res += 1
        return res

    def is_decreasing(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    def find_min_sum(self, nums: List[int]) -> (int, int):
        res = float('inf')
        idx = len(nums) - 1
        for i in range(len(nums) - 1):
            total = nums[i] + nums[i + 1]
            if total < res:
                res = total
                idx = i
        return idx, res
# leetcode submit region end(Prohibit modification and deletion)
