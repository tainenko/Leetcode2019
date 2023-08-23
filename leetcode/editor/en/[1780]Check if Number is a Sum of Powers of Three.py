# Given an integer n, return true if it is possible to represent n as the sum 
# of distinct powers of three. Otherwise, return false. 
# 
#  An integer y is a power of three if there exists an integer x such that y == 
# 3ˣ. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 12
# Output: true
# Explanation: 12 = 3¹ + 3²
#  
# 
#  Example 2: 
# 
#  
# Input: n = 91
# Output: true
# Explanation: 91 = 3⁰ + 3² + 3⁴
#  
# 
#  Example 3: 
# 
#  
# Input: n = 21
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁷ 
#  
# 
#  Related Topics Math 👍 895 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 > 1:
                return False
            n //= 3
        return True
# leetcode submit region end(Prohibit modification and deletion)
