#
# @lc app=leetcode id=318 lang=python
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (48.99%)
# Likes:    640
# Dislikes: 52
# Total Accepted:    87.2K
# Total Submissions: 175.8K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
# 
#

# @lc code=start
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask = [0] * len(words)
        res = 0
        for i in range(len(words)):
            for c in words[i]:
                mask[i] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not mask[i] & mask[j]:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# @lc code=end
