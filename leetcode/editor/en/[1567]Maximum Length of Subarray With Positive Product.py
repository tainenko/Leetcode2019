# Given an array of integers nums, find the maximum length of a subarray where 
# the product of all its elements is positive. 
# 
#  A subarray of an array is a consecutive sequence of zero or more values 
# taken out of that array. 
# 
#  Return the maximum length of a subarray with positive product. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which 
# has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the 
# product 0 which is not positive. 
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Dynamic Programming Greedy 👍 2296 👎 61


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
        for num in nums:
            if num > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif num < 0:
                ppos, pneg = pos, neg
                neg = ppos + 1
                if pneg > 0:
                    pos = pneg + 1
                else:
                    pos = 0
            else:
                pos = neg = 0
            res = max(res, pos)
        return res
# leetcode submit region end(Prohibit modification and deletion)
