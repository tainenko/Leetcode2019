# An integer has monotone increasing digits if and only if each pair of 
# adjacent digits x and y satisfy x <= y. 
# 
#  Given an integer n, return the largest number that is less than or equal to 
# n with monotone increasing digits. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 10
# Output: 9
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1234
# Output: 1234
#  
# 
#  Example 3: 
# 
#  
# Input: n = 332
# Output: 299
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics Math Greedy 👍 1260 👎 101


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
