#
# @lc app=leetcode id=386 lang=python
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (47.32%)
# Likes:    470
# Dislikes: 65
# Total Accepted:    47.7K
# Total Submissions: 97.2K
# Testcase Example:  '13'
#
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#

# @lc code=start
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[x for x in range(1,n+1)]
        res=sorted(res,key=lambda x:str(x))
        return res
        
# @lc code=end
