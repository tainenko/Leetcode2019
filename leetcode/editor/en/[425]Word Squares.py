# Given an array of unique strings words, return all the word squares you can 
# build from words. The same word from words can be used multiple times. You can 
# return the answer in any order. 
# 
#  A sequence of strings forms a valid word square if the kᵗʰ row and column 
# read the same string, where 0 <= k < max(numRows, numColumns). 
# 
#  
#  For example, the word sequence ["ball","area","lead","lady"] forms a word 
# square because each word reads the same both horizontally and vertically. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["area","lead","wall","lady","ball"]
# Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (
# just the order of words in each word square matters).
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["abat","baba","atan","atal"]
# Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (
# just the order of words in each word square matters).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 4 
#  All words[i] have the same length. 
#  words[i] consists of only lowercase English letters. 
#  All words[i] are unique. 
#  
# 
#  Related Topics Array String Backtracking Trie 👍 1064 👎 69


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.v = []

    def insert(self, w, i):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.v.append(i)

    def search(self, w):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return []
            node = node.children[idx]
        return node.v


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def dfs(letters):
            if len(letters) == len(words[0]):
                res.append(letters[:])
                return
            idxes = trie.search("".join([letters[i][len(letters)] for i in range(len(letters))]))
            for idx in idxes:
                letters.append(words[idx])
                dfs(letters)
                letters.pop()

        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, i)

        res = []
        for word in words:
            dfs([word])
        return res
# leetcode submit region end(Prohibit modification and deletion)
