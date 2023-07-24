#Table: Students 
#
# 
#+---------------+------+
#| Column Name   | Type |
#+---------------+------+
#| student_id    | int  |
#| department_id | int  |
#| mark          | int  |
#+---------------+------+
#student_id is the primary key of this table.
#Each row of this table indicates a student's ID, the ID of the department in 
#which the student enrolled, and their mark in the exam.
# 
#
# 
#
# Write an SQL query that reports the rank of each student in their department 
#as a percentage, where the rank as a percentage is computed using the following 
#formula: (student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_
#the_department - 1). The percentage should be rounded to 2 decimal places. 
#student_rank_in_the_department is determined by descending mark, such that the 
#student with the highest mark is rank 1. If two students get the same mark, they also 
#get the same rank. 
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
#Students table:
#+------------+---------------+------+
#| student_id | department_id | mark |
#+------------+---------------+------+
#| 2          | 2             | 650  |
#| 8          | 2             | 650  |
#| 7          | 1             | 920  |
#| 1          | 1             | 610  |
#| 3          | 1             | 530  |
#+------------+---------------+------+
#Output: 
#+------------+---------------+------------+
#| student_id | department_id | percentage |
#+------------+---------------+------------+
#| 7          | 1             | 0.0        |
#| 1          | 1             | 50.0       |
#| 3          | 1             | 100.0      |
#| 2          | 2             | 0.0        |
#| 8          | 2             | 0.0        |
#+------------+---------------+------------+
#Explanation: 
#For Department 1:
# - Student 7: percentage = (1 - 1) * 100 / (3 - 1) = 0.0
# - Student 1: percentage = (2 - 1) * 100 / (3 - 1) = 50.0
# - Student 3: percentage = (3 - 1) * 100 / (3 - 1) = 100.0
#For Department 2:
# - Student 2: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
# - Student 8: percentage = (1 - 1) * 100 / (2 - 1) = 0.0
# 
#
# Related Topics Database 👍 21 👎 61


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
with cte as(
    select student_id, department_id, rank() over (partition by department_id order by mark desc) rk
    from students
    )
    , cte2 as (
    select count(*) cnt, department_id
    from students
    group by department_id
    )
select s.student_id, s.department_id, COALESCE(round((c1.rk-1)*100/(c2.cnt -1),2),0) percentage
from students as s
join cte c1 on s.student_id=c1.student_id and s.department_id=c1.department_id
join cte2 c2 on s.department_id=c2.department_id
#leetcode submit region end(Prohibit modification and deletion)
