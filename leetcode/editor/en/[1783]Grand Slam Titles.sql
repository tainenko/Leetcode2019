#Table: Players 
#
# 
#+----------------+---------+
#| Column Name    | Type    |
#+----------------+---------+
#| player_id      | int     |
#| player_name    | varchar |
#+----------------+---------+
#player_id is the primary key for this table.
#Each row in this table contains the name and the ID of a tennis player.
# 
#
# 
#
# Table: Championships 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| year          | int     |
#| Wimbledon     | int     |
#| Fr_open       | int     |
#| US_open       | int     |
#| Au_open       | int     |
#+---------------+---------+
#year is the primary key for this table.
#Each row of this table contains the IDs of the players who won one each tennis 
#tournament of the grand slam.
# 
#
# 
#
# Write an SQL query to report the number of grand slam tournaments won by each 
#player. Do not include the players who did not win any tournament. 
#
# Return the result table in any order. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Players table:
#+-----------+-------------+
#| player_id | player_name |
#+-----------+-------------+
#| 1         | Nadal       |
#| 2         | Federer     |
#| 3         | Novak       |
#+-----------+-------------+
#Championships table:
#+------+-----------+---------+---------+---------+
#| year | Wimbledon | Fr_open | US_open | Au_open |
#+------+-----------+---------+---------+---------+
#| 2018 | 1         | 1       | 1       | 1       |
#| 2019 | 1         | 1       | 2       | 2       |
#| 2020 | 2         | 1       | 2       | 2       |
#+------+-----------+---------+---------+---------+
#Output: 
#+-----------+-------------+-------------------+
#| player_id | player_name | grand_slams_count |
#+-----------+-------------+-------------------+
#| 2         | Federer     | 5                 |
#| 1         | Nadal       | 7                 |
#+-----------+-------------+-------------------+
#Explanation: 
#Player 1 (Nadal) won 7 titles: Wimbledon (2018, 2019), Fr_open (2018, 2019, 202
#0), US_open (2018), and Au_open (2018).
#Player 2 (Federer) won 5 titles: Wimbledon (2020), US_open (2019, 2020), and 
#Au_open (2019, 2020).
#Player 3 (Novak) did not win anything, we did not include them in the result 
#table.
# 
#
# Related Topics Database 👍 205 👎 6
#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
with cte as(
    select year, Wimbledon as player_id
    from championships
    union all
    select year, fr_open as player_id
    from championships
    union all
    select year, us_open as player_id
    from championships
    union all
    select year, au_open as player_id
    from championships
)

select players.player_id, players.player_name, count(players.player_id) as grand_slams_count
from players join cte on players.player_id = cte.player_id
group by players.player_id

#leetcode submit region end(Prohibit modification and deletion)
