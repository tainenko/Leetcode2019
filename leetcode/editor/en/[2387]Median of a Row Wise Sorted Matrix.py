# Given an m x n matrix grid containing an odd number of integers where each 
# row is sorted in non-decreasing order, return the median of the matrix. 
# 
#  You must solve the problem in less than O(m * n) time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
# Output: 2
# Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4.
#  The median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,1,3,3,4]]
# Output: 3
# Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The 
# median is 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  m and n are both odd. 
#  1 <= grid[i][j] <= 10⁶ 
#  grid[i] is sorted in non-decreasing order. 
#  
# 
#  Related Topics Array Binary Search Matrix 👍 60 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        target = len(grid) * len(grid[0]) // 2 + 1
        l = 0
        r = 10 ** 6
        while l < r:
            mid = l + (r - l) // 2
            if sum(bisect_right(row, mid) for row in grid) >= target:
                r = mid
            else:
                l = mid + 1
        return l
# leetcode submit region end(Prohibit modification and deletion)
