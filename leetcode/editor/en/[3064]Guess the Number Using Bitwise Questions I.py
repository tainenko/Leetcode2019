# There is a number n that you have to find. 
# 
#  There is also a pre-defined API int commonSetBits(int num), which returns 
# the number of bits where both n and num are 1 in that position of their binary 
# representation. In other words, it returns the number of set bits in n & num, where 
# & is the bitwise AND operator. 
# 
#  Return the number n. 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 31 
#  
# 
#  Output: 31 
# 
#  Explanation: It can be proven that it's possible to find 31 using the 
# provided API. 
# 
#  Example 2: 
# 
#  
#  Input: n = 33 
#  
# 
#  Output: 33 
# 
#  Explanation: It can be proven that it's possible to find 33 using the 
# provided API. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2³⁰ - 1 
#  0 <= num <= 2³⁰ - 1 
#  If you ask for some num out of the given range, the output wouldn't be 
# reliable. 
#  
# 
#  Related Topics Bit Manipulation Interactive 👍 7 👎 2


# leetcode submit region begin(Prohibit modification and deletion)
# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        return sum(1 << i for i in range(31) if commonSetBits(1 << i))

# leetcode submit region end(Prohibit modification and deletion)
