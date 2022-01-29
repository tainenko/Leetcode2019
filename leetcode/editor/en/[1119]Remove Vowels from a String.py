# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and 
# return the new string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aeiou"
# Output: ""
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of only lowercase English letters. 
#  
#  Related Topics String 👍 245 👎 102


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeVowels(self, s: str) -> str:
        for c in ['a', 'e', 'i', 'o', 'u']:
            s = s.replace(c, '')
        return s

# leetcode submit region end(Prohibit modification and deletion)
