# Given an m x n integer matrix grid, return the maximum score of a path 
# starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions. 
# 
#  The score of a path is the minimum value in that path. 
# 
#  
#  For example, the score of the path 8 → 4 → 5 → 9 is 4. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
# Output: 4
# Explanation: The path with the maximum score is highlighted in yellow. 
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
# Output: 2
#  
# 
#  Example 3: 
#  
#  
# Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,
# 6,5,4,3]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 100 
#  0 <= grid[i][j] <= 10⁹ 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find Heap 
# (Priority Queue) Matrix 👍 1254 👎 122
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap = []
        res = float('inf')
        visited = set()
        m, n = len(grid), len(grid[0])
        heapq.heappush(heap, (-grid[0][0], 0, 0))
        while heap:
            val, i, j = heapq.heappop(heap)
            res = min(res, -val)
            if i == m - 1 and j == n - 1:
                return res
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(heap, (-grid[x][y], x, y))

# leetcode submit region end(Prohibit modification and deletion)
