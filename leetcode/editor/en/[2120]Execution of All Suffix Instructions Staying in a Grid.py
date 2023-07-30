# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right 
# cell at (n - 1, n - 1). You are given the integer n and an integer array 
# startPos where startPos = [startrow, startcol] indicates that a robot is initially at 
# cell (startrow, startcol). 
# 
#  You are also given a 0-indexed string s of length m where s[i] is the iᵗʰ 
# instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 
# 'D' (move down). 
# 
#  The robot can begin executing from any iᵗʰ instruction in s. It executes the 
# instructions one by one towards the end of s but it stops if either of these 
# conditions is met: 
# 
#  
#  The next instruction will move the robot off the grid. 
#  There are no more instructions left to execute. 
#  
# 
#  Return an array answer of length m where answer[i] is the number of 
# instructions the robot can execute if the robot begins executing from the iᵗʰ 
# instruction in s. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3, startPos = [0,1], s = "RRDDLU"
# Output: [1,5,4,3,1,0]
# Explanation: Starting from startPos and beginning execution from the iᵗʰ 
# instruction:
# - 0ᵗʰ: "RRDDLU". Only one instruction "R" can be executed before it moves off 
# the grid.
# - 1ˢᵗ:  "RDDLU". All five instructions can be executed while it stays in the 
# grid and ends at (1, 1).
# - 2ⁿᵈ:   "DDLU". All four instructions can be executed while it stays in the 
# grid and ends at (1, 0).
# - 3ʳᵈ:    "DLU". All three instructions can be executed while it stays in the 
# grid and ends at (0, 0).
# - 4ᵗʰ:     "LU". Only one instruction "L" can be executed before it moves off 
# the grid.
# - 5ᵗʰ:      "U". If moving up, it would move off the grid.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 2, startPos = [1,1], s = "LURD"
# Output: [4,1,0,0]
# Explanation:
# - 0ᵗʰ: "LURD".
# - 1ˢᵗ:  "URD".
# - 2ⁿᵈ:   "RD".
# - 3ʳᵈ:    "D".
#  
# 
#  Example 3: 
#  
#  
# Input: n = 1, startPos = [0,0], s = "LRUD"
# Output: [0,0,0,0]
# Explanation: No matter which instruction the robot begins execution from, it 
# would move off the grid.
#  
# 
#  
#  Constraints: 
# 
#  
#  m == s.length 
#  1 <= n, m <= 500 
#  startPos.length == 2 
#  0 <= startrow, startcol < n 
#  s consists of 'L', 'R', 'U', and 'D'. 
#  
# 
#  Related Topics String Simulation 👍 477 👎 44


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dirs = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
        ans = [0] * len(s)
        for i in range(len(s)):
            tmp = 0
            x, y = startPos
            for c in s[i:]:
                dx, dy = dirs[c]
                x += dx
                y += dy
                if x < 0 or x >= n:
                    break
                if y < 0 or y >= n:
                    break
                tmp += 1
            ans[i] = tmp
        return ans
# leetcode submit region end(Prohibit modification and deletion)
