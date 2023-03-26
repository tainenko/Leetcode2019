# Given a pattern and a string s, return true if s matches the pattern. 
# 
#  A string s matches a pattern if there is some bijective mapping of single 
# characters to strings such that if each character in pattern is replaced by the 
# string it maps to, then the resulting string is s. A bijective mapping means that 
# no two characters map to the same string, and no character maps to two different 
# strings. 
# 
#  
#  Example 1: 
# 
#  
# Input: pattern = "abab", s = "redblueredblue"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "red"
# 'b' -> "blue" 
# 
#  Example 2: 
# 
#  
# Input: pattern = "aaaa", s = "asdasdasdasd"
# Output: true
# Explanation: One possible mapping is as follows:
# 'a' -> "asd"
#  
# 
#  Example 3: 
# 
#  
# Input: pattern = "aabb", s = "xyzabcxzyabc"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= pattern.length, s.length <= 20 
#  pattern and s consist of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Backtracking 👍 782 👎 62


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.is_match(pattern, s, {}, set())

    def is_match(self, pattern: str, s: str, mapping: dict, used: set):
        if not pattern:
            return not s

        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not s.startswith(word):
                return False
            return self.is_match(pattern[1:], s[len(word):], mapping, used)

        for i in range(len(s)):
            word = s[:i + 1]
            if word in used:
                continue
            mapping[char] = word
            used.add(word)
            if self.is_match(pattern[1:], s[i + 1:], mapping, used):
                return True
            del mapping[char]
            used.remove(word)
        return False
# leetcode submit region end(Prohibit modification and deletion)
