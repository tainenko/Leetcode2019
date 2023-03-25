# Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
# rectangle containing only 1's and return its area. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1",
# "1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [["0"]]
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [["1"]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  rows == matrix.length 
#  cols == matrix[i].length 
#  1 <= row, cols <= 200 
#  matrix[i][j] is '0' or '1'. 
#  
#  Related Topics Array Dynamic Programming Stack Matrix Monotonic Stack 👍 6376
#  👎 106


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not (matrix[0]):
            return 0
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        height = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            res = max(res, self.max_rectangle(height))
        return res

    def max_rectangle(self, height):
        stack = list()
        res = 0
        for i in range(len(height)):
            curr = height[i]
            while stack and curr < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
