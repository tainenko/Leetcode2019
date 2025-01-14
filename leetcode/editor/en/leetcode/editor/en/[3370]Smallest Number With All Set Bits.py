# You are given a positive number n. 
# 
#  Return the smallest number x greater than or equal to n, such that the 
# binary representation of x contains only set bits 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 5 
#  
# 
#  Output: 7 
# 
#  Explanation: 
# 
#  The binary representation of 7 is "111". 
# 
#  Example 2: 
# 
#  
#  Input: n = 10 
#  
# 
#  Output: 15 
# 
#  Explanation: 
# 
#  The binary representation of 15 is "1111". 
# 
#  Example 3: 
# 
#  
#  Input: n = 3 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  The binary representation of 3 is "11". 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  
# 
#  Related Topics Math Bit Manipulation 👍 53 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while True:
            x = 1 << i
            if x > n:
                return x - 1
            i += 1

# leetcode submit region end(Prohibit modification and deletion)
