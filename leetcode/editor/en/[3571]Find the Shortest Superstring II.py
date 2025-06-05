# You are given two strings, s1 and s2. Return the shortest possible string 
# that contains both s1 and s2 as substrings. If there are multiple valid answers, 
# return any one of them. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s1 = "aba", s2 = "bab" 
#  
# 
#  Output: "abab" 
# 
#  Explanation: 
# 
#  "abab" is the shortest string that contains both "aba" and "bab" as 
# substrings. 
# 
#  Example 2: 
# 
#  
#  Input: s1 = "aa", s2 = "aaa" 
#  
# 
#  Output: "aaa" 
# 
#  Explanation: 
# 
#  "aa" is already contained within "aaa", so the shortest superstring is "aaa".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s1.length <= 100 
#  1 <= s2.length <= 100 
#  s1 and s2 consist of lowercase English letters only. 
#  
# 
#  👍 3 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        if m > n:
            return self.shortestSuperstring(s2, s1)

        if s1 in s2:
            return s2
        for i in range(m):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2
            if s2.endswith(s1[:m - i]):
                return s2 + s1[m - i:]

        return s1 + s2
# leetcode submit region end(Prohibit modification and deletion)
