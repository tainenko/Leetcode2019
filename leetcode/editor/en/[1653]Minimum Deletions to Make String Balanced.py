# You are given a string s consisting only of characters 'a' and 'b'. 
# 
#  You can delete any number of characters in s to make s balanced. s is 
# balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 
# 'a'. 
# 
#  Return the minimum number of deletions needed to make s balanced. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"),
#  or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# 
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is 'a' or 'b'. 
#  
# 
#  Related Topics String Dynamic Programming Stack 👍 1234 👎 35


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        dp = 0
        for c in s:
            if c == 'b':
                b += 1
                continue
            else:
                dp = min(dp + 1, b)
        return dp

# leetcode submit region end(Prohibit modification and deletion)
