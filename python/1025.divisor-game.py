'''
[1025] Divisor Game

https://leetcode.com/problems/divisor-game/description/

* algorithms
* Easy (63.60%)
* Source Code:       1025.divisor-game.py
* Total Accepted:    15K
* Total Submissions: 23.5K
* Testcase Example:  '2'

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:


        Choosing any x with 0 < x < N and N % x == 0.
        Replacing the number N on the chalkboard with N - x.


Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 





Example 1:


Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.



Example 2:


Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


 

Note:


        1 <= N <= 1000

'''
import math
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return False
        elif N == 2:
            return True
        elif N == 3:
            return False
        res = [False]*(N+1)
        res[2] = True
        res[3] = False
        for n in range(1,N+1):
            tmp=[]
            for x in range(1,int(math.sqrt(n))):
                if n%x == 0:
                    tmp.append(res[n-x])
            if all(tmp):
                res[n] = False
            else:
                res[n] = True
        return res[-1]
        
