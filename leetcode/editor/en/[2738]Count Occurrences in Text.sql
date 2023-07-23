#Table: Files 
#
# 
#+-------------+---------+
#| Column Name | Type    |
#+-- ----------+---------+
#| file_name   | varchar |
#| content     | text    |
#+-------------+---------+
#file_name is the primary key of this table. 
#Each row contains file_name and the content of that file.
# 
#
# Write an SQL query to find the number of occurrences of the words 'bull' and 
#'bear' as a standalone word, disregarding any instances where it appears as part 
#of another word (e.g. 'bullet' and 'bears' will not be considered). 
#
# Return the word 'bull' and 'bear' along with the corresponding number of 
#occurrences in any order. 
#
# The query result format is in the following example. 
#
# 
# Example 1: 
#
# 
#Input: 
#Files table:
#+------------+-----------------------------------------------------------------
#-----------------+
#| file_name  | contenet                                                        
#                 | 
#+------------+-----------------------------------------------------------------
#-----------------+
#| draft1.txt | The stock exchange predicts a bull market which would make many 
#investors happy. | 
#| draft2.txt | The stock exchange predicts a bull market which would make many 
#investors happy, |
#|            | but analysts warn of possibility of too much optimism and that 
#in fact we are    |
#|            | awaiting a bear market.                                         
#                 | 
#| draft3.txt | The stock exchange predicts a bull market which would make many 
#investors happy, |
#|            | but analysts warn of possibility of too much optimism and that 
#in fact we are    |
#|            | awaiting a bear market. As always predicting the future market 
#is an uncertain   |
#|            | game and all investors should follow their instincts and best 
#practices.         | 
#+------------+-----------------------------------------------------------------
#-----------------+
#Output: 
#+------+-------+
#| word | count |  
#+------+-------+
#| bull | 3     | 
#| bear | 2     | 
#+------+-------+
#Explanation: 
#- The word "bull" appears 1 time in "draft1.txt", 1 time in "draft2.txt", and 1
# time in "draft3.txt". Therefore, the total number of occurrences for the word 
#"bull" is 3.
#- The word "bear" appears 1 time in "draft2.txt", and 1 time in "draft3.txt". 
#Therefore, the total number of occurrences for the word "bear" is 2.
#
# 
#
# Related Topics Database 👍 7 👎 16


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below
select 'bull' as word, count(*) as count
from files
where content like '% bull %'
union all
select 'bear' as word, count(*) as count
from files
where content like '% bear %'
#leetcode submit region end(Prohibit modification and deletion)
