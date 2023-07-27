# An integer n is strictly palindromic if, for every base b between 2 and n - 2 
# (inclusive), the string representation of the integer n in base b is 
# palindromic. 
# 
#  Given an integer n, return true if n is strictly palindromic and false 
# otherwise. 
# 
#  A string is palindromic if it reads the same forward and backward. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.
# Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4
# Output: false
# Explanation: We only consider base 2: 4 = 100 (base 2), which is not 
# palindromic.
# Therefore, we return false.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  4 <= n <= 10⁵ 
#  
# 
#  Related Topics Math Two Pointers Brainteaser 👍 451 👎 1205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return all(self.is_palindromic(self.int2base(n, base)) for base in range(2, n - 1))

    def int2base(self, n: int, base: int) -> List[int]:
        res = list()
        while n:
            res.append(n % base)
            n //= base
        return res

    def is_palindromic(self, s: List[int]):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
