# Given an m x n picture consisting of black 'B' and white 'W' pixels and an 
# integer target, return the number of black lonely pixels. 
# 
#  A black lonely pixel is a character 'B' that located at a specific position (
# r, c) where: 
# 
#  
#  Row r and column c both contain exactly target black pixels. 
#  For all rows that have a black pixel at column c, they should be exactly the 
# same as row r. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W",
# "B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
# Output: 6
# Explanation: All the green 'B' are the black pixels we need (all 'B's at 
# column 1 and 3).
# Take 'B' at row r = 0 and column c = 1 as an example:
#  - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black 
# pixels. 
#  - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 
# 2. They are exactly the same as row r = 0.
#  
# 
#  Example 2: 
#  
#  
# Input: picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == picture.length 
#  n == picture[i].length 
#  1 <= m, n <= 200 
#  picture[i][j] is 'W' or 'B'. 
#  1 <= target <= min(m, n) 
#  
# 
#  Related Topics Array Hash Table Matrix 👍 82 👎 741

# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        rows = [0] * len(picture)
        cols = [0] * len(picture[0])
        m = defaultdict(int)
        for row in range(len(picture)):
            m["".join(picture[row])] += 1
            for col in range(len(picture[0])):
                if picture[row][col] == "B":
                    rows[row] += 1
                    cols[col] += 1
        res = 0
        for row in range(len(picture)):
            if m["".join(picture[row])] != target:
                continue
            for col in range(len(picture[0])):
                if picture[row][col] == "B" and rows[row] == target and cols[col] == target:
                    res += 1
        return res

    # leetcode submit region end(Prohibit modification and deletion)
