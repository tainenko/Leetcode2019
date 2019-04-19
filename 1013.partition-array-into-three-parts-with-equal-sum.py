'''
[1013] Partition Array Into Three Parts With Equal Sum

https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

* algorithms
* Easy (53.33%)
* Source Code:       1013.partition-array-into-three-parts-with-equal-sum.js
* Total Accepted:    9.1K
* Total Submissions: 16.7K
* Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:


Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1



Example 2:


Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false



Example 3:


Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4




 

Note:


        3 <= A.length <= 50000
        -10000 <= A[i] <= 10000

'''
class Solution(object):
    def canThreePartsEqualSum2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 解題思路
        # 兩個指標從前後開始掃，如果Sum of left和Sum of right不相等就移動指標，直接左右的Sum一樣
        # 最後再檢查中間的Sum是否和左右一樣
        # 問題：
        # 沒有目標值，並且Array裡頭有正有負，依照左右的Sum比較結果去決定哪個指標需要移動不合理。
        left=0
        right=len(A)-1
        Sl=A[left]
        Sr=A[right]
        while left<right:
            if Sl==Sr:
                break
            elif Sl<Sr:
                left+=1
                Sl+=A[left]
            else:
                right-=1
                Sr+=A[right]
        return True if Sl==Sr==sum(A[left+1:right]) else False
    def canThreePartsEqualSum(self, A):
        # 解題思路2
        # 先求Sum(A)，則partial Array Sum應為Sum(A)//3
        # 求到目標值後停下
        if sum(A)%3:
            return False
        target=sum(A)//3
        left=0
        right=len(A)-1
        Sl=A[left]
        Sr=A[right]
        while left<right:
            if Sl!=target:
                left+=1
                Sl+=A[left]
            if Sr!=target:
                right-=1
                Sr+=A[right]
            if Sr==Sl==target:
                break
        return True if Sl==Sr else False

        
