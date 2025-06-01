# You are given an array points representing integer coordinates of some points 
# on a 2D-plane, where points[i] = [xi, yi]. 
# 
#  The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan 
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute 
# value of val. 
# 
#  Return the minimum cost to make all points connected. All points are 
# connected if there is exactly one simple path between any two points. 
# 
#  
#  Example 1: 
#  
#  
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
#  
# 
#  Example 2: 
# 
#  
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= points.length <= 1000 
#  -10⁶ <= xi, yi <= 10⁶ 
#  All pairs (xi, yi) are distinct. 
#  
# 
#  Related Topics Array Union Find Graph Minimum Spanning Tree 👍 5323 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.parent[self.find(y)]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                distance.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        distance.sort()
        result = 0
        un = UnionFind(n)
        for edge in distance:
            if un.find(edge[1]) != un.find(edge[2]):
                result += edge[0]
                un.union(edge[1], edge[2])
        return result
# leetcode submit region end(Prohibit modification and deletion)
