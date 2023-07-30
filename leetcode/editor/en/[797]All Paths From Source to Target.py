# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find 
# all possible paths from node 0 to node n - 1 and return them in any order. 
# 
#  The graph is given as follows: graph[i] is a list of all nodes you can visit 
# from node i (i.e., there is a directed edge from node i to node graph[i][j]). 
# 
#  
#  Example 1: 
#  
#  
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#  
# 
#  Example 2: 
#  
#  
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == graph.length 
#  2 <= n <= 15 
#  0 <= graph[i][j] < n 
#  graph[i][j] != i (i.e., there will be no self-loops). 
#  All the elements of graph[i] are unique. 
#  The input graph is guaranteed to be a DAG. 
#  
# 
#  Related Topics Backtracking Depth-First Search Breadth-First Search Graph 👍 
# 6709 👎 137


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        res = []
        def dfs(path, curr):
            if curr==len(graph)-1:
                res.append(path.copy())
                return
            for node in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    path.append(node)
                    dfs(path,node)
                    visited.remove(node)
                    path.pop()
            return
        path = [0]
        dfs(path, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
