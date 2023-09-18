# You are given an n x n binary matrix grid where 1 represents land and 0 
# represents water. 
# 
#  An island is a 4-directionally connected group of 1's not connected to any 
# other 1's. There are exactly two islands in grid. 
# 
#  You may change 0's to 1's to connect the two islands to form one island. 
# 
#  Return the smallest number of 0's you must flip to connect the two islands. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[0,1],[1,0]]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == grid.length == grid[i].length 
#  2 <= n <= 100 
#  grid[i][j] is either 0 or 1. 
#  There are exactly two islands in grid. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Matrix 👍 5067 ?
# ? 186


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = y = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x = i
                    y = j
                    break
        island1 = [(x, y)]
        vis = set(island1)
        q = [(x, y)]
        while q:
            next_ = []
            for x, y in q:
                grid[x][y] = 2
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] == 0 or (
                    new_x, new_y) in vis:
                        continue
                    next_.append((new_x, new_y))
                    vis.add((new_x, new_y))
            island1.extend(next_)
            q = next_

        q = island1
        res = 0
        while q:
            next_ = []
            for x, y in q:
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or (new_x, new_y) in vis:
                        continue
                    if grid[new_x][new_y] == 1:
                        return res
                    vis.add((new_x, new_y))
                    next_.append((new_x, new_y))
            q = next_
            res += 1
# leetcode submit region end(Prohibit modification and deletion)
