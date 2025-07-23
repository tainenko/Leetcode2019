# Given an array of integers arr, find the sum of min(b), where b ranges over 
# every (contiguous) subarray of arr. Since the answer may be large, return the 
# answer modulo 10⁹ + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,
# 2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [11,81,94,43,3]
# Output: 444
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 3 * 10⁴ 
#  1 <= arr[i] <= 3 * 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming Stack Monotonic Stack 👍 8731 👎 699
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
