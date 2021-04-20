# There is an m by n grid with a ball. Given the start coordinate (i,j) of the b
# all, you can move the ball to adjacent cell or cross the grid boundary in four d
# irections (up, down, left, right). However, you can at most move N times. Find o
# ut the number of paths to move the ball out of grid boundary. The answer may be 
# very large, return it after mod 109 + 7. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
#  
# 
#  Example 2: 
# 
#  
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  Once you move the ball out of boundary, you cannot move it back. 
#  The length and height of the grid is in range [1,50]. 
#  N is in range [0,50]. 
#  
#  Related Topics Dynamic Programming Depth-first Search 
#  👍 759 👎 148


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        for k in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[k - 1][x - 1][y]
                    v2 = 1 if x == m - 1 else dp[k - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[k - 1][x][y - 1]
                    v4 = 1 if y == n - 1 else dp[k - 1][x][y + 1]
                    dp[k][x][y] = (v1 + v2 + v3 + v4) % (10 ** 9 + 7)

        return dp[N][i][j]

# leetcode submit region end(Prohibit modification and deletion)
