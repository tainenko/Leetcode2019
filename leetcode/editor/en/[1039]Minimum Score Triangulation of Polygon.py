# You have a convex n-sided polygon where each vertex has an integer value. You 
# are given an integer array values where values[i] is the value of the ith vertex
#  (i.e., clockwise order). 
# 
#  You will triangulate the polygon into n - 2 triangles. For each triangle, the
#  value of that triangle is the product of the values of its vertices, and the to
# tal score of the triangulation is the sum of these values over all n - 2 triangl
# es in the triangulation. 
# 
#  Return the smallest possible total score that you can achieve with some trian
# gulation of the polygon. 
# 
#  
#  Example 1: 
# 
#  
# Input: values = [1,2,3]
# Output: 6
# Explanation: The polygon is already triangulated, and the score of the only tr
# iangle is 6.
#  
# 
#  Example 2: 
# 
#  
# Input: values = [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7
#  = 245, or 3*4*5 + 3*4*7 = 144.
# The minimum score is 144.
#  
# 
#  Example 3: 
# 
#  
# Input: values = [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 +
#  1*1*1 = 13.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == values.length 
#  3 <= n <= 50 
#  1 <= values[i] <= 100 
#  
#  Related Topics Array Dynamic Programming 
#  👍 728 👎 95


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for j in range(2, n):
            for i in range(j - 2, -1, -1):
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
        return dp[0][n - 1]
# leetcode submit region end(Prohibit modification and deletion)
