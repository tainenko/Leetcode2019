#
# @lc app=leetcode id=211 lang=python
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (31.31%)
# Likes:    1313
# Dislikes: 72
# Total Accepted:    152.4K
# Total Submissions: 448.1K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
'[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'


#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

# @lc code=start
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.root
        for letter in word:
            if letter not in p:
                p[letter] = {}
            p = p[letter]
        p['#'] = {}

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        p = [self.root]
        for letter in word:
            next = []
            if letter == '.':
                for node in p:
                    next += node.values()
            else:
                for node in p:
                    if letter in node:
                        next.append(node[letter])
            if not next:
                return False
            p = next
        return any(['#' in x for x in p])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
