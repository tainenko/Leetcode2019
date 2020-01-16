--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--
-- https://leetcode.com/problems/consecutive-numbers/description/
--
-- database
-- Medium (34.66%)
-- Likes:    324
-- Dislikes: 84
-- Total Accepted:    71.9K
-- Total Submissions: 195.7K
-- Testcase Example:  '{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}'
--
-- Write a SQL query to find all numbers that appear at least three times
-- consecutively.
-- 
-- 
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- 
-- 
-- For example, given the above Logs table, 1 is the only number that appears
-- consecutively for at least three times.
-- 
-- 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT L1.Num as ConsecutiveNums
FROM Logs as L1
JOIN Logs as L2
ON L1.Id=L2.Id-1
JOIN Logs as L3
ON L2.Id=L3.Id-1
WHERE L1.Num=L2.Num
AND L1.Num=L3.Num

-- @lc code=end
