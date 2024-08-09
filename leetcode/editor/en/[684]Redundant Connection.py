# In this problem, a tree is an undirected graph that is connected and has no 
# cycles. 
# 
#  You are given a graph that started as a tree with n nodes labeled from 1 to 
# n, with one additional edge added. The added edge has two different vertices 
# chosen from 1 to n, and was not an edge that already existed. The graph is 
# represented as an array edges of length n where edges[i] = [ai, bi] indicates that there 
# is an edge between nodes ai and bi in the graph. 
# 
#  Return an edge that can be removed so that the resulting graph is a tree of 
# n nodes. If there are multiple answers, return the answer that occurs last in 
# the input. 
# 
#  
#  Example 1: 
#  
#  
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#  
# 
#  Example 2: 
#  
#  
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == edges.length 
#  3 <= n <= 1000 
#  edges[i].length == 2 
#  1 <= ai < bi <= edges.length 
#  ai != bi 
#  There are no repeated edges. 
#  The given graph is connected. 
#  
# 
#  Related Topics Depth-First Search Breadth-First Search Union Find Graph 👍 61
# 98 👎 403


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = list(range(len(edges) + 1))
        for a, b, in edges:

            root_a = self.find(a, tree)
            root_b = self.find(b, tree)
            if root_a == root_b:
                return [a, b]
            tree[root_a] = root_b

    def find(self, x, tree):
        if tree[x] == x:
            return x
        root = self.find(tree[x], tree)
        tree[x] = root
        return root
# leetcode submit region end(Prohibit modification and deletion)
