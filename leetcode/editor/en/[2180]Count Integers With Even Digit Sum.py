# Given a positive integer num, return the number of positive integers less 
# than or equal to num whose digit sums are even. 
# 
#  The digit sum of a positive integer is the sum of all its digits. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 
# 4.    
#  
# 
#  Example 2: 
# 
#  
# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 1000 
#  
# 
#  Related Topics Math Simulation 👍 324 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for n in range(1, num + 1):
            total = sum([int(digit) for digit in str(n)])
            if total % 2 == 0:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
