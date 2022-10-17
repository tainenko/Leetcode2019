# Given two positive integers a and b, return the number of common factors of a 
# and b. 
# 
#  An integer x is a common factor of a and b if x divides both a and b. 
# 
#  
#  Example 1: 
# 
#  
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
#  
# 
#  Example 2: 
# 
#  
# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= a, b <= 1000 
#  
# 
#  Related Topics Math Enumeration Number Theory 👍 184 👎 2


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        lcm = self.lcm(a, b)
        cnt = 0
        for i in range(1, lcm + 1):
            if lcm % i == 0:
                cnt += 1
        return cnt

    def lcm(self, a, b):
        if a < b:
            return self.lcm(b, a)
        if b == 0:
            return a
        return self.lcm(b, a % b)

# leetcode submit region end(Prohibit modification and deletion)
