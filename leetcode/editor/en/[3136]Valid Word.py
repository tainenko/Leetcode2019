# A word is considered valid if: 
# 
#  
#  It contains a minimum of 3 characters. 
#  It consists of the digits 0-9, and the uppercase and lowercase English 
# letters. (Not necessary to have all of them.) 
#  It includes at least one vowel. 
#  It includes at least one consonant. 
#  
# 
#  You are given a string word. 
# 
#  Return true if word is valid, otherwise, return false. 
# 
#  Notes: 
# 
#  
#  'a', 'e', 'i', 'o', 'u', and their uppercases are vowels. 
#  A consonant is an English letter that is not a vowel. 
#  
# 
#  
#  Example 1: 
# 
#  
#  Input: word = "234Adas" 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  This word satisfies the conditions. 
# 
#  Example 2: 
# 
#  
#  Input: word = "b3" 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  The length of this word is fewer than 3, and does not have a vowel. 
# 
#  Example 3: 
# 
#  
#  Input: word = "a3$e" 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  This word contains a '$' character and does not have a consonant. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 20 
#  word consists of English uppercase and lowercase letters, digits, '@', '#', 
# and '$'. 
#  
# 
#  👍 41 👎 72
import string


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        consonants = set(string.ascii_lowercase + string.ascii_uppercase) - vowels
        if not any(c in vowels for c in word):
            return False
        if not any(c in consonants for c in word):
            return False
        if not all(c.isalnum() for c in word):
            return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
