# An n x n matrix is valid if every row and every column contains all the 
# integers from 1 to n (inclusive). 
# 
#  Given an n x n integer matrix matrix, return true if the matrix is valid. 
# Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the 
# numbers 1, 2, and 3.
# Hence, we return true.
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do 
# not contain the numbers 2 or 3.
# Hence, we return false.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == matrix.length == matrix[i].length 
#  1 <= n <= 100 
#  1 <= matrix[i][j] <= n 
#  
#  Related Topics Array Hash Table Matrix 👍 126 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return self.helper(matrix) and self.helper(
            [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])

    def helper(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            s1 = set([i for i in range(1, len(matrix) + 1)])
            s2 = set(row)
            if s1 - s2:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)