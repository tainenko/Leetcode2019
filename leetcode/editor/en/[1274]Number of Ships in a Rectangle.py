# (This problem is an interactive problem.) 
# 
#  Each ship is located at an integer point on the sea represented by a 
# cartesian plane, and each integer point may contain at most 1 ship. 
# 
#  You have a function Sea.hasShips(topRight, bottomLeft) which takes two 
# points as arguments and returns true If there is at least one ship in the rectangle 
# represented by the two points, including on the boundary. 
# 
#  Given two points: the top right and bottom left corners of a rectangle, 
# return the number of ships present in that rectangle. It is guaranteed that there 
# are at most 10 ships in that rectangle. 
# 
#  Submissions making more than 400 calls to hasShips will be judged Wrong 
# Answer. Also, any solutions that attempt to circumvent the judge will result in 
# disqualification. 
# 
#  
#  Example : 
#  
#  
# Input: 
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
#  
# 
#  Example 2: 
# 
#  
# Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  On the input ships is only given to initialize the map internally. You must 
# solve this problem "blindfolded". In other words, you must find the answer using 
# the given hasShips API, without knowing the ships position. 
#  0 <= bottomLeft[0] <= topRight[0] <= 1000 
#  0 <= bottomLeft[1] <= topRight[1] <= 1000 
#  topRight != bottomLeft 
#  
# 
#  Related Topics Array Divide and Conquer Interactive 👍 511 👎 55


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        if x1 > x2 or y1 > y2:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if x1 == x2 and y1 == y2:
            return 1

        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        a = self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
        b = self.countShips(sea, Point(mid_x, y2), Point(x1, mid_y + 1))
        c = self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
        d = self.countShips(sea, Point(x2, mid_y), Point(mid_x + 1, y1))
        return a + b + c + d
# leetcode submit region end(Prohibit modification and deletion)
