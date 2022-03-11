# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing 
# moving one unit north, south, east, or west, respectively. You start at the 
# origin (0, 0) on a 2D plane and walk on the path specified by path. 
# 
#  Return true if the path crosses itself at any point, that is, if at any time 
# you are on a location you have previously visited. Return false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
#  
# 
#  Example 2: 
# 
#  
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= path.length <= 10⁴ 
#  path[i] is either 'N', 'S', 'E', or 'W'. 
#  
#  Related Topics Hash Table String 👍 460 👎 8


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = 0
        y = 0
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'W':
                x -= 1
            elif d == 'E':
                x += 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
# leetcode submit region end(Prohibit modification and deletion)
