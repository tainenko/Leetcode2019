# Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4
# -directionally connected group of 0s and a closed island is an island totally (
# all left, top, right, bottom) surrounded by 1s. 
# 
#  Return the number of closed islands. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,
# 0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (
# group of 1s). 
# 
#  Example 2: 
# 
#  
# 
#  
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 4355 👎 149


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 0:
                return
            grid[x][y] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

        m = len(grid)
        n = len(grid[0])
        for i in [0, m - 1]:
            for j in range(n):
                dfs(i, j)

        for i in range(m):
            for j in [0, n - 1]:
                dfs(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res

# leetcode submit region end(Prohibit modification and deletion)
