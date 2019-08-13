'''
[29] Divide Two Integers

https://leetcode.com/problems/divide-two-integers/description/

* algorithms
* Medium (16.15%)
* Source Code:       29.divide-two-integers.py
* Total Accepted:    200.1K
* Total Submissions: 1.2M
* Testcase Example:  '10\n3'

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:


Input: dividend = 10, divisor = 3
Output: 3

Example 2:


Input: dividend = 7, divisor = -3
Output: -2

Note:


        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if dividend==0:
            return 0
        if dividend ==MAX_INT and divisor==(-1):
            return MAX_INT
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            sign=-1
        else:
            sign=1
        dividend = abs(dividend)
        divisor=abs(divisor)
        res=0
        while dividend>=divisor:
            shift=0
            tmp=divisor
            while dividend>=tmp:
                dividend-=tmp
                res+=1<<shift
                shift += 1
                tmp <<= 1
        res*=sign
        if res>MAX_INT:
            return MAX_INT
        return res


