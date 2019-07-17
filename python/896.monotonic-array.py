'''
[896] Monotonic Array

https://leetcode.com/problems/monotonic-array/description/

* algorithms
* Easy (55.40%)
* Source Code:       896.monotonic-array.py
* Total Accepted:    47.8K
* Total Submissions: 86.4K
* Testcase Example:  '[1,2,2,3]'

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 





Example 1:


Input: [1,2,2,3]
Output: true



Example 2:


Input: [6,5,4,4]
Output: true



Example 3:


Input: [1,3,2]
Output: false



Example 4:


Input: [1,2,4,5]
Output: true



Example 5:


Input: [1,1,1]
Output: true


 

Note:


        1 <= A.length <= 50000
        -100000 <= A[i] <= 100000

'''
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def increase(A):
            for i in range(1, len(A)):
                if A[i] > A[i - 1]:
                    return False
            return True

        def decrease(A):
            for i in range(1, len(A)):
                if A[i] < A[i - 1]:
                    return False
            return True
        return increase(A) or decrease(A)

    def isMonotonic2(self,A):
        """
        :param A:
        :return:
        """
        inc = True
        dec = True
        for i in range(1,len(A)):
            inc = inc and A[i-1]<=A[i]
            dec = dec and A[i-1]>=A[i]
        return inc or dec




        
