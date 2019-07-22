'''
[976] Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/description/

* algorithms
* Easy (57.11%)
* Source Code:       976.largest-perimeter-triangle.py
* Total Accepted:    18K
* Total Submissions: 31.5K
* Testcase Example:  '[2,1,2]'

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 





Example 1:


Input: [2,1,2]
Output: 5



Example 2:


Input: [1,2,1]
Output: 0



Example 3:


Input: [3,2,3,4]
Output: 10



Example 4:


Input: [3,6,2,3]
Output: 8


 

Note:


        3 <= A.length <= 10000
        1 <= A[i] <= 10^6

'''
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        解題思路：
        三角形的構成條件為兩邊之和大於第三邊。
        先對list排序，考慮無法形成三角形的情景為 A[i]>=A[i-1]+A[i-2]，由於list為有序，A[i-2]>=A[i-3]，
        因此A[i]>=A[i-1]+A[i-3]，同理可証A[i]與剩下的邊長都無法構成三角形。
        因此我們想找到一個最長周長的三角形，必定是取連續三個周長，判斷是否符合兩邊和大於第三邊的條件。
        """
        A.sort()
        N=len(A)
        for i in range(N-1,1,-1):
            if A[i-1]+A[i-2]>A[i]:
                return A[i-1]+A[i-2]+A[i]
        return 0

        
