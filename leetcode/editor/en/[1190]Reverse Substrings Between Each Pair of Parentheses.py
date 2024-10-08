# You are given a string s that consists of lower case English letters and 
# brackets. 
# 
#  Reverse the strings in each pair of matching parentheses, starting from the 
# innermost one. 
# 
#  Your result should not contain any brackets. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(abcd)"
# Output: "dcba"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is 
# reversed.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, 
# the whole string.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s only contains lower case English characters and parentheses. 
#  It is guaranteed that all parentheses are balanced. 
#  
# 
#  Related Topics String Stack 👍 2819 👎 119


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                tail = stack.pop()
                stack[-1] += tail[::-1]
            else:
                stack[-1] += c
        return stack[-1]

# leetcode submit region end(Prohibit modification and deletion)
