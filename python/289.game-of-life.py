#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (47.00%)
# Likes:    1216
# Dislikes: 223
# Total Accepted:    139.9K
# Total Submissions: 284.6K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = self.count_neighbors(i, j, m,n,board)
                if board[i][j] == 1:
                    if count < 2 or count>3:
                        board[i][j] = 2
                    elif count == 2 or count == 3:
                        board[i][j] = 1
                elif board[i][j]==0:
                    if count == 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
        return board

    def count_neighbors(self, i, j, m, n,board):
        dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        count = 0
        for x, y in dirs:
            if 0 <= x + i < m and 0 <= y + j < n:
                if board[x + i][y + j] in (1,2):
                    count += 1
        return count

# @lc code=end
