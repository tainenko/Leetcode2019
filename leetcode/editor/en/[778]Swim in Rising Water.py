# You are given an n x n integer matrix grid where each value grid[i][j] 
# represents the elevation at that point (i, j). 
# 
#  The rain starts to fall. At time t, the depth of the water everywhere is t. 
# You can swim from a square to another 4-directionally adjacent square if and 
# only if the elevation of both squares individually are at most t. You can swim 
# infinite distances in zero time. Of course, you must stay within the boundaries of 
# the grid during your swim. 
# 
#  Return the least time until you can reach the bottom right square (n - 1, n -
#  1) if you start at the top left square (0, 0). 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a 
# higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[
# 10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 50 
#  0 <= grid[i][j] < n² 
#  Each value grid[i][j] is unique. 
#  
# 
#  Related Topics Array Binary Search Depth-First Search Breadth-First Search 
# Union Find Heap (Priority Queue) Matrix 👍 2941 👎 187


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        while pq:
            w, i, j = heapq.heappop(pq)
            visited.add((i, j))
            res = max(w, res)
            if i == m - 1 and j == n - 1:
                return res
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if x < 0 or x == m or y < 0 or y == n or (x, y) in visited:
                    continue
                heapq.heappush(pq, (grid[i + dx][j + dy], i + dx, j + dy))
        return res
    # leetcode submit region end(Prohibit modification and deletion)
