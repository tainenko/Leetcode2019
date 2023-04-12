# You are given an array colors, in which there are three colors: 1, 2 and 3. 
# 
#  You are also given some queries. Each query consists of two integers i and c,
#  return the shortest distance between the given index i and the target color c. 
# If there is no solution return -1. 
# 
#  
#  Example 1: 
# 
#  
# Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]
# Explanation: 
# The nearest 3 from index 1 is at index 4 (3 steps away).
# The nearest 2 from index 2 is at index 2 itself (0 steps away).
# The nearest 1 from index 6 is at index 3 (3 steps away).
#  
# 
#  Example 2: 
# 
#  
# Input: colors = [1,2], queries = [[0,3]]
# Output: [-1]
# Explanation: There is no 3 in the array.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= colors.length <= 5*10^4 
#  1 <= colors[i] <= 3 
#  1 <= queries.length <= 5*10^4 
#  queries[i].length == 2 
#  0 <= queries[i][0] < colors.length 
#  1 <= queries[i][1] <= 3 
#  
# 
#  Related Topics Array Binary Search Dynamic Programming 👍 491 👎 21


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dp = [[2147483647, 2147483647, 2147483647] for _ in range(len(colors))]
        dp[0][colors[0] - 1] = 0
        for i in range(1, len(colors)):

            for color in range(1, 4):
                if color == colors[i]:
                    dp[i][color - 1] = 0
                else:
                    dp[i][color - 1] = min(dp[i - 1][color - 1] + 1, dp[i][color - 1])
        for i in range(len(colors) - 2, -1, -1):
            for color in range(1, 4):
                if color == colors[i]:
                    continue
                else:
                    dp[i][color - 1] = min(dp[i + 1][color - 1] + 1, dp[i][color - 1])
        return [dp[query[0]][query[1] - 1] if dp[query[0]][query[1] - 1] != 2147483647 else -1 for query in queries]
# leetcode submit region end(Prohibit modification and deletion)
