# Given a square matrix mat, return the sum of the matrix diagonals. 
# 
#  Only include the sum of all the elements on the primary diagonal and all the 
# elements on the secondary diagonal that are not part of the primary diagonal. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
#  
# 
#  Example 3: 
# 
#  
# Input: mat = [[5]]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  n == mat.length == mat[i].length 
#  1 <= n <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics Array Matrix 👍 992 👎 20


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        m = len(mat[0])
        for i, j in zip(range(n), range(m)):
            total += mat[i][j]
        for i, j in zip(range(n - 1, -1, -1), range(m)):
            total += mat[i][j]
        if n == m and n % 2 == 1:
            total -= mat[n // 2][m // 2]
        return total
# leetcode submit region end(Prohibit modification and deletion)
