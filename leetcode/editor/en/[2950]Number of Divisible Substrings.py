# Each character of the English alphabet has been mapped to a digit as shown 
# below. 
# 
#  
# 
#  A string is divisible if the sum of the mapped values of its characters is 
# divisible by its length. 
# 
#  Given a string s, return the number of divisible substrings of s. 
# 
#  A substring is a contiguous non-empty sequence of characters within a string.
#  
# 
#  
#  Example 1: 
# 
#  
#  
#  
#  Substring 
#  Mapped 
#  Sum 
#  Length 
#  Divisible? 
#  
#  
#  a 
#  1 
#  1 
#  1 
#  Yes 
#  
#  
#  s 
#  7 
#  7 
#  1 
#  Yes 
#  
#  
#  d 
#  2 
#  2 
#  1 
#  Yes 
#  
#  
#  f 
#  3 
#  3 
#  1 
#  Yes 
#  
#  
#  as 
#  1, 7 
#  8 
#  2 
#  Yes 
#  
#  
#  sd 
#  7, 2 
#  9 
#  2 
#  No 
#  
#  
#  df 
#  2, 3 
#  5 
#  2 
#  No 
#  
#  
#  asd 
#  1, 7, 2 
#  10 
#  3 
#  No 
#  
#  
#  sdf 
#  7, 2, 3 
#  12 
#  3 
#  Yes 
#  
#  
#  asdf 
#  1, 7, 2, 3 
#  13 
#  4 
#  No 
#  
#  
#  
# 
#  
# Input: word = "asdf"
# Output: 6
# Explanation: The table above contains the details about every substring of 
# word, and we can see that 6 of them are divisible.
#  
# 
#  Example 2: 
# 
#  
# Input: word = "bdh"
# Output: 4
# Explanation: The 4 divisible substrings are: "b", "d", "h", "bdh".
# It can be shown that there are no other substrings of word that are divisible.
# 
#  
# 
#  Example 3: 
# 
#  
# Input: word = "abcd"
# Output: 6
# Explanation: The 6 divisible substrings are: "a", "b", "c", "d", "ab", "cd".
# It can be shown that there are no other substrings of word that are divisible.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 2000 
#  word consists only of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Counting Prefix Sum 👍 28 👎 6


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        m = {
            "a": 1,
            "b": 1,
            "c": 2,
            "d": 2,
            "e": 2,
            "f": 3,
            "g": 3,
            "h": 3,
            "i": 4,
            "j": 4,
            "k": 4,
            "l": 5,
            "m": 5,
            "n": 5,
            "o": 6,
            "p": 6,
            "q": 6,
            "r": 7,
            "s": 7,
            "t": 7,
            "u": 8,
            "v": 8,
            "w": 8,
            "x": 9,
            "y": 9,
            "z": 9,
        }
        prefix = [0] + list(itertools.accumulate([m[ch] for ch in word]))

        res = len(word)
        for i in range(len(word)):
            for j in range(2, len(word) + 1):
                if i + j > len(word):
                    break
                total = prefix[i + j] - prefix[i]
                if total % j == 0:
                    res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
