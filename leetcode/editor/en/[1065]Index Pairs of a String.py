# Given a string text and an array of strings words, return an array of all 
# index pairs [i, j] so that the substring text[i...j] is in words. 
# 
#  Return the pairs [i, j] in sorted order (i.e., sort them by their first 
# coordinate, and in case of ties sort them by their second coordinate). 
# 
#  
#  Example 1: 
# 
#  
# Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# Output: [[3,7],[9,13],[10,17]]
#  
# 
#  Example 2: 
# 
#  
# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]
# Explanation: Notice that matches can overlap, see "aba" is found in [0,2] and 
# [2,4].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 100 
#  1 <= words.length <= 20 
#  1 <= words[i].length <= 50 
#  text and words[i] consist of lowercase English letters. 
#  All the strings of words are unique. 
#  
#  Related Topics Array String Trie Sorting 👍 203 👎 73


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        words.sort(key=lambda x: len(x))
        for i in range(len(text)):
            for word in words:
                if i + len(word) > len(text):
                    continue
                if word == text[i:i + len(word)]:
                    res.append([i, i + len(word) - 1])
        return res

# leetcode submit region end(Prohibit modification and deletion)
