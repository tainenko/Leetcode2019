# Given an array of strings wordsDict and two strings that already exist in the 
# array word1 and word2, return the shortest distance between these two words in 
# the list. 
# 
#  Note that word1 and word2 may be the same. It is guaranteed that they 
# represent two individual words in the list. 
# 
#  
#  Example 1: 
#  Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1
#  = "makes", word2 = "coding"
# Output: 1
#  
#  Example 2: 
#  Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1
#  = "makes", word2 = "makes"
# Output: 3
#  
#  
#  Constraints: 
# 
#  
#  1 <= wordsDict.length <= 10⁵ 
#  1 <= wordsDict[i].length <= 10 
#  wordsDict[i] consists of lowercase English letters. 
#  word1 and word2 are in wordsDict. 
#  
# 
#  Related Topics Array String 👍 384 👎 91


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = -1
        res = len(wordsDict)
        if word1 != word2:
            for idx, word in enumerate(wordsDict):
                if word == word1:
                    pos1 = idx
                elif word == word2:
                    pos2 = idx
                if pos1 != -1 and pos2 != -1:
                    res = min(res, abs(pos1 - pos2))
        else:
            for idx, word in enumerate(wordsDict):
                if word == word1:
                    if pos1 != -1:
                        res = min(res, abs(pos1 - idx))
                    pos1 = idx
        return res
# leetcode submit region end(Prohibit modification and deletion)
