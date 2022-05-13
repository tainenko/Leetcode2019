# Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' 
# or empty '0', return the maximum enemies you can kill using one bomb. You can 
# only place the bomb in an empty cell. 
# 
#  The bomb kills all the enemies in the same row and column from the planted 
# point until it hits the wall since it is too strong to be destroyed. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] is either 'W', 'E', or '0'. 
#  
#  Related Topics Array Dynamic Programming Matrix 👍 780 👎 94


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    self.bfs(i, j, grid)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].isdigit():
                    res = max(int(grid[i][j]), res)
        return res

    def bfs(self, i, j, grid):
        for x in range(i, -1, -1):
            if grid[x][j] == 'W':
                break
            if grid[x][j].isdigit():
                grid[x][j] = str(int(grid[x][j]) + 1)
        for x in range(i + 1, len(grid)):
            if grid[x][j] == 'W':
                break
            if grid[x][j].isdigit():
                grid[x][j] = str(int(grid[x][j]) + 1)
        for y in range(j, -1, -1):
            if grid[i][y] == 'W':
                break
            if grid[i][y].isdigit():
                grid[i][y] = str(int(grid[i][y]) + 1)
        for y in range(j + 1, len(grid[0])):
            if grid[i][y] == 'W':
                break
            if grid[i][y].isdigit():
                grid[i][y] = str(int(grid[i][y]) + 1)
# leetcode submit region end(Prohibit modification and deletion)
