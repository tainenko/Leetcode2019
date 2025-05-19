# You are given a 2D character grid matrix of size m x n, represented as an 
# array of strings, where matrix[i][j] represents the cell at the intersection of the 
# iᵗʰ row and jᵗʰ column. Each cell is one of the following: 
# 
#  
#  '.' representing an empty cell. 
#  '#' representing an obstacle. 
#  An uppercase letter ('A'-'Z') representing a teleportation portal. 
#  
# 
#  You start at the top-left cell (0, 0), and your goal is to reach the bottom-
# right cell (m - 1, n - 1). You can move from the current cell to any adjacent 
# cell (up, down, left, right) as long as the destination cell is within the grid 
# bounds and is not an obstacle. 
# 
#  If you step on a cell containing a portal letter and you haven't used that 
# portal letter before, you may instantly teleport to any other cell in the grid 
# with the same letter. This teleportation does not count as a move, but each portal 
# letter can be used at most once during your journey. 
# 
#  Return the minimum number of moves required to reach the bottom-right cell. 
# If it is not possible to reach the destination, return -1. 
# 
#  
#  Example 1: 
# 
#  
#  Input: matrix = ["A..",".A.","..."] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  
# 
#  
#  Before the first move, teleport from (0, 0) to (1, 1). 
#  In the first move, move from (1, 1) to (1, 2). 
#  In the second move, move from (1, 2) to (2, 2). 
#  
# 
#  Example 2: 
# 
#  
#  Input: matrix = [".#...",".#.#.",".#.#.","...#."] 
#  
# 
#  Output: 13 
# 
#  Explanation: 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m == matrix.length <= 10³ 
#  1 <= n == matrix[i].length <= 10³ 
#  matrix[i][j] is either '#', '.', or an uppercase English letter. 
#  matrix[0][0] is not an obstacle. 
#  
# 
#  👍 61 👎 6
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        transports = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j].isalpha():
                    transports[matrix[i][j]].append((i, j))

        distances = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        q = collections.deque()

        def enqueue(x, y, d):
            if matrix[x][y].isalpha():
                for nx, ny in transports[matrix[x][y]]:
                    q.append((nx, ny))
                    distances[nx][ny] = d
            else:
                q.append((x, y))
                distances[x][y] = d

        enqueue(0, 0, 0)
        while q:
            x, y = q.popleft()
            if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
                return distances[x][y]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if x + dx < 0 or x + dx >= len(matrix) or y + dy < 0 or y + dy >= len(matrix[0]):
                    continue
                if matrix[x + dx][y + dy] == '#':
                    continue
                if distances[x + dx][y + dy] > distances[x][y] + 1:
                    enqueue(x + dx, y + dy, distances[x][y] + 1)

        return -1

# leetcode submit region end(Prohibit modification and deletion)
