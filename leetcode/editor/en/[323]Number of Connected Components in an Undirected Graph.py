# You have a graph of n nodes. You are given an integer n and an array edges 
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the 
# graph. 
# 
#  Return the number of connected components in the graph. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
#  
# 
#  Example 2: 
#  
#  
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 2000 
#  1 <= edges.length <= 5000 
#  edges[i].length == 2 
#  0 <= ai <= bi < n 
#  ai != bi 
#  There are no repeated edges. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 24
# 50 👎 81


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        e = defaultdict(deque)
        for x, y in edges:
            e[x].append(y)
            e[y].append(x)
        visited = set()
        cnt = 0
        for i in range(n):
            if i in visited:
                continue
            cnt += 1
            visited.add(i)
            q = e[i]
            while q:
                node = q.popleft()
                visited.add(node)
                for dst in e[node]:
                    if dst in visited:
                        continue
                    q.append(dst)
        return cnt

# leetcode submit region end(Prohibit modification and deletion)
