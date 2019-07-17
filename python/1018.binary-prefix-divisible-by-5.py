'''
[1018] Binary Prefix Divisible By 5

https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

* algorithms
* Easy (46.60%)
* Source Code:       1018.binary-prefix-divisible-by-5.py
* Total Accepted:    11.4K
* Total Submissions: 24.5K
* Testcase Example:  '[0,1,1]'

Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:


Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.


Example 2:


Input: [1,1,1]
Output: [false,false,false]


Example 3:


Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]


Example 4:


Input: [1,1,1,0,1]
Output: [false,false,false,false,false]


 

Note:


        1 <= A.length <= 30000
        A[i] is 0 or 1

'''
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        prefix=0
        res=[]
        for a in A:
            prefix = (2*prefix+a) % 5
            res.append(prefix==0)
        return res


    def prefixesDivBy5_2(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        num=""
        res=[]
        for bit in A:
            num+=str(bit)
            if int(num,2) % 5 ==0:
                res.append(True)
            else:
                res.append(False)
        return res
