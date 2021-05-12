# In English, we have a concept called root, which can be followed by some other
#  word to form another longer word - let's call this word successor. For example,
#  when the root "an" is followed by the successor word "other", we can form a new
#  word "another". 
# 
#  Given a dictionary consisting of many roots and a sentence consisting of word
# s separated by spaces, replace all the successors in the sentence with the root 
# forming it. If a successor can be replaced by more than one root, replace it wit
# h the root that has the shortest length. 
# 
#  Return the sentence after the replacement. 
# 
#  
#  Example 1: 
#  Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled b
# y the battery"
# Output: "the cat was rat by the bat"
#  Example 2: 
#  Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
#  Example 3: 
#  Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa a
# aa aaa aaaaaa bbb baba ababa"
# Output: "a a a a a a a a bbb baba a"
#  Example 4: 
#  Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was ra
# ttled by the battery"
# Output: "the cat was rat by the bat"
#  Example 5: 
#  Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solutio
# n is accepted"
# Output: "it is ab that this solution is ac"
#  
#  
#  Constraints: 
# 
#  
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 100 
#  dictionary[i] consists of only lower-case letters. 
#  1 <= sentence.length <= 10^6 
#  sentence consists of only lower-case letters and spaces. 
#  The number of words in sentence is in the range [1, 1000] 
#  The length of each word in sentence is in the range [1, 1000] 
#  Each two consecutive words in sentence will be separated by exactly one space
# . 
#  sentence does not have leading or trailing spaces. 
#  
#  Related Topics Hash Table Trie 
#  👍 1000 👎 145


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = self.build_trie(dictionary)
        words = sentence.split(" ")
        res = []
        for word in words:
            tmp = self.search(trie, word)
            if tmp:
                res.append(tmp)
            else:
                res.append(word)
        return " ".join(res)

    def build_trie(self, dictionary):
        trie = {}
        for letter in dictionary:
            tmp = trie
            for char in letter:
                if char not in tmp.keys():
                    tmp[char] = {}
                tmp = tmp[char]
            tmp["$"] = True
        return trie

    def search(self, trie, word):
        res = ""
        for char in word:
            if trie.get("$"):
                return res
            elif char not in trie.keys():
                return ""
            else:
                res += char
                trie = trie[char]
        return res if trie.get("$") else ""
# leetcode submit region end(Prohibit modification and deletion)
