# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer 
# n and a list of edges where edges[i] = [ai, bi] indicates that there is an 
# undirected edge between nodes ai and bi in the graph. 
# 
#  Return true if the edges of the given graph make up a valid tree, and false 
# otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2000 
#  0 <= edges.length <= 5000 
#  edges[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  There are no self-loops or repeated edges. 
#  
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 21
# 01 👎 55


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dist = defaultdict(list)
        for node1, node2 in edges:
            dist[node1].append(node2)
            dist[node2].append(node1)
        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            visited.add(node)
            for point in dist[node]:
                if point not in visited:
                    visited.add(point)
                    q.append(point)
        return len(visited) == n
# leetcode submit region end(Prohibit modification and deletion)
