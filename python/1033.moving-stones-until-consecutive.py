'''
[1033] Moving Stones Until Consecutive

https://leetcode.com/problems/moving-stones-until-consecutive/description/

* algorithms
* Easy (35.77%)
* Source Code:       1033.moving-stones-until-consecutive.py
* Total Accepted:    6.2K
* Total Submissions: 17.3K
* Testcase Example:  '1\n2\n5'

Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints.  Formally, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

 

Example 1:


Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.



Example 2:


Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.



Example 3:


Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.


 



Note:


        1 <= a <= 100
        1 <= b <= 100
        1 <= c <= 100
        a != b, b != c, c != a
'''
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        a,b,c=sorted([a,b,c])
        min,max=0,0
        # there are three senarios in min step
        # the first one, all of them are already consecutive, we don't need to move.
        # the min step is zero
        if a+1==b and b+1==c:
            min=0
        # the second one, two of the nums are consecutive or they are difference by two.
        # we can move the third num to the consecutive positive or insert into the others.
        # the min step would be 1.
        elif b-a<=2 or c-b <=2:
            min=1
        # else, we need to move two of the nums.
        else:
            min=2
        # the max step is we move the lowest and highest position stone to the middle and move one step in a time.
        # the highest position need (c-b-1) steps. the lowest position need (b-a-1) steps.
        max=(c-b-1)+(b-a-1)
        return [min,max]

        
