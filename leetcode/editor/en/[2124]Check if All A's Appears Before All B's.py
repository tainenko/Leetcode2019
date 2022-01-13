# Given a string s consisting of only the characters 'a' and 'b', return true 
# if every 'a' appears before every 'b' in the string. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5
# .
# Hence, every 'a' appears before every 'b' and we return true.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab"
# Output: false
# Explanation:
# There is an 'a' at index 2 and a 'b' at index 1.
# Hence, not every 'a' appears before every 'b' and we return false.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "bbb"
# Output: true
# Explanation:
# There are no 'a's, hence, every 'a' appears before every 'b' and we return 
# true.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s[i] is either 'a' or 'b'. 
#  
#  Related Topics String 👍 147 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkString(self, s: str) -> bool:
        if not s:
            return True
        idx_a = -1
        idx_b = len(s) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a':
                idx_a = i
                break
        for i in range(len(s)):
            if s[i] == 'b':
                idx_b = i
                break
        return idx_a <= idx_b

# leetcode submit region end(Prohibit modification and deletion)
