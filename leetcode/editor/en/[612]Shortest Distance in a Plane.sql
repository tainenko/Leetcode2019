#Table: Point2D 
#
# 
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| x           | int  |
#| y           | int  |
#+-------------+------+
#(x, y) is the primary key column for this table.
#Each row of this table indicates the position of a point on the X-Y plane.
# 
#
# 
#
# The distance between two points p1(x1, y1) and p2(x2, y2) is sqrt((x2 - x1)² +
# (y2 - y1)²). 
#
# Write an SQL query to report the shortest distance between any two points 
#from the Point2D table. Round the distance to two decimal points. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Point2D table:
#+----+----+
#| x  | y  |
#+----+----+
#| -1 | -1 |
#| 0  | 0  |
#| -1 | -2 |
#+----+----+
#Output: 
#+----------+
#| shortest |
#+----------+
#| 1.00     |
#+----------+
#Explanation: The shortest distance is 1.00 from point (-1, -1) to (-1, 2).
# 
#
# Related Topics Database 👍 199 👎 68


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select round(min(sqrt(power(p1.x-p2.x,2)+power(p1.y-p2.y,2))),2) shortest
from point2d as p1
join point2d as p2
on p1.x!=p2.x or p1.y!=p2.y
#leetcode submit region end(Prohibit modification and deletion)
