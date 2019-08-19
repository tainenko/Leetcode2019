#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (32.02%)
# Total Accepted:    313.6K
# Total Submissions: 978.1K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.dfs(board, (i, j), word[1:]):
                        return True
        return False

    def dfs(self, board, pos, word):
        if not word:
            return True
        i, j = pos
        dires = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in dires:
            if 0 <= i + x < len(board) and 0 <= j + y < len(board[0]):
                if board[i + x][j + y] == word[0]:
                    board[i][j] = board[i][j].swapcase()
                    if self.dfs(board, (i + x, j + y), word[1:]):
                        return True
                    board[i][j] = board[i][j].swapcase()
        return False
