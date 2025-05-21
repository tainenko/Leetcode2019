# You are given an m x n matrix of characters boxGrid representing a side-view 
# of a box. Each cell of the box is one of the following: 
# 
#  
#  A stone '#' 
#  A stationary obstacle '*' 
#  Empty '.' 
#  
# 
#  The box is rotated 90 degrees clockwise, causing some of the stones to fall 
# due to gravity. Each stone falls down until it lands on an obstacle, another 
# stone, or the bottom of the box. Gravity does not affect the obstacles' positions, 
# and the inertia from the box's rotation does not affect the stones' horizontal 
# positions. 
# 
#  It is guaranteed that each stone in boxGrid rests on an obstacle, another 
# stone, or the bottom of the box. 
# 
#  Return an n x m matrix representing the box after the rotation described 
# above. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: boxGrid = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: boxGrid = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: boxGrid = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == boxGrid.length 
#  n == boxGrid[i].length 
#  1 <= m, n <= 500 
#  boxGrid[i][j] is either '#', '*', or '.'. 
#  
# 
#  Related Topics Array Two Pointers Matrix 👍 1555 👎 80


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - i - 1] = boxGrid[i][j]

        for j in range(m):
            q = collections.deque()
            for i in range(n - 1, -1, -1):
                if rotated[i][j] == '*':
                    q.clear()
                elif rotated[i][j] == '.':
                    q.append(i)
                elif q:
                    rotated[q.popleft()][j] = '#'
                    rotated[i][j] = '.'
                    q.append(i)
        return rotated

# leetcode submit region end(Prohibit modification and deletion)
