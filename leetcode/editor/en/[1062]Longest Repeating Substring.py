# Given a string s, return the length of the longest repeating substrings. If 
# no repeating substring exists, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of 
# which occurs twice.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics String Binary Search Dynamic Programming Rolling Hash Suffix 
# Array Hash Function 👍 599 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res

# leetcode submit region end(Prohibit modification and deletion)
