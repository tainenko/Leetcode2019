# Given an integer n, add a dot (".") as the thousands separator and return it 
# in string format. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 987
# Output: "987"
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1234
# Output: "1.234"
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 2³¹ - 1 
#  
#  Related Topics String 👍 320 👎 11


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f'{n:,}'.replace(",", '.')

# leetcode submit region end(Prohibit modification and deletion)
