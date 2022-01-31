# Given a string s, return the number of substrings that have only one distinct 
# letter. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", 
# "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aaaaaaaaaa"
# Output: 55
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] consists of only lowercase English letters. 
#  
#  Related Topics Math String 👍 256 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countLetters(self, s: str) -> int:
        prev = s[0]
        res = 0
        cnt = 0
        for char in s:
            if prev == char:
                cnt += 1
            else:
                res += (1 + cnt) * cnt // 2
                prev = char
                cnt = 1
        res += (1 + cnt) * cnt // 2
        return res
# leetcode submit region end(Prohibit modification and deletion)
