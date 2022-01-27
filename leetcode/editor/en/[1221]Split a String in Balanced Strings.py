# Balanced strings are those that have an equal quantity of 'L' and 'R' 
# characters. 
# 
#  Given a balanced string s, split it in the maximum amount of balanced 
# strings. 
# 
#  Return the maximum amount of split balanced strings. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring 
# contains same number of 'L' and 'R'.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring 
# contains same number of 'L' and 'R'.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] is either 'L' or 'R'. 
#  s is a balanced string. 
#  
#  Related Topics String Greedy Counting 👍 1549 👎 714


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
