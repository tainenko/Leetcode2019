# Return the number of permutations of 1 to n so that prime numbers are at 
# prime indices (1-indexed.) 
# 
#  (Recall that an integer is prime if and only if it is greater than 1, and 
# cannot be written as a product of two positive integers both smaller than it.) 
# 
#  Since the answer may be large, return the answer modulo 10^9 + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] 
# is not because the prime number 5 is at index 1.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 100
# Output: 682289015
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 100 
#  
#  Related Topics Math 👍 206 👎 322


# leetcode submit region begin(Prohibit modification and deletion)
from math import factorial


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt_prime = self.countPrime(n)
        return (factorial(cnt_prime) * factorial(n - cnt_prime)) % (10 ** 9 + 7)

    def countPrime(self, n):
        primes = [False] * (n + 1)
        cnt = 0
        for i in range(2, n + 1):
            if primes[i]:
                continue
            cnt += 1
            for j in range(i, n + 1, i):
                primes[j] = True
        return cnt

# leetcode submit region end(Prohibit modification and deletion)
