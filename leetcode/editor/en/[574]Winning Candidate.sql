#Table: Candidate 
#
# 
#+-------------+----------+
#| Column Name | Type     |
#+-------------+----------+
#| id          | int      |
#| name        | varchar  |
#+-------------+----------+
#id is the primary key column for this table.
#Each row of this table contains information about the id and the name of a 
#candidate.
# 
#
# 
#
# Table: Vote 
#
# 
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| id          | int  |
#| candidateId | int  |
#+-------------+------+
#id is an auto-increment primary key.
#candidateId is a foreign key to id from the Candidate table.
#Each row of this table determines the candidate who got the iᵗʰ vote in the 
#elections.
# 
#
# 
#
# Write an SQL query to report the name of the winning candidate (i.e., the 
#candidate who got the largest number of votes). 
#
# The test cases are generated so that exactly one candidate wins the elections.
# 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Candidate table:
#+----+------+
#| id | name |
#+----+------+
#| 1  | A    |
#| 2  | B    |
#| 3  | C    |
#| 4  | D    |
#| 5  | E    |
#+----+------+
#Vote table:
#+----+-------------+
#| id | candidateId |
#+----+-------------+
#| 1  | 2           |
#| 2  | 4           |
#| 3  | 3           |
#| 4  | 2           |
#| 5  | 5           |
#+----+-------------+
#Output: 
#+------+
#| name |
#+------+
#| B    |
#+------+
#Explanation: 
#Candidate B has 2 votes. Candidates C, D, and E have 1 vote each.
#The winner is candidate B.
# 
#
# Related Topics Database 👍 156 👎 407


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select c.name
    from candidate as c
    join vote as v
    on v.candidateId=c.id
    group by c.id
    order by count(v.candidateId) desc
    limit 1
#leetcode submit region end(Prohibit modification and deletion)
