# You are given a binary string s consisting only of zeroes and ones. 
# 
#  A substring of s is considered balanced if all zeroes are before ones and 
# the number of zeroes is equal to the number of ones inside the substring. Notice 
# that the empty substring is considered a balanced substring. 
# 
#  Return the length of the longest balanced substring of s. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4. 
#  
# 
#  Example 3: 
# 
#  
# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so 
# the answer is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 50 
#  '0' <= s[i] <= '1' 
#  
# 
#  👍 170 👎 12


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] == "0" and s[i] == "1":
                zeros = 0
                ones = 0
                for j in range(i - 1, -1, -1):
                    if s[j] == "1":
                        break
                    zeros += 1
                for k in range(i, len(s)):
                    if s[k] == "0":
                        break
                    ones += 1
                res = max(res, min(ones, zeros))
        return res * 2
# leetcode submit region end(Prohibit modification and deletion)
