# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return tru
# e if the four points construct a square.
#
#  The coordinate of a point pi is represented as [xi, yi]. The input is not giv
# en in any order.
#
#  A valid square has four equal sides with positive length and four equal angle
# s (90-degree angles).
#
#
#  Example 1:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
#
#
#  Example 2:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
#
#
#  Example 3:
#
#
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
#
#
#
#  Constraints:
#
#
#  p1.length == p2.length == p3.length == p4.length == 2
#  -104 <= xi, yi <= 104
#
#  Related Topics Math
#  👍 458 👎 603


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        s = set()
        edges = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i + 1, 4):
                x1, y1 = edges[i]
                x2, y2 = edges[j]
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist == 0:
                    return False
                s.add(dist)
        return len(s) == 2
# leetcode submit region end(Prohibit modification and deletion)
