#Table: Products 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| product_id    | int     |
#| new_price     | int     |
#| change_date   | date    |
#+---------------+---------+
#(product_id, change_date) is the primary key of this table.
#Each row of this table indicates that the price of some product was changed to 
#a new price at some date. 
#
# 
#
# Write an SQL query to find the prices of all products on 2019-08-16. Assume 
#the price of all products before any change is 10. 
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
#Products table:
#+------------+-----------+-------------+
#| product_id | new_price | change_date |
#+------------+-----------+-------------+
#| 1          | 20        | 2019-08-14  |
#| 2          | 50        | 2019-08-14  |
#| 1          | 30        | 2019-08-15  |
#| 1          | 35        | 2019-08-16  |
#| 2          | 65        | 2019-08-17  |
#| 3          | 20        | 2019-08-18  |
#+------------+-----------+-------------+
#Output: 
#+------------+-------+
#| product_id | price |
#+------------+-------+
#| 2          | 50    |
#| 1          | 35    |
#| 3          | 10    |
#+------------+-------+
# 
#
# Related Topics Database 👍 367 👎 103


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
with prices as (
    select product_id, new_price price, rank() over (partition by product_id order by change_date desc) rank_num
    from products
    where change_date<='2019-08-16'
)

select tmp.product_id, coalesce(price,10) price
from (select distinct(product_id) product_id from products) tmp
left join prices on prices.product_id = tmp.product_id and prices.rank_num=1
#leetcode submit region end(Prohibit modification and deletion)
