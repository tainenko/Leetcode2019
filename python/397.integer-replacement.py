#
# @lc app=leetcode id=397 lang=python
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (31.74%)
# Likes:    283
# Dislikes: 278
# Total Accepted:    48.1K
# Total Submissions: 149.1K
# Testcase Example:  '8'
#
# 
# Given a positive integer n and you can do operations as follow:
# 
# 
# 
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# 
# 
# 
# 
# What is the minimum number of replacements needed for n to become 1?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# 8
# 
# Output:
# 3
# 
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# 
# 
# Example 2:
# 
# Input:
# 7
# 
# Output:
# 4
# 
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# 
#

# @lc code=start
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解題思路
        # 如果是奇數，把奇數變成四的倍數後變1的步驟會減少，唯有3是例外(3-1後的步驟比3+1更少)
        # 因此我們首先判斷n是奇數或偶數，如果n是奇數，且末兩位是'11'則加一，其餘的情況直接減一
        # 為了加速運算，我們可以用binary operation
        cnt=0
        while n>1:
            cnt+=1
            if n&1:
                if n&2 and n!=3:
                    n+=1
                else:
                    n-=1
            else:
                n>>=1
        return cnt

    def integerReplacement_recursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n, 0)

    def helper(self, n, cnt):
        if n == 1:
            return cnt
        if n % 2 == 0:
            return self.helper(n // 2, cnt + 1)
        return min(self.helper(n + 1, cnt + 1), self.helper(n - 1, cnt + 1))

# @lc code=end
