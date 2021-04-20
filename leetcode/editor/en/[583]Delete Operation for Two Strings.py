# Given two strings word1 and word2, return the minimum number of steps required
#  to make word1 and word2 the same. 
# 
#  In one step, you can delete exactly one character in either string. 
# 
#  
#  Example 1: 
# 
#  
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make 
# "eat" to "ea".
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word1.length, word2.length <= 500 
#  word1 and word2 consist of only lowercase English letters. 
#  
#  Related Topics String 
#  👍 1477 👎 37


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
