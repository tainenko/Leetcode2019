# Design a data structure that will be initialized with a string array, and 
# then it should answer queries of the shortest distance between two different 
# strings from the array. 
# 
#  Implement the WordDistance class: 
# 
#  
#  WordDistance(String[] wordsDict) initializes the object with the strings 
# array wordsDict. 
#  int shortest(String word1, String word2) returns the shortest distance 
# between word1 and word2 in the array wordsDict. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["WordDistance", "shortest", "shortest"]
# [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"]
# , ["makes", "coding"]]
# Output
# [null, 3, 1]
# 
# Explanation
# WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", 
# "coding", "makes"]);
# wordDistance.shortest("coding", "practice"); // return 3
# wordDistance.shortest("makes", "coding");    // return 1
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
#  At most 5000 calls will be made to shortest. 
#  
#  Related Topics Array Hash Table Two Pointers String Design 👍 733 👎 212


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.m = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.m[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        res = float('inf')
        while i < len(self.m[word1]) and j < len(self.m[word2]):
            res = min(res, abs(self.m[word1][i] - self.m[word2][j]))
            if self.m[word1][i] < self.m[word2][j]:
                i += 1
            else:
                j += 1
        return res
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
# leetcode submit region end(Prohibit modification and deletion)
