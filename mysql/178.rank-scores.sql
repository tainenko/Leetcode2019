--
-- @lc app=leetcode id=178 lang=mysql
--
-- [178] Rank Scores
--
-- https://leetcode.com/problems/rank-scores/description/
--
-- database
-- Medium (37.90%)
-- Likes:    617
-- Dislikes: 98
-- Total Accepted:    86.2K
-- Total Submissions: 208.7K
-- Testcase Example:  '{"headers": {"Scores": ["Id", "Score"]}, "rows": {"Scores": [[1, 3.50], [2, 3.65], [3, 4.00], [4, 3.85], [5, 4.00], [6, 3.65]]}}'
--
-- Write a SQL query to rank scores. If there is a tie between two scores, both
-- should have the same ranking. Note that after a tie, the next ranking number
-- should be the next consecutive integer value. In other words, there should
-- be no "holes" between ranks.
-- 
-- 
-- +----+-------+
-- | Id | Score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+
-- 
-- 
-- For example, given the above Scores table, your query should generate the
-- following report (order by highest score):
-- 
-- 
-- +-------+------+
-- | Score | Rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Score,
(SELECT COUNT(*) FROM (SELECT DISTINCT Score s FROM Scores)t WHERE s>=Score) Rank
FROM Scores
ORDER BY Score DESC

-- @lc code=end
