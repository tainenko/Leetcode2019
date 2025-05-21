# Given an array of strings nums containing n unique binary strings each of 
# length n, return a binary string of length n that does not appear in nums. If there 
# are multiple answers, you may return any of them. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" 
# would also be correct.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 16 
#  nums[i].length == n 
#  nums[i] is either '0' or '1'. 
#  All the strings of nums are unique. 
#  
# 
#  Related Topics Array Hash Table String Backtracking 👍 2517 👎 88


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        existed = set(nums)
        length = len(nums[0])
        i = 0
        while True:
            num = bin(i)[2:].zfill(length)
            if num not in existed:
                return num
            i += 1

# leetcode submit region end(Prohibit modification and deletion)
