# Given an m x n integers matrix, return the length of the longest increasing 
# path in matrix. 
# 
#  From each cell, you can either move in four directions: left, right, up, or 
# down. You may not move diagonally or move outside the boundary (i.e., wrap-
# around is not allowed). 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally 
# is not allowed.
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [[1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 200 
#  0 <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  Related Topics Array Dynamic Programming Depth-First Search Breadth-First 
# Search Graph Topological Sort Memoization Matrix 👍 7908 👎 118


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[float("-inf")] * n for _ in range(m)]

        def helper(i, j, prev):
            if i < 0 or i == m or j < 0 or j == n or matrix[i][j] <= prev:
                return 0
            if dp[i][j] != float("-inf"):
                return dp[i][j]
            val = matrix[i][j]
            dp[i][j] = 1 + max(helper(i - 1, j, val), helper(i + 1, j, val), helper(i, j - 1, val),
                               helper(i, j + 1, val))
            return dp[i][j]

        return max([helper(i, j, float("-inf")) for i in range(m) for j in range(n)])

# leetcode submit region end(Prohibit modification and deletion)
