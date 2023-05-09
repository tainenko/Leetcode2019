#Table: Views 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| article_id    | int     |
#| author_id     | int     |
#| viewer_id     | int     |
#| view_date     | date    |
#+---------------+---------+
#There is no primary key for this table, it may have duplicate rows.
#Each row of this table indicates that some viewer viewed an article (written 
#by some author) on some date. 
#Note that equal author_id and viewer_id indicate the same person. 
#
# 
#
# Write an SQL query to find all the people who viewed more than one article on 
#the same date. 
#
# Return the result table sorted by id in ascending order. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Views table:
#+------------+-----------+-----------+------------+
#| article_id | author_id | viewer_id | view_date  |
#+------------+-----------+-----------+------------+
#| 1          | 3         | 5         | 2019-08-01 |
#| 3          | 4         | 5         | 2019-08-01 |
#| 1          | 3         | 6         | 2019-08-02 |
#| 2          | 7         | 7         | 2019-08-01 |
#| 2          | 7         | 6         | 2019-08-02 |
#| 4          | 7         | 1         | 2019-07-22 |
#| 3          | 4         | 4         | 2019-07-21 |
#| 3          | 4         | 4         | 2019-07-21 |
#+------------+-----------+-----------+------------+
#Output: 
#+------+
#| id   |
#+------+
#| 5    |
#| 6    |
#+------+
# 
#
# Related Topics Database 👍 118 👎 27


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below

#leetcode submit region end(Prohibit modification and deletion)
