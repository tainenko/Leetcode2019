# Given an array of points where points[i] = [xi, yi] represents a point on the 
# X-Y plane, return the maximum number of points that lie on the same straight 
# line. 
# 
#  
#  Example 1: 
#  
#  
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#  
# 
#  Example 2: 
#  
#  
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= points.length <= 300 
#  points[i].length == 2 
#  -10⁴ <= xi, yi <= 10⁴ 
#  All the points are unique. 
#  
# 
#  Related Topics Array Hash Table Math Geometry 👍 3587 👎 409


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            lines = defaultdict(int)
            duplicate = 1
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicate += 1
                    continue
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                gcd = self.gcd(x, y)
                lines[(x // gcd), (y // gcd)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicate)
        return res

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    # leetcode submit region end(Prohibit modification and deletion)
