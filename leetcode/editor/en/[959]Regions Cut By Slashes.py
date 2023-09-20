# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists 
# of a '/', '\', or blank space ' '. These characters divide the square into 
# contiguous regions. 
# 
#  Given the grid grid represented as a string array, return the number of 
# regions. 
# 
#  Note that backslash characters are escaped, so a '\' is represented as '\\'. 
# 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [" /","/ "]
# Output: 2
#  
# 
#  Example 2: 
#  
#  
# Input: grid = [" /","  "]
# Output: 1
#  
# 
#  Example 3: 
#  
#  
# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/,
#  and "/\\" refers to /\.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == grid.length == grid[i].length 
#  1 <= n <= 30 
#  grid[i][j] is either '/', '\', or ' '. 
#  
# 
#  Related Topics Array Hash Table Depth-First Search Breadth-First Search 
# Union Find Matrix 👍 2941 👎 553


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            fa, fb = find(a), find(b)
            if fa != fb:
                p[fa] = fb
                nonlocal size
                size -= 1

        n = len(grid)
        size = n * n * 4
        p = list(range(size))
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                k = i * n + j
                if i < n - 1:
                    union(4 * k + 2, (k + n) * 4)
                if j < n - 1:
                    union(4 * k + 1, (k + 1) * 4 + 3)
                if v == '/':
                    union(4 * k, 4 * k + 3)
                    union(4 * k + 1, 4 * k + 2)
                elif v == '\\':
                    union(4 * k, 4 * k + 1)
                    union(4 * k + 2, 4 * k + 3)
                else:
                    union(4 * k, 4 * k + 1)
                    union(4 * k + 1, 4 * k + 2)
                    union(4 * k + 2, 4 * k + 3)
        return size
# leetcode submit region end(Prohibit modification and deletion)
