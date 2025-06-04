# Given two strings s and t, find the number of ways you can choose a non-empty 
# substring of s and replace a single character by a different character such 
# that the resulting substring is a substring of t. In other words, find the number 
# of substrings in s that differ from some substring in t by exactly one character. 
# 
# 
#  For example, the underlined substrings in "computer" and "computation" only 
# differ by the 'e'/'a', so this is a valid way. 
# 
#  Return the number of substrings that satisfy the condition above. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that 
# differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
#  
# 
# Example 2:
# 
#  
# Input: s = "ab", t = "bb"
# Output: 3
# Explanation: The following are the pairs of substrings from s and t that 
# differ by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# ​​​​The underlined portions are the substrings that are chosen from s and t.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 100 
#  s and t consist of lowercase English letters only. 
#  
# 
#  Related Topics Hash Table String Dynamic Programming Enumeration 👍 1177 👎 3
# 54


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i, a in enumerate(s):
            for j, b in enumerate(t):
                if a != b:
                    l = r = 0
                    while i > l and j > l and s[i - l - 1] == t[j - l - 1]:
                        l += 1
                    while i + r + 1 < len(s) and j + r + 1 < len(t) and s[i + r + 1] == t[j + r + 1]:
                        r += 1
                    ans += (l + 1) * (r + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
