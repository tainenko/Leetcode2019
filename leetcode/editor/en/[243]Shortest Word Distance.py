# Given an array of strings wordsDict and two different strings that already 
# exist in the array word1 and word2, return the shortest distance between these two 
# words in the list. 
# 
#  
#  Example 1: 
# 
#  
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 
# = "coding", word2 = "practice"
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 
# = "makes", word2 = "coding"
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= wordsDict.length <= 3 * 10⁴ 
#  1 <= wordsDict[i].length <= 10 
#  wordsDict[i] consists of lowercase English letters. 
#  word1 and word2 are in wordsDict. 
#  word1 != word2 
#  
#  Related Topics Array String 👍 876 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = [i for i, val in enumerate(wordsDict) if val == word1]
        idx2 = [i for i, val in enumerate(wordsDict) if val == word2]
        return min(abs(i - j) for i in idx1 for j in idx2)

# leetcode submit region end(Prohibit modification and deletion)
