# Given a 2D array rooks of length n, where rooks[i] = [xi, yi] indicates the 
# position of a rook on an n x n chess board. Your task is to move the rooks 1 cell 
# at a time vertically or horizontally (to an adjacent cell) such that the board 
# becomes peaceful. 
# 
#  A board is peaceful if there is exactly one rook in each row and each column.
#  
# 
#  Return the minimum number of moves required to get a peaceful board. 
# 
#  Note that at no point can there be two rooks in the same cell. 
# 
#  
#  Example 1: 
# 
#  
#  Input: rooks = [[0,0],[1,0],[1,1]] 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
# 
#  Example 2: 
# 
#  
#  Input: rooks = [[0,0],[0,1],[0,2],[0,3]] 
#  
# 
#  Output: 6 
# 
#  Explanation: 
# 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n == rooks.length <= 500 
#  0 <= xi, yi <= n - 1 
#  The input is generated such that there are no 2 rooks in the same cell. 
#  
# 
#  Related Topics Array Greedy Sorting Counting Sort 👍 56 👎 12


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        res = 0
        rooks.sort()
        m = len(rooks)
        for i in range(m):
            chess = rooks[i]
            res += abs(i - chess[0])
        rooks.sort(key=lambda x: x[1])
        for j in range(m):
            chess = rooks[j]
            res += abs(j - chess[1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
