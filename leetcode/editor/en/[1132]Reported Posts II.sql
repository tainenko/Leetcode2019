#Table
: Actions
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| post_id       | int     |
#| action_date   | date    | 
#| action        | enum    |
#| extra         | varchar |
#+---------------+---------+
#There is no primary key for this table, it may have duplicate rows.
#The action column is an ENUM type of ('view', 'like', 'reaction', 'comment', 
#'report', 'share').
#The extra column has optional information about the action, such as a reason 
#for the report or a type of reaction.
# 
#
# 
#
# Table: Removals 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| post_id       | int     |
#| remove_date   | date    | 
#+---------------+---------+
#post_id is the primary key of this table.
#Each row in this table indicates that some post was removed due to being 
#reported or as a result of an admin review.
# 
#
# 
#
# Write an SQL query to find the average daily percentage of posts that got 
#removed after being reported as spam, rounded to 2 decimal places. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Actions table:
#+---------+---------+-------------+--------+--------+
#| user_id | post_id | action_date | action | extra  |
#+---------+---------+-------------+--------+--------+
#| 1       | 1       | 2019-07-01  | view   | null   |
#| 1       | 1       | 2019-07-01  | like   | null   |
#| 1       | 1       | 2019-07-01  | share  | null   |
#| 2       | 2       | 2019-07-04  | view   | null   |
#| 2       | 2       | 2019-07-04  | report | spam   |
#| 3       | 4       | 2019-07-04  | view   | null   |
#| 3       | 4       | 2019-07-04  | report | spam   |
#| 4       | 3       | 2019-07-02  | view   | null   |
#| 4       | 3       | 2019-07-02  | report | spam   |
#| 5       | 2       | 2019-07-03  | view   | null   |
#| 5       | 2       | 2019-07-03  | report | racism |
#| 5       | 5       | 2019-07-03  | view   | null   |
#| 5       | 5       | 2019-07-03  | report | racism |
#+---------+---------+-------------+--------+--------+
#Removals table:
#+---------+-------------+
#| post_id | remove_date |
#+---------+-------------+
#| 2       | 2019-07-20  |
#| 3       | 2019-07-18  |
#+---------+-------------+
#Output: 
#+-----------------------+
#| average_daily_percent |
#+-----------------------+
#| 75.00                 |
#+-----------------------+
#Explanation: 
#The percentage for 2019-07-04 is 50% because only one post of two spam 
#reported posts were removed.
#The percentage for 2019-07-02 is 100% because one post was reported as spam 
#and it was removed.
#The other days had no spam reports so the average is (50 + 100) / 2 = 75%
#Note that the output is only one number and that we do not care about the 
#remove dates.
# 
#
# Related Topics Database
👍 139
👎 521


#leetcode submit region
begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select round(sum(remove_count / post_count) / count(*) * 100, 2) average_daily_percent
from (select count(distinct removals.post_id) remove_count, count(distinct actions.post_id) post_count
      from actions
               left join removals on removals.post_id = actions.post_id
      where actions.extra = "spam"
      group by actions.action_date) tmp #leetcode submit region
end(Prohibit modification and deletion)
