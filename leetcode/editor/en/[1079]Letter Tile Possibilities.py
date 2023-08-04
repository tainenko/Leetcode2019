# You have n tiles, where each tile has one letter tiles[i] printed on it. 
# 
#  Return the number of possible non-empty sequences of letters you can make 
# using the letters printed on those tiles. 
# 
#  
#  Example 1: 
# 
#  
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", 
# "ABA", "BAA".
#  
# 
#  Example 2: 
# 
#  
# Input: tiles = "AAABBC"
# Output: 188
#  
# 
#  Example 3: 
# 
#  
# Input: tiles = "V"
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tiles.length <= 7 
#  tiles consists of uppercase English letters. 
#  
# 
#  Related Topics Hash Table String Backtracking Counting 👍 2317 👎 64
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)

        def dfs(count: Dict[int, int]) -> int:
            res = 0
            for k, v in count.items():
                if v == 0:
                    continue
                count[k] -= 1
                res += 1 + dfs(count)
                count[k] += 1
            return res

        return dfs(cnt)

# leetcode submit region end(Prohibit modification and deletion)
