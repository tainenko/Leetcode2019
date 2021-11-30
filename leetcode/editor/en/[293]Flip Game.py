# You are playing a Flip Game with your friend. 
# 
#  You are given a string currentState that contains only '+' and '-'. You and 
# your friend take turns to flip two consecutive "++" into "--". The game ends 
# when a person can no longer make a move, and therefore the other person will be the 
# winner. 
# 
#  Return all possible states of the string currentState after one valid move. 
# You may return the answer in any order. If there is no valid move, return an 
# empty list []. 
# 
#  
#  Example 1: 
# 
#  
# Input: currentState = "++++"
# Output: ["--++","+--+","++--"]
#  
# 
#  Example 2: 
# 
#  
# Input: currentState = "+"
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= currentState.length <= 500 
#  currentState[i] is either '+' or '-'. 
#  
#  Related Topics String 👍 150 👎 354


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []
        res = []

        for i in range(len(currentState) - 1):
            if currentState[i:i + 2] == '++':
                res.append(currentState[:i] + '--' + currentState[i + 2:])
        return res
# leetcode submit region end(Prohibit modification and deletion)
