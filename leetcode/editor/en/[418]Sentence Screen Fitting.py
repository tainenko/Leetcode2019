# Given a rows x cols screen and a sentence represented as a list of strings, 
# return the number of times the given sentence can be fitted on the screen. 
# 
#  The order of words in the sentence must remain unchanged, and a word cannot 
# be split into two lines. A single space must separate two consecutive words in a 
# line. 
# 
#  
#  Example 1: 
# 
#  
# Input: sentence = ["hello","world"], rows = 2, cols = 8
# Output: 1
# Explanation:
# hello---
# world---
# The character '-' signifies an empty space on the screen.
#  
# 
#  Example 2: 
# 
#  
# Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
# Output: 2
# Explanation:
# a-bcd- 
# e-a---
# bcd-e-
# The character '-' signifies an empty space on the screen.
#  
# 
#  Example 3: 
# 
#  
# Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
# Output: 1
# Explanation:
# i-had
# apple
# pie-i
# had--
# The character '-' signifies an empty space on the screen.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= sentence.length <= 100 
#  1 <= sentence[i].length <= 10 
#  sentence[i] consists of lowercase English letters. 
#  1 <= rows, cols <= 2 * 10⁴ 
#  
# 
#  Related Topics String Dynamic Programming Simulation 👍 959 👎 489


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        all_len = sum(map(len, sentence)) + n
        sentence = " ".join(sentence) + " "
        start = 0
        for i in range(rows):
            start += cols
            if sentence[start % all_len] == " ":
                start += 1
            else:
                while start > 0 and sentence[(start - 1) % all_len] != " ":
                    start -= 1
        return start // all_len
# leetcode submit region end(Prohibit modification and deletion)
