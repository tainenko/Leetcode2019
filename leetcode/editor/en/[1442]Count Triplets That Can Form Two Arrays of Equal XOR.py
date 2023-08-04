# Given an array of integers arr. 
# 
#  We want to select three indices i, j and k where (0 <= i < j <= k < arr.
# length). 
# 
#  Let's define a and b as follows: 
# 
#  
#  a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] 
#  b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] 
#  
# 
#  Note that ^ denotes the bitwise-xor operation. 
# 
#  Return the number of triplets (i, j and k) Where a == b. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,1,1,1,1]
# Output: 10
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[i] <= 10⁸ 
#  
# 
#  Related Topics Array Hash Table Math Bit Manipulation Prefix Sum 👍 1277 👎 5
# 6
import itertools
from _operator import xor


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        xors = [0] + list(itertools.accumulate(arr, xor))
        for j in range(1, len(arr)):
            for i in range(0, j):
                xors_i = xors[j] ^ xors[i]
                for k in range(j, len(arr)):
                    if xors_i == xors[j] ^ xors[k + 1]:
                        res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
