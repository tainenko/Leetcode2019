#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (23.58%)
# Total Accepted:    159.4K
# Total Submissions: 669.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m = len(board)
        n = len(board[0])
        self.border(board, (m, n), '$', 'O')
        self.dfs(board, (m, n), 'X', 'O')
        self.border(board, (m, n), 'O', '$')

    def helper(self, board, len, pos, letter, target):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = pos
        m, n = len
        board[x][y] = letter
        for i, j in dirs:
            if 0 <= x + i < m and 0 <= y + j < n and board[x + i][y + j] == target:
                self.helper(board, (m, n), (x + i, y + j), letter, target)

    def border(self, board, len, letter, target):
        m, n = len
        for top in range(n):
            if board[0][top] == target:
                self.helper(board, (m, n), (0, top), letter, target)

        for bottom in range(n):
            if board[-1][bottom] == target:
                self.helper(board, (m, n), (m - 1, bottom), letter, target)

        for left in range(m):
            if board[left][0] == target:
                self.helper(board, (m, n), (left, 0), letter, target)

        for right in range(m):
            if board[right][-1] == target:
                self.helper(board, (m, n), (right, n - 1), letter, target)

    def dfs(self, board, len, letter, target):
        m, n = len
        for i in range(m):
            for j in range(n):
                if board[i][j] == target:
                    self.helper(board, (m, n), (i, j), letter, target)
