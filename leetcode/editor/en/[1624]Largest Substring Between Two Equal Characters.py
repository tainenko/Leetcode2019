# Given a string s, return the length of the longest substring between two 
# equal characters, excluding the two characters. If there is no such substring return 
# -1. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 
# 'a's. 
# 
#  Example 2: 
# 
#  
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 300 
#  s contains only lowercase English letters. 
#  
#  Related Topics Hash Table String 👍 383 👎 24


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        for idx, c in enumerate(s):
            if c not in m:
                m[c] = idx
        res = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] in m:
                res = max(res, i - m[s[i]] - 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
