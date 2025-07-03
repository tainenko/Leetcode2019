# You are given an integer array nums. 
# 
#  Return true if the frequency of any element of the array is prime, otherwise,
#  return false. 
# 
#  The frequency of an element x is the number of times it occurs in the array. 
# 
# 
#  A prime number is a natural number greater than 1 with only two factors, 1 
# and itself. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,2,3,4,5,4] 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  4 has a frequency of two, which is a prime number. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,3,4,5] 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  All elements have a frequency of one. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [2,2,2,4,4] 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  Both 2 and 4 have a prime frequency. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
# 
#  Related Topics Array Hash Table Math Counting Number Theory 👍 32 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        cnt = collections.Counter(nums)
        for v in cnt.values():
            if self.is_prime(v):
                return True
        return False

    def is_prime(self, v: int) -> bool:
        if v == 1:
            return False
        for i in range(2, int(sqrt(v)) + 1):
            if v % i == 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
