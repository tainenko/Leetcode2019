#Table: Traffic 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| activity      | enum    |
#| activity_date | date    |
#+---------------+---------+
#There is no primary key for this table, it may have duplicate rows.
#The activity column is an ENUM type of ('login', 'logout', 'jobs', 'groups', 
#'homepage').
# 
#
# 
#
# Write an SQL query to reports for every date within at most 90 days from 
#today, the number of users that logged in for the first time on that date. Assume 
#today is 2019-06-30. 
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
#Traffic table:
#+---------+----------+---------------+
#| user_id | activity | activity_date |
#+---------+----------+---------------+
#| 1       | login    | 2019-05-01    |
#| 1       | homepage | 2019-05-01    |
#| 1       | logout   | 2019-05-01    |
#| 2       | login    | 2019-06-21    |
#| 2       | logout   | 2019-06-21    |
#| 3       | login    | 2019-01-01    |
#| 3       | jobs     | 2019-01-01    |
#| 3       | logout   | 2019-01-01    |
#| 4       | login    | 2019-06-21    |
#| 4       | groups   | 2019-06-21    |
#| 4       | logout   | 2019-06-21    |
#| 5       | login    | 2019-03-01    |
#| 5       | logout   | 2019-03-01    |
#| 5       | login    | 2019-06-21    |
#| 5       | logout   | 2019-06-21    |
#+---------+----------+---------------+
#Output: 
#+------------+-------------+
#| login_date | user_count  |
#+------------+-------------+
#| 2019-05-01 | 1           |
#| 2019-06-21 | 2           |
#+------------+-------------+
#Explanation: 
#Note that we only care about dates with non zero user count.
#The user with id 5 first logged in on 2019-03-01 so he's not counted on 2019-06
#-21.
# 
#
# Related Topics Database 👍 134 👎 147


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select login_date, count(login_date) user_count
from (select user_id, min(activity_date) login_date from traffic where activity='login' group by user_id) tmp
where login_date >= '2019-06-30'- interval 90 day
group by login_date
order by login_date
#leetcode submit region end(Prohibit modification and deletion)
