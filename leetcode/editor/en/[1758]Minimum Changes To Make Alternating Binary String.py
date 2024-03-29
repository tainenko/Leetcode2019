# You are given a string s consisting only of the characters '0' and '1'. In 
# one operation, you can change any '0' to '1' or vice versa. 
# 
#  The string is called alternating if no two adjacent characters are equal. 
# For example, the string "010" is alternating, while the string "0100" is not. 
# 
#  Return the minimum number of operations needed to make s alternating. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which 
# is alternating.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s[i] is either '0' or '1'. 
#  
# 
#  Related Topics String 👍 445 👎 15


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)
        cnt = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cnt += 1
                s[i] = "1" if s[i] == "0" else "0"
        return min(cnt, len(s) - cnt)

# leetcode submit region end(Prohibit modification and deletion)
