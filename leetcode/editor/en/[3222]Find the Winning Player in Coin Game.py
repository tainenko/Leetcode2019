# You are given two positive integers x and y, denoting the number of coins 
# with values 75 and 10 respectively. 
# 
#  Alice and Bob are playing a game. Each turn, starting with Alice, the player 
# must pick up coins with a total value 115. If the player is unable to do so, 
# they lose the game. 
# 
#  Return the name of the player who wins the game if both players play 
# optimally. 
# 
#  
#  Example 1: 
# 
#  
#  Input: x = 2, y = 7 
#  
# 
#  Output: "Alice" 
# 
#  Explanation: 
# 
#  The game ends in a single turn: 
# 
#  
#  Alice picks 1 coin with a value of 75 and 4 coins with a value of 10. 
#  
# 
#  Example 2: 
# 
#  
#  Input: x = 4, y = 11 
#  
# 
#  Output: "Bob" 
# 
#  Explanation: 
# 
#  The game ends in 2 turns: 
# 
#  
#  Alice picks 1 coin with a value of 75 and 4 coins with a value of 10. 
#  Bob picks 1 coin with a value of 75 and 4 coins with a value of 10. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= x, y <= 100 
#  
# 
#  Related Topics Math Simulation Game Theory 👍 61 👎 5


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return self.helper(x, y, 0)

    def helper(self, x: int, y: int, player: int):
        if x < 1 or y < 4:
            return "Alice" if player else "Bob"
        return self.helper(x - 1, y - 4, 1 - player)
# leetcode submit region end(Prohibit modification and deletion)
