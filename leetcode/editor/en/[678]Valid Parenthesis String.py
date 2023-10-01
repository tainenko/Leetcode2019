# Given a string s containing only three types of characters: '(', ')' and '*', 
# return true if s is valid. 
# 
#  The following rules define a valid string: 
# 
#  
#  Any left parenthesis '(' must have a corresponding right parenthesis ')'. 
#  Any right parenthesis ')' must have a corresponding left parenthesis '('. 
#  Left parenthesis '(' must go before the corresponding right parenthesis ')'. 
# 
#  '*' could be treated as a single right parenthesis ')' or a single left 
# parenthesis '(' or an empty string "". 
#  
# 
#  
#  Example 1: 
#  Input: s = "()"
# Output: true
#  
#  Example 2: 
#  Input: s = "(*)"
# Output: true
#  
#  Example 3: 
#  Input: s = "(*))"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s[i] is '(', ')' or '*'. 
#  
# 
#  Related Topics String Dynamic Programming Stack Greedy 👍 4886 👎 123


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        x = 0
        for c in s:
            if c in '(*':
                x += 1
            elif x:
                x -= 1
            else:
                return False
        x = 0
        for c in s[::-1]:
            if c in '*)':
                x += 1
            elif x:
                x -= 1
            else:
                return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
