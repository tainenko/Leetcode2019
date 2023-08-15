# You are given an array arr of positive integers. You are also given the array 
# queries where queries[i] = [lefti, righti]. 
# 
#  For each query i compute the XOR of elements from lefti to righti (that is, 
# arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ). 
# 
#  Return an array answer where answer[i] is the answer to the iᵗʰ query. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8] 
# Explanation: 
# The binary representation of the elements in the array are:
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# Output: [8,0,4,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length, queries.length <= 3 * 10⁴ 
#  1 <= arr[i] <= 10⁹ 
#  queries[i].length == 2 
#  0 <= lefti <= righti < arr.length 
#  
# 
#  Related Topics Array Bit Manipulation Prefix Sum 👍 1379 👎 37
from _operator import xor
from itertools import accumulate


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0] + list(accumulate(arr, xor))
        return [xor(pre_xor[right + 1], pre_xor[left]) for left, right in queries]
# leetcode submit region end(Prohibit modification and deletion)
