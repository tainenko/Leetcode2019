'''
[821] Shortest Distance to a Character

https://leetcode.com/problems/shortest-distance-to-a-character/description/

* algorithms
* Easy (63.69%)
* Source Code:       821.shortest-distance-to-a-character.py
* Total Accepted:    39.9K
* Total Submissions: 62.5K
* Testcase Example:  '"loveleetcode"\n"e"'

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:


Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


 

Note:


        S string length is in [1, 10000].
        C is a single character, and guaranteed to be in string S.
        All letters in S and C are lowercase.

'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        lst = [None]*len(S)
        targets=[]
        for i in range(len(S)):
            if S[i]==C:
                targets.append(i)
        for i in range(len(S)):
            if i in targets:
                lst[i]=0
            else:
                lst[i]=min([abs(i-x) for x in targets])
        return lst

        
