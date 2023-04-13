# Given an m x n matrix mat where every row is sorted in strictly increasing 
# order, return the smallest common element in all rows. 
# 
#  If there is no common element, return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# Output: 5
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 500 
#  1 <= mat[i][j] <= 10⁴ 
#  mat[i] is sorted in strictly increasing order. 
#  
# 
#  Related Topics Array Hash Table Binary Search Matrix Counting 👍 515 👎 28


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        res = set(mat[0])
        for i in range(1, len(mat)):
            res = res.intersection(set(mat[i]))
        if len(res):
            return min(res)
        return -1

# leetcode submit region end(Prohibit modification and deletion)
