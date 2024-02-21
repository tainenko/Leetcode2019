# Given two positive integers a and b, return the count of numbers having 
# unique digits in the range [a, b] (inclusive).
# 
#  
#  Example 1: 
# 
#  
# Input: a = 1, b = 20
# Output: 19
# Explanation: All the numbers in the range [1, 20] have unique digits except 11
# . Hence, the answer is 19.
#  
# 
#  Example 2: 
# 
#  
# Input: a = 9, b = 19
# Output: 10
# Explanation: All the numbers in the range [9, 19] have unique digits except 11
# . Hence, the answer is 10. 
#  
# 
#  Example 3: 
# 
#  
# Input: a = 80, b = 120
# Output: 27
# Explanation: There are 41 numbers in the range [80, 120], 27 of which have 
# unique digits.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= a <= b <= 1000 
#  
# 
#  Related Topics Hash Table Math Dynamic Programming 👍 12 👎 3


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        return sum([len(set(str(num))) == len(str(num)) for num in range(a, b + 1)])
# leetcode submit region end(Prohibit modification and deletion)
