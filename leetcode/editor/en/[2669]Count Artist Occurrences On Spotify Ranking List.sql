#Table: Spotify 
#
# 
#+-------------+---------+ 
#| Column Name | Type    | 
#+-------------+---------+ 
#| id          | int     | 
#| track_name  | varchar |
#| artist      | varchar |
#+-------------+---------+
#id is the primary Key for this table.
#Each row contains an id, track_name, and artist.
# 
#
# Write an SQL query to find how many times each artist appeared on the spotify 
#ranking list. 
#
# Return the result table having the artist's name along with the corresponding 
#number of occurrences ordered by occurrence count in descending order. If the 
#occurrences are equal, then it’s ordered by the artist’s name in ascending order. 
#
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input:
#Spotify table: 
#+---------+--------------------+------------+ 
#| id      | track_name         | artist     |  
#+---------+--------------------+------------+
#| 303651  | Heart Won't Forget | Sia        |
#| 1046089 | Shape of you       | Ed Sheeran |
#| 33445   | I'm the one        | DJ Khalid  |
#| 811266  | Young Dumb & Broke | DJ Khalid  | 
#| 505727  | Happier            | Ed Sheeran |
#+---------+--------------------+------------+ 
#Output:
#+------------+-------------+
#| artist     | occurrences | 
#+------------+-------------+
#| DJ Khalid  | 2           |
#| Ed Sheeran | 2           |
#| Sia        | 1           | 
#+------------+-------------+ 
#
#Explanation: The count of occurrences is listed in descending order under the 
#column name "occurrences". If the number of occurrences is the same, the 
#artist's names are sorted in ascending order.
# 
#
# 👍 5 👎 0


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select artist, count(artist) occurrences
from spotify
group by artist
order by occurrences desc, artist
#leetcode submit region end(Prohibit modification and deletion)
