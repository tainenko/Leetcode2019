# You are given a 2D boolean matrix grid. 
# 
#  A collection of 3 elements of grid is a right triangle if one of its 
# elements is in the same row with another element and in the same column with the third 
# element. The 3 elements may not be next to each other. 
# 
#  Return an integer that is the number of right triangles that can be made 
# with 3 elements of grid such that all of them have a value of 1. 
# 
#  
#  Example 1: 
# 
#  
#  
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  0 
#  1 
#  1 
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  
#  
# 
#  
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  0 
#  1 
#  1 
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  
# 
#  
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  0 
#  1 
#  1 
#  
#  
#  0 
#  1 
#  0 
#  
#  
#  
# 
#  
#  Input: grid = [[0,1,0],[0,1,1],[0,1,0]] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  There are two right triangles with elements of the value 1. Notice that the 
# blue ones do not form a right triangle because the 3 elements are in the same 
# column. 
# 
#  Example 2: 
# 
#  
#  
#  
#  
#  1 
#  0 
#  0 
#  0 
#  
#  
#  0 
#  1 
#  0 
#  1 
#  
#  
#  1 
#  0 
#  0 
#  0 
#  
#  
#  
#  
# 
#  
#  Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]] 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  There are no right triangles with elements of the value 1. Notice that the 
# blue ones do not form a right triangle. 
# 
#  Example 3: 
# 
#  
#  
#  
#  
#  1 
#  0 
#  1 
#  
#  
#  1 
#  0 
#  0 
#  
#  
#  1 
#  0 
#  0 
#  
#  
#  
#  
# 
#  
#  
#  
#  1 
#  0 
#  1 
#  
#  
#  1 
#  0 
#  0 
#  
#  
#  1 
#  0 
#  0 
#  
#  
#  
# 
#  
#  Input: grid = [[1,0,1],[1,0,0],[1,0,0]] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  There are two right triangles with elements of the value 1. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= grid.length <= 1000 
#  1 <= grid[i].length <= 1000 
#  0 <= grid[i][j] <= 1 
#  
# 
#  Related Topics Array Hash Table Math Combinatorics Counting 👍 119 👎 22


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                res += (rows[i] - 1) * (cols[j] - 1)
        return res

# leetcode submit region end(Prohibit modification and deletion)
