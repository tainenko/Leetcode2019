# You are given an array words of size n consisting of non-empty strings. 
# 
#  We define the score of a string word as the number of strings words[i] such 
# that word is a prefix of words[i]. 
# 
#  
#  For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 
# 2, since "ab" is a prefix of both "ab" and "abc". 
#  
# 
#  Return an array answer of size n where answer[i] is the sum of scores of 
# every non-empty prefix of words[i]. 
# 
#  Note that a string is considered as a prefix of itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abc","ab","bc","b"]
# Output: [5,4,3,2]
# Explanation: The answer for each string is the following:
# - "abc" has 3 prefixes: "a", "ab", and "abc".
# - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", 
# and 1 string with the prefix "abc".
# The total is answer[0] = 2 + 2 + 1 = 5.
# - "ab" has 2 prefixes: "a" and "ab".
# - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
# 
# The total is answer[1] = 2 + 2 = 4.
# - "bc" has 2 prefixes: "b" and "bc".
# - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
# The total is answer[2] = 2 + 1 = 3.
# - "b" has 1 prefix: "b".
# - There are 2 strings with the prefix "b".
# The total is answer[3] = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["abcd"]
# Output: [4]
# Explanation:
# "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
# Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array String Trie Counting 👍 612 👎 48


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0

    def insert(self, w):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.cnt += 1

    def search(self, w):
        res = 0
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return res
            node = node.children[idx]
            res += node.cnt
        return res


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.search(word) for word in words]

# leetcode submit region end(Prohibit modification and deletion)
