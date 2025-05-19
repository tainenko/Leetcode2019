# There is a number n between 0 and 2³⁰ - 1 (both inclusive) that you have to 
# find. 
# 
#  There is a pre-defined API int commonBits(int num) that helps you with your 
# mission. But here is the challenge, every time you call this function, n changes 
# in some way. But keep in mind, that you have to find the initial value of n. 
# 
#  commonBits(int num) acts as follows: 
# 
#  
#  Calculate count which is the number of bits where both n and num have the 
# same value in that position of their binary representation. 
#  n = n XOR num 
#  Return count. 
#  
# 
#  Return the number n. 
# 
#  Note: In this world, all numbers are between 0 and 2³⁰ - 1 (both inclusive), 
# thus for counting common bits, we see only the first 30 bits of those numbers. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 2³⁰ - 1 
#  0 <= num <= 2³⁰ - 1 
#  If you ask for some num out of the given range, the output wouldn't be 
# reliable. 
#  
# 
#  Related Topics Bit Manipulation Interactive 👍 13 👎 3


# leetcode submit region begin(Prohibit modification and deletion)
# Definition of commonBits API.
# def commonBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        res = 0
        for i in range(32):
            count1 = commonBits(1 << i)
            count2 = commonBits(1 << i)
            if count1 > count2:
                res |= 1 << i
        return res
# leetcode submit region end(Prohibit modification and deletion)
