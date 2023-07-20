# Given a positive integer num represented as a string, return the integer num 
# without trailing zeros as a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and 
# return integer "512301".
#  
# 
#  Example 2: 
# 
#  
# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num.length <= 1000 
#  num consists of only digits. 
#  num doesn't have any leading zeros. 
#  
# 
#  Related Topics String 👍 180 👎 7


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = len(num) - 1
        while num[idx] == "0":
            idx -= 1
        return num[:idx + 1]

# leetcode submit region end(Prohibit modification and deletion)
