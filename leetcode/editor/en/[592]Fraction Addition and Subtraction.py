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
import re


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        res = [0, 1]
        tmp = ["", ""]
        idx = 0
        operator = '+'
        for char in expression:
            if char == '+' or char == '-':
                if tmp != ["", ""]:
                    tmp = [int(x) for x in tmp]
                    if res[1] % tmp[1] != 0:
                        deno = res[1] * tmp[1]
                    else:
                        deno = res[1]
                    if operator == '+':
                        res[0] = res[0] * (deno / res[1]) + tmp[0] * (deno / tmp[1])
                    else:
                        res[0] = res[0] * (deno / res[1]) - tmp[0] * (deno / tmp[1])
                    res[1] = deno
                operator = char
                idx = 0
                tmp = ["", ""]
                continue
            if char == '/':
                idx = 1
                continue
            tmp[idx] += char
        tmp = [int(x) for x in tmp]
        if res[1] % tmp[1] != 0:
            deno = res[1] * tmp[1]
        else:
            deno = res[1]
        if operator == '+':
            res[0] = res[0] * (deno / res[1]) + tmp[0] * (deno / tmp[1])
        else:
            res[0] = res[0] * (deno / res[1]) - tmp[0] * (deno / tmp[1])
        res[1] = deno
        if res[0] == 0:
            return "0/1"
        gcd = self.find_gcd(res[1], res[0])
        return "/".join([str(x / gcd) for x in res])

    def find_gcd(self, m, n):
        m = abs(m)
        n = abs(n)
        while n != 0:
            r = m % n
            m = n
            n = r
        return m

# leetcode submit region end(Prohibit modification and deletion)
