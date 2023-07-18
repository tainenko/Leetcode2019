# You are given an m x n integer array grid where grid[i][j] could be: 
# 
#  
#  1 representing the starting square. There is exactly one starting square. 
#  2 representing the ending square. There is exactly one ending square. 
#  0 representing empty squares we can walk over. 
#  -1 representing obstacles that we cannot walk over. 
#  
# 
#  Return the number of 4-directional walks from the starting square to the 
# ending square, that walk over every non-obstacle square exactly once. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#  
# 
#  Example 3: 
#  
#  
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# 
# Note that the starting and ending square can be anywhere in the grid.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 20 
#  1 <= m * n <= 20 
#  -1 <= grid[i][j] <= 2 
#  There is exactly one starting cell and one ending cell. 
#  
# 
#  Related Topics Array Backtracking Bit Manipulation Matrix 👍 4690 👎 175


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty = 0
        x, y = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = i
                    y = j
                elif grid[i][j] == 0:
                    empty += 1
        return self.dfs(grid, len(grid), len(grid[0]), x, y, empty)

    def dfs(self, grid, m, n, x, y, empty):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 0
        if grid[x][y] == -1:
            return 0
        if grid[x][y] == 2:
            if empty == -1:
                return 1
            return 0
        grid[x][y] = -1
        empty -= 1
        count = self.dfs(
            grid, m, n, x + 1, y, empty
        ) + self.dfs(
            grid, m, n, x - 1, y, empty
        ) + self.dfs(
            grid, m, n, x,
            y + 1, empty
        ) + self.dfs(
            grid, m, n, x, y - 1, empty
        )
        grid[x][y] = 0
        return count
    # leetcode submit region end(Prohibit modification and deletion)
