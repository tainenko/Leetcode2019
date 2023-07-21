#Table: Relations 
#
# 
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| user_id     | int  |
#| follower_id | int  |
#+-------------+------+
#(user_id, follower_id) is the primary key for this table.
#Each row of this table indicates that the user with ID follower_id is 
#following the user with ID user_id.
# 
#
# 
#
# Write an SQL query to find all the pairs of users with the maximum number of 
#common followers. In other words, if the maximum number of common followers 
#between any two users is maxCommon, then you have to return all pairs of users that 
#have maxCommon common followers. 
#
# The result table should contain the pairs user1_id and user2_id where user1_
#id < user2_id. 
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
#Relations table:
#+---------+-------------+
#| user_id | follower_id |
#+---------+-------------+
#| 1       | 3           |
#| 2       | 3           |
#| 7       | 3           |
#| 1       | 4           |
#| 2       | 4           |
#| 7       | 4           |
#| 1       | 5           |
#| 2       | 6           |
#| 7       | 5           |
#+---------+-------------+
#Output: 
#+----------+----------+
#| user1_id | user2_id |
#+----------+----------+
#| 1        | 7        |
#+----------+----------+
#Explanation: 
#Users 1 and 2 have two common followers (3 and 4).
#Users 1 and 7 have three common followers (3, 4, and 5).
#Users 2 and 7 have two common followers (3 and 4).
#Since the maximum number of common followers between any two users is 3, we 
#return all pairs of users with three common followers, which is only the pair (1, 7
#). We return the pair as (1, 7), not as (7, 1).
#Note that we do not have any information about the users that follow users 3, 4
#, and 5, so we consider them to have 0 followers.
# 
#
# Related Topics Database 👍 84 👎 6


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below

#leetcode submit region end(Prohibit modification and deletion)
