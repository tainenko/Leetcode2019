# Given a string s, find the sum of the 3 largest unique prime numbers that can 
# be formed using any of its substrings. 
# 
#  Return the sum of the three largest unique prime numbers that can be formed. 
# If fewer than three exist, return the sum of all available primes. If no prime 
# numbers can be formed, return 0. 
# 
#  Note: Each prime number should be counted only once, even if it appears in 
# multiple substrings. Additionally, when converting a substring to an integer, any 
# leading zeros are ignored. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "12234" 
#  
# 
#  Output: 1469 
# 
#  Explanation: 
# 
#  
#  The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 
# 223, and 1223. 
#  The 3 largest primes are 1223, 223, and 23. Their sum is 1469. 
#  
# 
#  Example 2: 
# 
#  
#  Input: s = "111" 
#  
# 
#  Output: 11 
# 
#  Explanation: 
# 
#  
#  The unique prime number formed from the substrings of "111" is 11. 
#  Since there is only one prime number, the sum is 11. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10 
#  s consists of only digits. 
#  
# 
#  Related Topics Hash Table Math String Sorting Number Theory 👍 44 👎 7


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        ans = 0
        seen = set()
        for i in range(len(s)):
            num = 0
            for j in range(i, len(s)):
                num = 10 * num + int(s[j])
                if num not in seen and self.is_prime(num):
                    seen.add(num)
        return sum(sorted(seen)[-3:] if len(seen) > 2 else seen)

    def is_prime(self, n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
