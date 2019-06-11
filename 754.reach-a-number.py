'''
[754] Reach a Number

https://leetcode.com/problems/reach-a-number/description/

* algorithms
* Easy (32.59%)
* Source Code:       754.reach-a-number.py
* Total Accepted:    10.5K
* Total Submissions: 32.1K
* Testcase Example:  '1'


You are standing at position 0 on an infinite number line.  There is a goal at position target.

On each move, you can either go left or right.  During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.


Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.



Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.



Note:
target will be a non-zero integer in the range [-10^9, 10^9].

'''
class Solution(object):
    def reachNumber(self,target):
        if target<0:
            target=(-target)
        n=0
        while n*(n+1)//2 < target:
            n+=1
        total = n * (n + 1) // 2
        if total == target:
            return n
        else:
            if (total-target)%2==0:
                return n
            else:
                if n%2==0:
                    return n+1
                else:
                    return n+2


    def reachNumber_trie(self, target):
        """
        create a binary to find out the target
        :type target: int
        :rtype: int
        """
        count=0
        q=[0]
        while q:
            count+=1
            next=[]
            while q:
                tmp=q.pop(0)
                left=tmp-count
                right=tmp+count
                if left==target or right==target:
                    return count
                next.append(left)
                next.append(right)
            q+=next
        
