#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (44.59%)
# Likes:    1679
# Dislikes: 62
# Total Accepted:    110.1K
# Total Submissions: 244K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        curr_sell = 0
        prev_sell = 0
        buy = -prices[0]
        for price in prices:
            tmp = curr_sell
            curr_sell = max(curr_sell, buy + price)
            buy = max(buy, prev_sell - price)
            prev_sell = tmp
        return curr_sell
# @lc code=end
