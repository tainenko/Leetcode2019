# Given a string s representing a valid expression, implement a basic 
# calculator to evaluate it, and return the result of the evaluation. 
# 
#  Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval(). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "1 + 1"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: s = " 2-1 + 2 "
# Output: 3
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s consists of digits, '+', '-', '(', ')', and ' '. 
#  s represents a valid expression. 
#  '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid). 
# 
#  '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid). 
# 
#  There will be no two consecutive operators in the input. 
#  Every number and running calculation will fit in a signed 32-bit integer. 
#  
# 
#  Related Topics Math String Stack Recursion 👍 5801 👎 426


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        stack = [sign]
        num = 0
        for c in s:
            print(c)
            if c.isdigit():
                num = 10 * num + (ord(c) - ord("0"))
            elif c == "(":
                stack.append(sign)
            elif c == ")":
                stack.pop()
            elif c == "+" or c == "-":
                res += (sign * num)
                sign = (1 if c == "+" else -1) * stack[-1]
                num = 0
        return res + sign * num

# leetcode submit region end(Prohibit modification and deletion)
