# You are given a 0-indexed string s consisting of only lowercase English 
# letters. Return the number of substrings in s that begin and end with the same 
# character. 
# 
#  A substring is a contiguous non-empty sequence of characters within a string.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcba"
# Output: 7
# Explanation:
# The substrings of length 1 that start and end with the same letter are: "a", 
# "b", "c", "b", and "a".
# The substring of length 3 that starts and ends with the same letter is: "bcb".
# 
# The substring of length 5 that starts and ends with the same letter is: 
# "abcba".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abacad"
# Output: 9
# Explanation:
# The substrings of length 1 that start and end with the same letter are: "a", 
# "b", "a", "c", "a", and "d".
# The substrings of length 3 that start and end with the same letter are: "aba" 
# and "aca".
# The substring of length 5 that starts and ends with the same letter is: 
# "abaca".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a"
# Output: 1
# Explanation:
# The substring of length 1 that starts and ends with the same letter is: "a".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists only of lowercase English letters. 
#  
# 
#  Related Topics Hash Table Math String Counting Prefix Sum 👍 103 👎 6


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
        for v in idx.values():
            res += len(v) * (len(v) - 1) // 2
        return res + len(s)
# leetcode submit region end(Prohibit modification and deletion)
