# You are starving and you want to eat food as quickly as possible. You want to 
# find the shortest path to arrive at any food cell. 
# 
#  You are given an m x n character matrix, grid, of these different types of 
# cells: 
# 
#  
#  '*' is your location. There is exactly one '*' cell. 
#  '#' is a food cell. There may be multiple food cells. 
#  'O' is free space, and you can travel through these cells. 
#  'X' is an obstacle, and you cannot travel through these cells. 
#  
# 
#  You can travel to any adjacent cell north, east, south, or west of your 
# current location if there is not an obstacle. 
# 
#  Return the length of the shortest path for you to reach any food cell. If 
# there is no path for you to reach food, return -1. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O",
# "O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#",
# "X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
#  
# 
#  Example 3: 
#  
#  
# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O",
# "X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X",
# "X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach 
# the bottom food. 
# 
#  Example 4: 
# 
#  
# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O",
# "X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["O",
# "O","O","O","O","O","O","O"]]
# Output: 5 
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  grid[row][col] is '*', 'X', 'O', or '#'. 
#  The grid contains exactly one '*'. 
#  
# 
#  Related Topics Array Breadth-First Search Matrix 👍 710 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i, j))
                    visited.add((i, j))
        step = 0
        while q:
            step += 1
            nxt = []
            for x, y in q:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if not (0 <= x + dx < m and 0 <= y + dy < n):
                        continue

                    if (x + dx, y + dy) in visited:
                        continue
                    if grid[x + dx][y + dy] == "X":
                        continue
                    elif grid[x + dx][y + dy] == "#":
                        return step
                    elif grid[x + dx][y + dy] == "O":
                        nxt.append((x + dx, y + dy))
                        visited.add((x + dx, y + dy))
            q = nxt

        return -1
# leetcode submit region end(Prohibit modification and deletion)
