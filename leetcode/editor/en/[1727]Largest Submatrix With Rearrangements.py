# You are given a binary matrix matrix of size m x n, and you are allowed to 
# rearrange the columns of the matrix in any order. 
# 
#  Return the area of the largest submatrix within matrix where every element 
# of the submatrix is 1 after reordering the columns optimally. 
# 
#  
#  Example 1: 
#  
#  
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
#  
# 
#  Example 2: 
#  
#  
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no 
# way to make a submatrix of 1s larger than an area of 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m * n <= 10⁵ 
#  matrix[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Greedy Sorting Matrix 👍 1953 👎 104


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    matrix[i][j] = matrix[i - 1][j] + 1
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for j, v in enumerate(row, 1):
                ans = max(ans, j * v)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
