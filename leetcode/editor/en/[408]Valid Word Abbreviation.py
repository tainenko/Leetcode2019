# A string can be abbreviated by replacing any number of non-adjacent, non-
# empty substrings with their lengths. The lengths should not have leading zeros. 
# 
#  For example, a string such as "substitution" could be abbreviated as (but 
# not limited to): 
# 
#  
#  "s10n" ("s ubstitutio n") 
#  "sub4u4" ("sub stit u tion") 
#  "12" ("substitution") 
#  "su3i1u2on" ("su bst i t u ti on") 
#  "substitution" (no substrings replaced) 
#  
# 
#  The following are not valid abbreviations: 
# 
#  
#  "s55n" ("s ubsti tutio n", the replaced substrings are adjacent) 
#  "s010n" (has leading zeros) 
#  "s0ubstitution" (replaces an empty substring) 
#  
# 
#  Given a string word and an abbreviation abbr, return whether the string 
# matches the given abbreviation. 
# 
#  A substring is a contiguous non-empty sequence of characters within a string.
#  
# 
#  
#  Example 1: 
# 
#  
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" (
# "i nternational iz atio n").
#  
# 
#  Example 2: 
# 
#  
# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 20 
#  word consists of only lowercase English letters. 
#  1 <= abbr.length <= 10 
#  abbr consists of lowercase English letters and digits. 
#  All the integers in abbr will fit in a 32-bit integer. 
#  
#  Related Topics Two Pointers String 👍 292 👎 1211


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        target = ""
        num = ""
        length = 0
        for i in range(len(abbr)):
            if abbr[i].isalpha():
                if num:
                    if num[0] == '0':
                        return False
                    length += int(num)
                    target += '*' * int(num)
                    num = ""
                target += abbr[i]
                length += 1
                if length > len(word):
                    return False
            else:
                num += abbr[i]
        if num:
            if num[0] == '0':
                return False
            length += int(num)
            if length > len(word):
                return False
            target += '*' * int(num)
        if length != len(word):
            return False
        for i in range(len(word)):
            if target[i] != '*' and word[i] != target[i]:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
