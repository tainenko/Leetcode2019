# There is a long table with a line of plates and candles arranged on top of it.
#  You are given a 0-indexed string s consisting of characters '*' and '|' only, 
# where a '*' represents a plate and a '|' represents a candle. 
# 
#  You are also given a 0-indexed 2D integer array queries where queries[i] = [
# lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each 
# query, you need to find the number of plates between candles that are in the 
# substring. A plate is considered between candles if there is at least one candle to 
# its left and at least one candle to its right in the substring. 
# 
#  
#  For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||*
# *|". The number of plates between candles in this substring is 2, as each of 
# the two plates has at least one candle in the substring to its left and right. 
#  
# 
#  Return an integer array answer where answer[i] is the answer to the iᵗʰ 
# query. 
# 
#  
#  Example 1: 
#  
#  
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.
#  
# 
#  Example 2: 
#  
#  
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15
# ,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= s.length <= 10⁵ 
#  s consists of '*' and '|' characters. 
#  1 <= queries.length <= 10⁵ 
#  queries[i].length == 2 
#  0 <= lefti <= righti < s.length 
#  
# 
#  Related Topics Array String Binary Search Prefix Sum 👍 878 👎 32


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pre_sum = [0] * len(s)
        total = 0
        for i, char in enumerate(s):
            if char == "*":
                total += 1
            pre_sum[i] = total
        left_index = [-1] * len(s)
        curr = -1
        for i, char in enumerate(s):
            if char == "|":
                curr = i
            left_index[i] = curr
        right_index = [-1] * len(s)
        curr = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                curr = i
            right_index[i] = curr
        res = [0] * len(queries)
        for idx, (start, end) in enumerate(queries):
            i = right_index[start]
            j = left_index[end]
            if i >= 0 and j >= 0 and i < j:
                res[idx] = pre_sum[j] - pre_sum[i]
        return res

        # leetcode submit region end(Prohibit modification and deletion)
