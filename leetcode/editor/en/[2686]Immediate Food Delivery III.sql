#Table: Delivery 
#
# 
#+-----------------------------+---------+
#| Column Name                 | Type    |
#+-----------------------------+---------+
#| delivery_id                 | int     |
#| customer_id                 | int     |
#| order_date                  | date    |
#| customer_pref_delivery_date | date    |
#+-----------------------------+---------+
#delivery_id is the primary key of this table.
#Each row contains information about food delivery to a customer that makes an 
#order at some date and specifies a preferred delivery date (on the order date or 
#after it).
# 
#
# If the customer's preferred delivery date is the same as the order date, then 
#the order is called immediate, otherwise, it is scheduled. 
#
# Write an SQL query to find the percentage of immediate orders on each unique 
#order_date, rounded to 2 decimal places. 
#
# Return the result table ordered by order_date in ascending order. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Delivery table:
#+-------------+-------------+------------+-----------------------------+
#| delivery_id | customer_id | order_date | customer_pref_delivery_date |
#+-------------+-------------+------------+-----------------------------+
#| 1           | 1           | 2019-08-01 | 2019-08-02                  |
#| 2           | 2           | 2019-08-01 | 2019-08-01                  |
#| 3           | 1           | 2019-08-01 | 2019-08-01                  |
#| 4           | 3           | 2019-08-02 | 2019-08-13                  |
#| 5           | 3           | 2019-08-02 | 2019-08-02                  |
#| 6           | 2           | 2019-08-02 | 2019-08-02                  |
#| 7           | 4           | 2019-08-03 | 2019-08-03                  |
#| 8           | 1           | 2019-08-03 | 2019-08-03                  |
#| 9           | 5           | 2019-08-04 | 2019-08-08                  |
#| 10          | 2           | 2019-08-04 | 2019-08-18                  |
#+-------------+-------------+------------+-----------------------------+
#Output: 
#+------------+----------------------+
#| order_date | immediate_percentage |
#+------------+----------------------+
#| 2019-08-01 | 66.67                |
#| 2019-08-02 | 66.67                |
#| 2019-08-03 | 100.00               |
#| 2019-08-04 | 0.00                 |
#+------------+----------------------+
#Explanation: 
#- On 2019-08-01 there were three orders, out of those, two were immediate and 
#one was scheduled. So, immediate percentage for that date was 66.67.
#- On 2019-08-02 there were three orders, out of those, two were immediate and 
#one was scheduled. So, immediate percentage for that date was 66.67.
#- On 2019-08-03 there were two orders, both were immediate. So, the immediate 
#percentage for that date was 100.00.
#- On 2019-08-04 there were two orders, both were scheduled. So, the immediate 
#percentage for that date was 0.00.
#order_date is sorted in ascending order.
# 
#
# Related Topics Database 👍 7 👎 0


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select order_date, round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)/count(order_date)*100,2) as immediate_percentage
from Delivery
group by order_date
order by order_date
#leetcode submit region end(Prohibit modification and deletion)
