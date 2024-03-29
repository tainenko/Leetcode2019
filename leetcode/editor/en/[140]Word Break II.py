# Given a string s and a dictionary of strings wordDict, add spaces in s to 
# construct a sentence where each word is a valid dictionary word. Return all such 
# possible sentences in any order. 
# 
#  Note that the same word in the dictionary may be reused multiple times in 
# the segmentation. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine",
# "pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  1 <= wordDict.length <= 1000 
#  1 <= wordDict[i].length <= 10 
#  s and wordDict[i] consist of only lowercase English letters. 
#  All the strings of wordDict are unique. 
#  
# 
#  Related Topics Hash Table String Dynamic Programming Backtracking Trie 
# Memoization 👍 5526 👎 492


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = dict()
        return self.dfs(s, memo, wordDict)

    def dfs(self, s, memo, wordDict):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for r in self.dfs(s[len(word):], memo, wordDict):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res

# leetcode submit region end(Prohibit modification and deletion)
