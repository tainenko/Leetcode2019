"""
[1016] Binary String With Substrings Representing 1 To N

https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/description/

* algorithms
* Medium (60.45%)
* Source Code:       1016.binary-string-with-substrings-representing-1-to-n.py
* Total Accepted:    7.4K
* Total Submissions: 12.3K
* Testcase Example:  '"0110"\n3'

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:


Input: S = "0110", N = 3
Output: true


Example 2:


Input: S = "0110", N = 4
Output: false


 

Note:


        1 <= S.length <= 1000
        1 <= N <= 10^9

"""
class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        
