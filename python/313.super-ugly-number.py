#
# @lc app=leetcode id=313 lang=python
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (42.24%)
# Likes:    448
# Dislikes: 113
# Total Accepted:    67.4K
# Total Submissions: 156.5K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the n^th super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
# 
# Example:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:
# 
# 
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
# The n^th super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# 
#

# @lc code=start
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        candidate = [1] * len(primes)
        ids = [0] * len(primes)
        next_min = 1
        for _ in range(1, n):
            for i in range(len(primes)):
                if next_min == candidate[i]:
                    candidate[i] = uglies[ids[i]] * primes[i]
                    ids[i] += 1
            next_min = min(candidate)
            uglies.append(next_min)
        return uglies[-1]

# @lc code=end
