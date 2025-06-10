# You are given an integer n. We reorder the digits in any order (including the 
# original order) such that the leading digit is not zero. 
# 
#  Return true if and only if we can do this so that the resulting number is a 
# power of two. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: n = 10
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁹ 
#  
# 
#  Related Topics Hash Table Math Sorting Counting Enumeration 👍 2135 👎 440


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def convert(n: int) -> list:
            cnt = [0] * 10
            while n:
                n, v = divmod(n, 10)
                cnt[v] += 1
            return cnt

        i, s = 1, convert(n)
        while i <= 10 ** 9:
            if s == convert(i):
                return True
            i <<= 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
