# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 
#  👍 2831 👎 104


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        matrix = [['.'] * n for _ in range(n)]
        self.res = []
        self.dp(0,matrix)
        return self.res

    def is_valid(self, row, col, path):
        n = len(path)
        for i in range(row, -1, -1):
            if path[i][col] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if path[i][j] == 'Q':
                return False
        for i, j in zip(range(row, -1,-1), range(col, n)):
            if path[i][j] == 'Q':
                return False
        return True

    def dp(self, row, path):
        n = len(path)
        if row == n:
            self.res.append(["".join(x) for x in path])
            return
        for x in range(n):
            if self.is_valid(row, x, path):
                path[row][x] = 'Q'
                self.dp(row + 1, path)
                path[row][x] = '.'
# leetcode submit region end(Prohibit modification and deletion)
