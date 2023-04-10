# Given a binary array data, return the minimum number of swaps required to 
# group all 1’s present in the array together in any place in the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation: There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.
#  
# 
#  Example 2: 
# 
#  
# Input: data = [0,0,0,1,0]
# Output: 0
# Explanation: Since there is only one 1 in the array, no swaps are needed.
#  
# 
#  Example 3: 
# 
#  
# Input: data = [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1
# ].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= data.length <= 10⁵ 
#  data[i] is either 0 or 1. 
#  
# 
#  Related Topics Array Sliding Window 👍 1087 👎 13


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total = sum(data)
        i = 0
        tmp = sum(data[i:total])
        res = total - tmp
        if res == 0:
            return 0
        for j in range(total, len(data)):
            tmp += data[j]
            tmp -= data[i]
            res = min(res, total - tmp)
            i += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)
