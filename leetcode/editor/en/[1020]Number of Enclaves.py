# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1
#  represents a land cell. 
# 
#  A move consists of walking from one land cell to another adjacent (4-
# directionally) land cell or walking off the boundary of the grid. 
# 
#  Return the number of land cells in grid for which we cannot walk off the 
# boundary of the grid in any number of moves. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is 
# not enclosed because its on the boundary.
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 3713 👎 70


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy)

        m = len(grid)
        n = len(grid[0])
        for i in [0, m - 1]:
            for j in range(n):
                dfs(i, j)
        for j in [0, n - 1]:
            for i in range(m):
                dfs(i, j)

        return sum(v for row in grid for v in row)

# leetcode submit region end(Prohibit modification and deletion)
