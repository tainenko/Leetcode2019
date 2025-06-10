# Given an integer n, return the smallest prime palindrome greater than or 
# equal to n. 
# 
#  An integer is prime if it has exactly two divisors: 1 and itself. Note that 1
#  is not a prime number. 
# 
#  
#  For example, 2, 3, 5, 7, 11, and 13 are all primes. 
#  
# 
#  An integer is a palindrome if it reads the same from left to right as it 
# does from right to left. 
# 
#  
#  For example, 101 and 12321 are palindromes. 
#  
# 
#  The test cases are generated so that the answer always exists and is in the 
# range [2, 2 * 10⁸]. 
# 
#  
#  Example 1: 
#  Input: n = 6
# Output: 7
#  
#  Example 2: 
#  Input: n = 8
# Output: 11
#  
#  Example 3: 
#  Input: n = 13
# Output: 101
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁸ 
#  
# 
#  Related Topics Math Number Theory 👍 470 👎 840


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            v = 2
            while v * v <= n:
                if n % v == 0:
                    return False
                v += 1
            return True

        def is_palindrome(n: int) -> bool:
            n = str(n)
            i = 0
            j = len(n) - 1
            while i < j:
                if n[i] != n[j]:
                    return False
                i += 1
                j -= 1

            return True

        while 1:
            if is_palindrome(n) and is_prime(n):
                return n
            if 10 ** 7 < n < 10 ** 8:
                n = 10 ** 8
            n += 1

# leetcode submit region end(Prohibit modification and deletion)
