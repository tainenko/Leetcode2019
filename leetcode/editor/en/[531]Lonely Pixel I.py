# Given an m x n picture consisting of black 'B' and white 'W' pixels, return 
# the number of black lonely pixels. 
# 
#  A black lonely pixel is a character 'B' that located at a specific position 
# where the same row and same column don't have any other black pixels. 
# 
#  
#  Example 1: 
#  
#  
# Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#  
# 
#  Example 2: 
#  
#  
# Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == picture.length 
#  n == picture[i].length 
#  1 <= m, n <= 500 
#  picture[i][j] is 'W' or 'B'. 
#  
# 
#  Related Topics Array Hash Table Matrix 👍 394 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        res = 0
        rows = defaultdict(int)
        cols = defaultdict(int)
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == "B":
                    rows[row] += 1
                    cols[col] += 1
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == "B" and rows[row] == 1 and cols[col] == 1:
                    res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
