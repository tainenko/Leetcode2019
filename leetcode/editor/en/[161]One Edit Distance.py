# Given two strings s and t, return true if they are both one edit distance 
# apart, otherwise return false. 
# 
#  A string s is said to be one distance apart from a string t if you can: 
# 
#  
#  Insert exactly one character into s to get t. 
#  Delete exactly one character from s to get t. 
#  Replace exactly one character of s with a different character to get t. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length, t.length <= 10⁴ 
#  s and t consist of lowercase letters, uppercase letters, and digits. 
#  
#  Related Topics Two Pointers String 👍 1011 👎 157


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if not s and not t:
            return False
        if not s or not t:
            return True
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                return s[i + 1:] == t[i + 1:]
            else:
                return False
        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            return s[i:] == t[i + 1:]
        return True
# leetcode submit region end(Prohibit modification and deletion)
