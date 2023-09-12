# The diameter of a tree is the number of edges in the longest path in that 
# tree. 
# 
#  There is an undirected tree of n nodes labeled from 0 to n - 1. You are 
# given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates 
# that there is an undirected edge between nodes ai and bi in the tree. 
# 
#  Return the diameter of the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: The longest path of the tree is the path 1 - 0 - 2.
#  
# 
#  Example 2: 
#  
#  
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == edges.length + 1 
#  1 <= n <= 10⁴ 
#  0 <= ai, bi < n 
#  ai != bi 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Graph 
# Topological Sort 👍 751 👎 17
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        def dfs(u, t):
            nonlocal vis, res, dist
            if u in vis:
                return
            vis.add(u)
            for v in trie[u]:
                dfs(v, t + 1)
            if res < t:
                res = t
                dist = u

        trie = defaultdict(set)
        for u, v in edges:
            trie[u].add(v)
            trie[v].add(u)

        vis = set()
        res = 0
        dist = 0
        dfs(edges[0][0], 0)

        vis = set()
        dfs(dist, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
