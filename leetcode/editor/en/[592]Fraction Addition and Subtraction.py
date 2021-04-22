# Given a string representing an expression of fraction addition and subtraction
# , you need to return the calculation result in string format. The final result s
# hould be irreducible fraction. If your final result is an integer, say 2, you ne
# ed to change it to the format of fraction that has denominator 1. So in this cas
# e, 2 should be converted to 2/1. 
# 
#  Example 1: 
#  
# Input:"-1/2+1/2"
# Output: "0/1"
#  
#  
# 
#  Example 2: 
#  
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
#  
#  
# 
#  Example 3: 
#  
# Input:"1/3-1/2"
# Output: "-1/6"
#  
#  
# 
#  Example 4: 
#  
# Input:"5/3+1/3"
# Output: "2/1"
#  
#  
# 
#  Note: 
#  
#  The input string only contains '0' to '9', '/', '+' and '-'. So does the outp
# ut. 
#  Each fraction (input and output) has format ±numerator/denominator. If the fi
# rst input fraction or the output is positive, then '+' will be omitted. 
#  The input only contains valid irreducible fractions, where the numerator and 
# denominator of each fraction will always be in the range [1,10]. If the denomina
# tor is 1, it means this fraction is actually an integer in a fraction format def
# ined above. 
#  The number of given fractions will be in the range [1,10]. 
#  The numerator and denominator of the final result are guaranteed to be valid 
# and in the range of 32-bit int. 
#  
#  Related Topics Math 
#  👍 231 👎 352


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
# leetcode submit region end(Prohibit modification and deletion)
