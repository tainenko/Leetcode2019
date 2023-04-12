# There are n cities labeled from 1 to n. You are given the integer n and an 
# array connections where connections[i] = [xi, yi, costi] indicates that the cost 
# of connecting city xi and city yi (bidirectional connection) is costi. 
# 
#  Return the minimum cost to connect all the n cities such that there is at 
# least one path between each pair of cities. If it is impossible to connect all the 
# n cities, return -1, 
# 
#  The cost is the sum of the connections' costs used. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation: Choosing any 2 edges will connect all cities so we choose the 
# minimum 2.
#  
# 
#  Example 2: 
#  
#  
# Input: n = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation: There is no way to connect all cities even if all edges are used.
# 
#  
# 
#  
#  Constraints:
# 
#  
#  1 <= n <= 10⁴ 
#  1 <= connections.length <= 10⁴ 
#  connections[i].length == 3 
#  1 <= xi, yi <= n 
#  xi != yi 
#  0 <= costi <= 10⁵ 
#  
# 
#  Related Topics Union Find Graph Heap (Priority Queue) Minimum Spanning Tree ?
# ? 1024 👎 58


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        fa = [i for i in range(n+1)]

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        connections.sort(key=lambda x: x[2])
        linked = 0
        total = 0
        for x, y, cost in connections:
            x = find(x)
            y = find(y)
            if x == y:
                continue
            linked += 1
            total += cost
            fa[x] = y
            if linked == n - 1:
                return total
        return -1
# leetcode submit region end(Prohibit modification and deletion)
