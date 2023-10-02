# In combinatorial mathematics, a derangement is a permutation of the elements 
# of a set, such that no element appears in its original position. 
# 
#  You are given an integer n. There is originally an array consisting of n 
# integers from 1 to n in ascending order, return the number of derangements it can 
# generate. Since the answer may be huge, return it modulo 10⁹ + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] 
# and [3,1,2].
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁶ 
#  
# 
#  Related Topics Math Dynamic Programming 👍 213 👎 161


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = b, (i - 1) * (a + b) % mod
        return b
# leetcode submit region end(Prohibit modification and deletion)
