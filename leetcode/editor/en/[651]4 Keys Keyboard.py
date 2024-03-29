# Imagine you have a special keyboard with the following keys: 
# 
#  
#  A: Print one 'A' on the screen. 
#  Ctrl-A: Select the whole screen. 
#  Ctrl-C: Copy selection to buffer. 
#  Ctrl-V: Print buffer on screen appending it after what has already been 
# printed. 
#  
# 
#  Given an integer n, return the maximum number of 'A' you can print on the 
# screen with at most n presses on the keys. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: We can at most get 3 A's on screen by pressing the following key 
# sequence:
# A, A, A
#  
# 
#  Example 2: 
# 
#  
# Input: n = 7
# Output: 9
# Explanation: We can at most get 9 A's on screen by pressing following key 
# sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 50 
#  
# 
#  Related Topics Math Dynamic Programming 👍 638 👎 86


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
