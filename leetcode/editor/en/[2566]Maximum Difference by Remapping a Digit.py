# You are given an integer num. You know that Danny Mittal will sneakily remap 
# one of the 10 possible digits (0 to 9) to another digit. 
# 
#  Return the difference between the maximum and minimum values Danny can make 
# by remapping exactly one digit in num. 
# 
#  Notes: 
# 
#  
#  When Danny remaps a digit d1 to another digit d2, Danny replaces all 
# occurrences of d1 in num with d2. 
#  Danny can remap a digit to itself, in which case num does not change. 
#  Danny can remap different digits for obtaining minimum and maximum values 
# respectively. 
#  The resulting number after remapping can contain leading zeroes. 
#  We mentioned "Danny Mittal" to congratulate him on being in the top 10 in 
# Weekly Contest 326. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: num = 11891
# Output: 99009
# Explanation: 
# To achieve the maximum value, Danny can remap the digit 1 to the digit 9 to 
# yield 99899.
# To achieve the minimum value, Danny can remap the digit 1 to the digit 0, 
# yielding 890.
# The difference between these two numbers is 99009.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 90
# Output: 99
# Explanation:
# The maximum value that can be returned by the function is 99 (if 0 is 
# replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is 
# replaced by 0).
# Thus, we return 99. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10⁸ 
#  
# 
#  👍 144 👎 29


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num1 = str(num)
        digit = ""
        for c in num1:
            if c != "9":
                digit = c
                break
        if digit:
            num1 = num1.replace(digit, "9")
        num2 = str(num)
        num2 = num2.replace(num2[0], "0")
        return int(num1) - int(num2)

# leetcode submit region end(Prohibit modification and deletion)
