# Given an m x n binary matrix mat, return the length of the longest line of 
# consecutive one in the matrix. 
# 
#  The line could be horizontal, vertical, diagonal, or anti-diagonal. 
# 
#  
#  Example 1: 
#  
#  
# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
#  
# 
#  Example 2: 
#  
#  
# Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  mat[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Dynamic Programming Matrix 👍 768 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                dp[i][j] = [1, 1, 1, 1]
                if i > 0:
                    dp[i][j][0] += dp[i - 1][j][0]
                if j > 0:
                    dp[i][j][1] += dp[i][j - 1][1]
                if i > 0 and j > 0:
                    dp[i][j][2] += dp[i - 1][j - 1][2]
                if i > 0 and j < n - 1:
                    dp[i][j][3] += dp[i - 1][j + 1][3]
                res = max(res, *dp[i][j])
        return res

# leetcode submit region end(Prohibit modification and deletion)
