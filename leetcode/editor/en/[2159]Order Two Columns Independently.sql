#Table: Data 
#
# 
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| first_col   | int  |
#| second_col  | int  |
#+-------------+------+
#There is no primary key for this table and it may contain duplicates.
# 
#
# 
#
# Write an SQL query to independently: 
#
# 
# order first_col in ascending order. 
# order second_col in descending order. 
# 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Data table:
#+-----------+------------+
#| first_col | second_col |
#+-----------+------------+
#| 4         | 2          |
#| 2         | 3          |
#| 3         | 1          |
#| 1         | 4          |
#+-----------+------------+
#Output: 
#+-----------+------------+
#| first_col | second_col |
#+-----------+------------+
#| 1         | 4          |
#| 2         | 3          |
#| 3         | 2          |
#| 4         | 1          |
#+-----------+------------+
# 
#
# Related Topics Database 👍 60 👎 15


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
with cte as(
    select first_col,
    second_col,
     row_number() over( order by first_col asc) r_num1,
     row_number() over (order by second_col desc) r_num2
    from data
    )
select c1.first_col, c2.second_col
from cte c1
join cte c2
on c1.r_num1=c2.r_num2
order by c1.first_col, c2.second_col desc
