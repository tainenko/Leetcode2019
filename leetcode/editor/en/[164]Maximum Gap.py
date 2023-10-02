# Given an integer array nums, return the maximum difference between two 
# successive elements in its sorted form. If the array contains less than two elements, 
# return 0. 
# 
#  You must write an algorithm that runs in linear time and uses linear extra 
# space. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) 
# has the maximum difference 3.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Sorting Bucket Sort Radix Sort 👍 3015 👎 347


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        mi, mx = min(nums), max(nums)
        n = len(nums)
        bucket_size = max(1, (mx - mi) // (n - 1))
        bucket_count = (mx - mi) // bucket_size + 1
        buckets = [[inf, -inf] for _ in range(bucket_count)]
        for num in nums:
            i = (num - mi) // bucket_size
            buckets[i][0] = min(buckets[i][0], num)
            buckets[i][1] = max(buckets[i][1], num)

        prev = inf
        res = 0
        for b_mi, b_mx in buckets:
            if b_mi > b_mx:
                continue
            res = max(res, b_mi - prev)
            prev = b_mx

        return res
# leetcode submit region end(Prohibit modification and deletion)
