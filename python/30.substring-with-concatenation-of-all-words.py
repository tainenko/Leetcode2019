#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (25.00%)
# Likes:    973
# Dislikes: 1305
# Total Accepted:    185.5K
# Total Submissions: 724.2K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
# 
# 
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_map = {}
        for word in words:
            words_map[word] = words_map.get(word, 0) + 1
        word_len = len(words)
        word_size = len(words[0])
        res = []
        for i in range(len(s) - word_len * word_size + 1):
            j = 0
            word_cnts = {}
            while j < word_len:
                word = s[i + word_size * j:i + word_size * j + word_size]
                if word not in words_map:
                    break
                word_cnts[word] = word_cnts.get(word, 0) + 1
                if word_cnts[word] > words_map[word]:
                    break
                j += 1
            if j == word_len:
                res.append(i)
        return res

# @lc code=end
