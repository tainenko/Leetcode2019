# Given an array of strings words, return the first palindromic string in the 
# array. If there is no such string, return an empty string "". 
# 
#  A string is palindromic if it reads the same forward and backward. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is 
# returned.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 100 
#  words[i] consists only of lowercase English letters. 
#  
#  Related Topics Array Two Pointers String 👍 186 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindromic(word):
                return word

        return ""

    def is_palindromic(self, word):
        left = 0
        right = len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
