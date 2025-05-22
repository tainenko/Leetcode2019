# You are given an integer n. There is an undirected graph with n vertices, 
# numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [
# ai, bi] denotes that there exists an undirected edge connecting vertices ai and 
# bi. 
# 
#  Return the number of complete connected components of the graph. 
# 
#  A connected component is a subgraph of a graph in which there exists a path 
# between any two vertices, and no vertex of the subgraph shares an edge with a 
# vertex outside of the subgraph. 
# 
#  A connected component is said to be complete if there exists an edge between 
# every pair of its vertices. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components 
# of this graph are complete.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since 
# there is an edge between every pair of two vertices. On the other hand, the 
# component containing vertices 3, 4, and 5 is not complete since there is no edge 
# between vertices 4 and 5. Thus, the number of complete components in this graph is 1
# .
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 50 
#  0 <= edges.length <= n * (n - 1) / 2 
#  edges[i].length == 2 
#  0 <= ai, bi <= n - 1 
#  ai != bi 
#  There are no repeated edges. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 11
# 60 👎 28


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i: int) -> (int, int):
            visited[i] = True
            cnt, edge = 1, len(g[i])
            for j in g[i]:
                if visited[j]:
                    continue
                ncnt, nedge = dfs(j)
                cnt += ncnt
                edge += nedge
            return cnt, edge

        g = defaultdict(list)
        for start, end in edges:
            g[start].append(end)
            g[end].append(start)

        visited = [False] * n
        res = 0
        for i in range(n):
            if visited[i]:
                continue
            cnt, edge = dfs(i)
            if cnt * (cnt - 1) == edge:
                res += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
