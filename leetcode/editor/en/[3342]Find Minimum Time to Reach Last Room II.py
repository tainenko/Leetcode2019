# There is a dungeon with n x m rooms arranged as a grid. 
# 
#  You are given a 2D array moveTime of size n x m, where moveTime[i][j] 
# represents the minimum time in seconds when you can start moving to that room. You 
# start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving 
# between adjacent rooms takes one second for one move and two seconds for the next,
#  alternating between the two. 
# 
#  Return the minimum time to reach the room (n - 1, m - 1). 
# 
#  Two rooms are adjacent if they share a common wall, either horizontally or 
# vertically. 
# 
#  
#  Example 1: 
# 
#  
#  Input: moveTime = [[0,4],[4,4]] 
#  
# 
#  Output: 7 
# 
#  Explanation: 
# 
#  The minimum time required is 7 seconds. 
# 
#  
#  At time t == 4, move from room (0, 0) to room (1, 0) in one second. 
#  At time t == 5, move from room (1, 0) to room (1, 1) in two seconds. 
#  
# 
#  Example 2: 
# 
#  
#  Input: moveTime = [[0,0,0,0],[0,0,0,0]] 
#  
# 
#  Output: 6 
# 
#  Explanation: 
# 
#  The minimum time required is 6 seconds. 
# 
#  
#  At time t == 0, move from room (0, 0) to room (1, 0) in one second. 
#  At time t == 1, move from room (1, 0) to room (1, 1) in two seconds. 
#  At time t == 3, move from room (1, 1) to room (1, 2) in one second. 
#  At time t == 4, move from room (1, 2) to room (1, 3) in two seconds. 
#  
# 
#  Example 3: 
# 
#  
#  Input: moveTime = [[0,1],[1,2]] 
#  
# 
#  Output: 4 
# 
#  
#  Constraints: 
# 
#  
#  2 <= n == moveTime.length <= 750 
#  2 <= m == moveTime[i].length <= 750 
#  0 <= moveTime[i][j] <= 10⁹ 
#  
# 
#  Related Topics Array Graph Heap (Priority Queue) Matrix Shortest Path 👍 323 
# 👎 51


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = [[0, 0, 0]]
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[inf] * m for _ in range(n)]
        while pq:
            d, x, y = heapq.heappop(pq)
            if x == n - 1 and y == m - 1:
                return d
            if d > dist[x][y]:
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 > x + dx or 0 > y + dy or x + dx >= n or y + dy >= m:
                    continue
                t = max(d, moveTime[x + dx][y + dy]) + (x + y) % 2 + 1
                if dist[x + dx][y + dy] > t:
                    dist[x + dx][y + dy] = t
                    heapq.heappush(pq, (t, x + dx, y + dy))

# leetcode submit region end(Prohibit modification and deletion)
