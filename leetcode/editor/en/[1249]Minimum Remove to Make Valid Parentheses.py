# Given a string s of '(' , ')' and lowercase English characters. 
# 
#  Your task is to remove the minimum number of parentheses ( '(' or ')', in 
# any positions ) so that the resulting parentheses string is valid and return any 
# valid string. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, contains only lowercase characters, or 
#  It can be written as AB (A concatenated with B), where A and B are valid 
# strings, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either'(' , ')', or lowercase English letter. 
#  
# 
#  Related Topics String Stack 👍 5889 👎 108


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        remove = []
        for i, v in enumerate(s):
            if v == "(":
                stack.append(("(", i))
            elif v==")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                    continue
                else:
                    remove.append((")", i))
        remove += stack
        for _,i in remove[::-1]:
            del s[i]

        return "".join(s)

# leetcode submit region end(Prohibit modification and deletion)