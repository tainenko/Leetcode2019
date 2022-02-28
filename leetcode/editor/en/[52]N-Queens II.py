# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return the number of distinct solutions to the n-queens 
# puzzle. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 👍 1389 👎 203


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [-1] * n
        res = 0

        def helper(board, row):
            if row == len(board):
                nonlocal res
                res += 1
                return
            for col in range(n):
                board[row] = col
                if self.is_valid(board, row, col):
                    helper(board, row + 1)
                board[row] = -1

        helper(board, 0)
        return res

    def is_valid(self, board, row, col):
        for pre_row in range(row):
            if board[pre_row] == -1 or board[pre_row] == col or abs(pre_row - row) == abs(board[pre_row] - col):
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
