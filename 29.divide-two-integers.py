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
        count = 0
        while divisor * (count + 1) < dividend:
            count += 1
        return count
