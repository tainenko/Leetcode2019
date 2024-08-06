# You are given a n x n 2D array grid containing distinct elements in the range 
# [0, n² - 1]. 
# 
#  Implement the neighborSum class: 
# 
#  
#  neighborSum(int [][]grid) initializes the object. 
#  int adjacentSum(int value) returns the sum of elements which are adjacent 
# neighbors of value, that is either to the top, left, right, or bottom of value in 
# grid. 
#  int diagonalSum(int value) returns the sum of elements which are diagonal 
# neighbors of value, that is either to the top-left, top-right, bottom-left, or 
# bottom-right of value in grid. 
#  
# 
#  
# 
#  
#  Example 1: 
# 
#  
#  Input: 
#  
# 
#  ["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"] 
# 
#  [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]] 
# 
#  Output: [null, 6, 16, 16, 4] 
# 
#  Explanation: 
# 
#  
# 
#  
#  The adjacent neighbors of 1 are 0, 2, and 4. 
#  The adjacent neighbors of 4 are 1, 3, 5, and 7. 
#  The diagonal neighbors of 4 are 0, 2, 6, and 8. 
#  The diagonal neighbor of 8 is 4. 
#  
# 
#  Example 2: 
# 
#  
#  Input: 
#  
# 
#  ["neighborSum", "adjacentSum", "diagonalSum"] 
# 
#  [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]
#  
# 
#  Output: [null, 23, 45] 
# 
#  Explanation: 
# 
#  
# 
#  
#  The adjacent neighbors of 15 are 0, 10, 7, and 6. 
#  The diagonal neighbors of 9 are 4, 12, 14, and 15. 
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= n == grid.length == grid[0].length <= 10 
#  0 <= grid[i][j] <= n² - 1 
#  All grid[i][j] are distinct. 
#  value in adjacentSum and diagonalSum will be in the range [0, n² - 1]. 
#  At most 2 * n² calls will be made to adjacentSum and diagonalSum. 
#  
# 
#  Related Topics Array Hash Table Design Matrix Simulation 👍 46 👎 5
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.m = len(grid)
        self.n = len(grid[0])
        self.adjacent = defaultdict(int)
        self.diagonal = defaultdict(int)
        for i in range(self.m):
            for j in range(self.n):
                val = grid[i][j]
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if i + x < 0 or i + x >= self.m or j + y < 0 or j + y >= self.n:
                        continue
                    self.adjacent[val] += grid[i + x][j + y]
                for x, y in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    if i + x < 0 or i + x >= self.m or j + y < 0 or j + y >= self.n:
                        continue
                    self.diagonal[val] += grid[i + x][j + y]

    def adjacentSum(self, value: int) -> int:
        return self.adjacent[value]

    def diagonalSum(self, value: int) -> int:
        return self.diagonal[value]
# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# leetcode submit region end(Prohibit modification and deletion)
