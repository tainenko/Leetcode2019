# Design a data structure that is initialized with a list of different words. 
# Provided a string, you should determine if you can change exactly one character 
# in this string to match any word in the data structure. 
# 
#  Implement the MagicDictionary class: 
# 
#  
#  MagicDictionary() Initializes the object. 
#  void buildDict(String[] dictionary) Sets the data structure with an array of 
# distinct strings dictionary. 
#  bool search(String searchWord) Returns true if you can change exactly one 
# character in searchWord to match any string in the data structure, otherwise 
# returns false. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]
# 
# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to 
# match "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= dictionary.length <= 100 
#  1 <= dictionary[i].length <= 100 
#  dictionary[i] consists of only lower-case English letters. 
#  All the strings in dictionary are distinct. 
#  1 <= searchWord.length <= 100 
#  searchWord consists of only lower-case English letters. 
#  buildDict will be called only once before search. 
#  At most 100 calls will be made to search. 
#  
# 
#  Related Topics Hash Table String Depth-First Search Design Trie 👍 1429 👎 21
# 2


# leetcode submit region begin(Prohibit modification and deletion)
class MagicDictionary:

    def __init__(self):
        self.trie = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.build(word)

    def build(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = dict()
            node = node[c]
        node['#'] = '#'

    def search(self, searchWord: str) -> bool:
        def dfs(word, i, node, modified):
            if i == len(word):
                return '#' in node and modified

            if word[i] in node and dfs(word, i + 1, node[word[i]], modified):
                return True

            elif modified:
                return False

            else:
                for letter in node:
                    if letter == '#' or letter == word[i]:
                        continue
                    if dfs(word, i + 1, node[letter], True):
                        return True
                return False

        return dfs(searchWord, 0, self.trie, False)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# leetcode submit region end(Prohibit modification and deletion)
