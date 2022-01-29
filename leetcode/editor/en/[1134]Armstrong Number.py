# Given an integer n, return true if and only if it is an Armstrong number. 
# 
#  The k-digit number n is an Armstrong number if and only if the kᵗʰ power of 
# each digit sums to n. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 153
# Output: true
# Explanation: 153 is a 3-digit number, and 153 = 1³ + 5³ + 3³.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 123
# Output: false
# Explanation: 123 is a 3-digit number, and 123 != 1³ + 2³ + 3³ = 36.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁸ 
#  
#  Related Topics Math 👍 145 👎 16


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        return n == sum(int(x) ** k for x in str(n))

# leetcode submit region end(Prohibit modification and deletion)
