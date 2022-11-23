# Given a string s and an array of strings words, return the number of words[i] 
# that is a subsequence of s. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order 
# of the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: 
# "a", "acd", "ace".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 50 
#  s and words[i] consist of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Trie Sorting 👍 4818 👎 202


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(word[1:])
        cnt = 0
        for c in s:
            tmp = waiting[c]
            waiting[c] = []
            for word in tmp:
                if not word:
                    cnt += 1
                    continue
                waiting[word[0]].append(word[1:])
        return cnt

# leetcode submit region end(Prohibit modification and deletion)
