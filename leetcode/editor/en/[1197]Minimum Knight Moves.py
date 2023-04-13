# In an infinite chess board with coordinates from -infinity to +infinity, you 
# have a knight at square [0, 0]. 
# 
#  A knight has 8 possible moves it can make, as illustrated below. Each move 
# is two squares in a cardinal direction, then one square in an orthogonal 
# direction. 
#  
#  Return the minimum number of steps needed to move the knight to the square [
# x, y]. It is guaranteed the answer exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#  
# 
#  Example 2: 
# 
#  
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#  
# 
#  
#  Constraints: 
# 
#  
#  -300 <= x, y <= 300 
#  0 <= |x| + |y| <= 300 
#  
# 
#  Related Topics Breadth-First Search 👍 1381 👎 384


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        visited = set()
        visited.add((0, 0))
        q = deque([((0, 0), 0)])
        while q:
            pos, step = q.popleft()
            step += 1
            for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos == (x, y):
                    return step
                if new_pos in visited:
                    continue
                visited.add(new_pos)
                q.append((new_pos, step))

# leetcode submit region end(Prohibit modification and deletion)
