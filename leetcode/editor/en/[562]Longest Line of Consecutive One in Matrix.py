# Given an m x n binary matrix mat, return the length of the longest line of 
# consecutive one in the matrix. 
# 
#  The line could be horizontal, vertical, diagonal, or anti-diagonal. 
# 
#  
#  Example 1: 
#  
#  
# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
#  
# 
#  Example 2: 
#  
#  
# Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  mat[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Dynamic Programming Matrix 👍 768 👎 103


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
