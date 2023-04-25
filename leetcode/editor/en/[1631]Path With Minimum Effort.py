# You are a hiker preparing for an upcoming hike. You are given heights, a 2D 
# array of size rows x columns, where heights[row][col] represents the height of 
# cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to 
# travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can 
# move up, down, left, or right, and you wish to find a route that requires the 
# minimum effort. 
# 
#  A route's effort is the maximum absolute difference in heights between two 
# consecutive cells of the route. 
# 
#  Return the minimum effort required to travel from the top-left cell to the 
# bottom-right cell. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 
# in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute 
# difference is 3.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 
# in consecutive cells, which is better than route [1,3,5,3,5].
#  
# 
#  Example 3: 
#  
#  
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 
# Output: 0
# Explanation: This route does not require any effort.
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == heights.length 
#  columns == heights[i].length 
#  1 <= rows, columns <= 100 
#  1 <= heights[i][j] <= 10⁶ 
#  
# 
#  Related Topics Array Binary Search Depth-First Search Breadth-First Search 
# Union Find Heap (Priority Queue) Matrix 👍 4206 👎 156


# leetcode submit region begin(Prohibit modification and deletion)
class DSU:
    def __init__(self):
        self.par = list(range(10001))

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dsu = DSU()
        edges = []
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                pos = n * i + j
                if i < m - 1:
                    edges.append((abs(heights[i + 1][j] - heights[i][j]), pos, pos + n))
                if j < n - 1:
                    edges.append((abs(heights[i][j + 1] - heights[i][j]), pos, pos + 1))
        edges.sort()
        for edge in edges:
            dsu.union(edge[1], edge[2])
            if dsu.connected(0, m * n - 1):
                return edge[0]
        return 0
# leetcode submit region end(Prohibit modification and deletion)
