# You are given an array nums consisting of positive integers. 
# 
#  You have to take each integer in the array, reverse its digits, and add it 
# to the end of the array. You should apply this operation to the original integers 
# in nums. 
# 
#  Return the number of distinct integers in the final array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,13,10,12,31]
# Output: 6
# Explanation: After including the reverse of each number, the resulting array 
# is [1,13,10,12,31,1,31,1,21,13].
# The reversed integers that were added to the end of the array are underlined. 
# Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
# 
# The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13,
#  21, and 31). 
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2]
# Output: 1
# Explanation: After including the reverse of each number, the resulting array 
# is [2,2,2,2,2,2].
# The number of distinct integers in this array is 1 (The number 2).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁶ 
#  
# 
#  Related Topics Array Hash Table Math 👍 478 👎 43


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums += [int(str(num)[::-1]) for num in nums]
        return len(set(nums))
# leetcode submit region end(Prohibit modification and deletion)
