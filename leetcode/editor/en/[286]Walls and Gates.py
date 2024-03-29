# You are given an m x n grid rooms initialized with these three possible 
# values. 
# 
#  
#  -1 A wall or an obstacle. 
#  0 A gate. 
#  INF Infinity means an empty room. We use the value 2³¹ - 1 = 2147483647 to 
# represent INF as you may assume that the distance to a gate is less than 214748364
# 7. 
#  
# 
#  Fill each empty room with the distance to its nearest gate. If it is 
# impossible to reach a gate, it should be filled with INF. 
# 
#  
#  Example 1: 
# 
#  
# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647
# ,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#  
# 
#  Example 2: 
# 
#  
# Input: rooms = [[-1]]
# Output: [[-1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == rooms.length 
#  n == rooms[i].length 
#  1 <= m, n <= 250 
#  rooms[i][j] is -1, 0, or 2³¹ - 1. 
#  
#  Related Topics Array Breadth-First Search Matrix 👍 2354 👎 38


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(x, y, val):
            if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] <= val:
                return
            rooms[x][y] = val
            bfs(x - 1, y, val + 1)
            bfs(x, y - 1, val + 1)
            bfs(x + 1, y, val + 1)
            bfs(x, y + 1, val + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    bfs(i - 1, j, 1)
                    bfs(i, j - 1, 1)
                    bfs(i + 1, j, 1)
                    bfs(i, j + 1, 1)

# leetcode submit region end(Prohibit modification and deletion)
