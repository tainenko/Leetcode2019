# Given an integer n, return true if n has exactly three positive divisors. 
# Otherwise, return false. 
# 
#  An integer m is a divisor of n if there exists an integer k such that n = k *
#  m. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁴ 
#  
#  Related Topics Math 👍 244 👎 18


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
            if cnt > 3:
                return False
        return cnt == 3
# leetcode submit region end(Prohibit modification and deletion)
