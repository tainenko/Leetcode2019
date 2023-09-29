# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day, and an integer fee representing a transaction fee. 
# 
#  Find the maximum profit you can achieve. You may complete as many 
# transactions as you like, but you need to pay the transaction fee for each transaction. 
# 
#  Note: 
# 
#  
#  You may not engage in multiple transactions simultaneously (i.e., you must 
# sell the stock before you buy again). 
#  The transaction fee is only charged once for each stock purchase and sale. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 5 * 10⁴ 
#  1 <= prices[i] < 5 * 10⁴ 
#  0 <= fee < 5 * 10⁴ 
#  
# 
#  Related Topics Array Dynamic Programming Greedy 👍 6766 👎 188


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f1, f2 = -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, f2 - price)
            f2 = max(f2, f1 + price - fee)
        return f2
# leetcode submit region end(Prohibit modification and deletion)
