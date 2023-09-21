# Implement a basic calculator to evaluate a simple expression string. 
# 
#  The expression string contains only non-negative integers, '+', '-', '*', '/
# ' operators, and open '(' and closing parentheses ')'. The integer division 
# should truncate toward zero. 
# 
#  You may assume that the given expression is always valid. All intermediate 
# results will be in the range of [-2³¹, 2³¹ - 1]. 
# 
#  Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval(). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "1+1"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: s = "6-4/2"
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s <= 10⁴ 
#  s consists of digits, '+', '-', '*', '/', '(', and ')'. 
#  s is a valid expression. 
#  
# 
#  Related Topics Math String Stack Recursion 👍 1066 👎 273


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        op = '+'
        i = 0
        num = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '(':
                j = self.find_closing(s, i)
                num = self.calculate(s[i + 1:j])
                i = j
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)
                op = c
                num = 0
            i += 1
        return sum(stack)

    def find_closing(self, s: str, idx: int) -> int:
        level = 0
        for i in range(idx, len(s)):
            if s[i] == '(':
                level += 1
            elif s[i] == ')':
                level -= 1
                if level == 0:
                    return i
        return i

# leetcode submit region end(Prohibit modification and deletion)
