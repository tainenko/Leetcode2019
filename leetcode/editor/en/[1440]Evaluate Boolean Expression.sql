#Table Variables: 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| name          | varchar |
#| value         | int     |
#+---------------+---------+
#name is the primary key for this table.
#This table contains the stored variables and their values.
# 
#
# 
#
# Table Expressions: 
#
# 
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| left_operand  | varchar |
#| operator      | enum    |
#| right_operand | varchar |
#+---------------+---------+
#(left_operand, operator, right_operand) is the primary key for this table.
#This table contains a boolean expression that should be evaluated.
#operator is an enum that takes one of the values ('<', '>', '=')
#The values of left_operand and right_operand are guaranteed to be in the 
#Variables table.
# 
#
# 
#
# Write an SQL query to evaluate the boolean expressions in Expressions table. 
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
#Variables table:
#+------+-------+
#| name | value |
#+------+-------+
#| x    | 66    |
#| y    | 77    |
#+------+-------+
#Expressions table:
#+--------------+----------+---------------+
#| left_operand | operator | right_operand |
#+--------------+----------+---------------+
#| x            | >        | y             |
#| x            | <        | y             |
#| x            | =        | y             |
#| y            | >        | x             |
#| y            | <        | x             |
#| x            | =        | x             |
#+--------------+----------+---------------+
#Output: 
#+--------------+----------+---------------+-------+
#| left_operand | operator | right_operand | value |
#+--------------+----------+---------------+-------+
#| x            | >        | y             | false |
#| x            | <        | y             | true  |
#| x            | =        | y             | false |
#| y            | >        | x             | true  |
#| y            | <        | x             | false |
#| x            | =        | x             | true  |
#+--------------+----------+---------------+-------+
#Explanation: 
#As shown, you need to find the value of each boolean expression in the table 
#using the variables table.
# 
#
# Related Topics Database 👍 190 👎 12


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below

#leetcode submit region end(Prohibit modification and deletion)
