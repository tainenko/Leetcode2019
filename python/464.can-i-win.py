#
# @lc app=leetcode id=464 lang=python
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (28.56%)
# Likes:    873
# Dislikes: 156
# Total Accepted:    48.4K
# Total Submissions: 169.4K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#

# @lc code=start
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger >= desiredTotal:
            return True
        if (maxChoosableInteger + 1) * maxChoosableInteger < desiredTotal * 2:
            return False
        dp = dict()

        def helper(state, total):
            for x in range(maxChoosableInteger, 0, -1):
                if not state & (1 << (x - 1)):
                    if x + total >= desiredTotal:
                        dp[state] = True
                        return True
                    break
            for x in range(1, maxChoosableInteger + 1):
                if not state & (1 << (x - 1)):
                    nstate = state | (1 << (x - 1))
                    if nstate not in dp:
                        dp[nstate] = helper(nstate, total + x)
                    if not dp[nstate]:
                        dp[state] = True
                        return True
            dp[state] = False
            return False

        return helper(0, 0)

# @lc code=end
