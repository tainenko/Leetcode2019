# You are given an m x n integer matrix grid where each cell is either 0 (empty)
#  or 1 (obstacle). You can move up, down, left, or right from and to an empty 
# cell in one step. 
# 
#  Return the minimum number of steps to walk from the upper left corner (0, 0) 
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most k 
# obstacles. If it is not possible to find such walk return -1. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such 
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 40 
#  1 <= k <= m * n 
#  grid[i][j] is either 0 or 1. 
#  grid[0][0] == grid[m - 1][n - 1] == 0 
#  
# 
#  Related Topics Array Breadth-First Search Matrix 👍 4304 👎 76
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if k >= m + n - 3:
            return m + n - 2
        q = deque([(0, 0, k)])
        vis = {(0, 0, k)}
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                x, y, k = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue
                    if (new_x, new_y) == (m - 1, n - 1):
                        return res
                    if grid[new_x][new_y] == 0 and (new_x, new_y, k) not in vis:
                        q.append((new_x, new_y, k))
                        vis.add((new_x, new_y, k))
                    if grid[new_x][new_y] == 1 and k > 0 and (new_x, new_y, k - 1) not in vis:
                        q.append((new_x, new_y, k - 1))
                        vis.add((new_x, new_y, k - 1))
        return -1
# leetcode submit region end(Prohibit modification and deletion)
