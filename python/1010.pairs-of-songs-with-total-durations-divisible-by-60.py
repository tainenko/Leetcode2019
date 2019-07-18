'''
[1010] Pairs of Songs With Total Durations Divisible by 60

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

* algorithms
* Easy (45.66%)
* Source Code:       1010.pairs-of-songs-with-total-durations-divisible-by-60.py
* Total Accepted:    13.5K
* Total Submissions: 29.5K
* Testcase Example:  '[30,20,150,100,40]'

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:


Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60



Example 2:


Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.



 

Note:


        1 <= time.length <= 60000
        1 <= time[i] <= 500
'''
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        total=0
        dct = {}
        for i in range(len(time)-1,-1,-1):
            tmp = time[i]%60
            if tmp == 0 and dct.get(tmp,None):
                total+=dct[tmp]
            elif dct.get(60-tmp,None):
                total+=dct[60-tmp]
            dct[tmp]=dct.get(tmp,0)+1
        return total

    def numPairsDivisibleBy60_bruce_force(self, time):
        """
        exceed time limit
        :type time: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if (time[i]+time[j])%60==0:
                    total+=1
        return total

        
