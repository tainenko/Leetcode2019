# You are given two arrays rowSum and colSum of non-negative integers where 
# rowSum[i] is the sum of the elements in the iᵗʰ row and colSum[j] is the sum of the 
# elements of the jᵗʰ column of a 2D matrix. In other words, you do not know the 
# elements of the matrix, but you do know the sums of each row and column. 
# 
#  Find any matrix of non-negative integers of size rowSum.length x colSum.
# length that satisfies the rowSum and colSum requirements. 
# 
#  Return a 2D array representing any matrix that fulfills the requirements. 
# It's guaranteed that at least one matrix that fulfills the requirements exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: rowSum = [3,8], colSum = [4,7]
# Output: [[3,0],
#          [1,7]]
# Explanation: 
# 0ᵗʰ row: 3 + 0 = 3 == rowSum[0]
# 1ˢᵗ row: 1 + 7 = 8 == rowSum[1]
# 0ᵗʰ column: 3 + 1 = 4 == colSum[0]
# 1ˢᵗ column: 0 + 7 = 7 == colSum[1]
# The row and column sums match, and all matrix elements are non-negative.
# Another possible matrix is: [[1,2],
#                              [3,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: rowSum = [5,7,10], colSum = [8,6,8]
# Output: [[0,5,0],
#          [6,1,0],
#          [2,0,8]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= rowSum.length, colSum.length <= 500 
#  0 <= rowSum[i], colSum[i] <= 10⁸ 
#  sum(rowSum) == sum(colSum) 
#  
# 
#  Related Topics Array Greedy Matrix 👍 1319 👎 35


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
# leetcode submit region end(Prohibit modification and deletion)
