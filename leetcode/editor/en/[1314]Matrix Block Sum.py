# Given a m x n matrix mat and an integer k, return a matrix answer where each 
# answer[i][j] is the sum of all elements mat[r][c] for: 
# 
#  
#  i - k <= r <= i + k, 
#  j - k <= c <= j + k, and 
#  (r, c) is a valid position in the matrix. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, k <= 100 
#  1 <= mat[i][j] <= 100 
#  
# 
#  Related Topics Array Matrix Prefix Sum 👍 2259 👎 345


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + \
                                       prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(i - k, 0) + 1
                c1 = max(j - k, 0) + 1
                r2 = min(i + k, m - 1) + 1
                c2 = min(j + k, n - 1) + 1

                res[i][j] = prefix[r2][c2] - prefix[r2][c1 - 1] - \
                            prefix[r1 - 1][c2] + prefix[r1 - 1][c1 - 1]
        return res
# leetcode submit region end(Prohibit modification and deletion)
