'''
[994] Rotting Oranges

https://leetcode.com/problems/rotting-oranges/description/

* algorithms
* Easy (46.47%)
* Source Code:       994.rotting-oranges.py
* Total Accepted:    14.1K
* Total Submissions: 30.4K
* Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'

In a given grid, each cell can have one of three values:


        the value 0 representing an empty cell;
        the value 1 representing a fresh orange;
        the value 2 representing a rotten orange.


Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 


Example 1:




Input: [
[2,1,1],
[1,1,0],
[0,1,1]]
Output: 4



Example 2:


Input: [
[2,1,1],
[0,1,1],
[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.



Example 3:


Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


 

Note:


        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        grid[i][j] is only 0, 1, or 2.

'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i = len(grid)
        j = len(grid[0])
        fresh=0
        q=[]
        for x in range(i):
            for y in range(j):
                if grid[x][y]==1:
                    fresh+=1
                if grid[x][y]==2:
                    q.append((x,y,0))
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        res=0
        while q:
            x,y,c=q.pop(0)
            for row,col in direction:
                if i>x+row>=0 and j>y+col>=0 and grid[x+row][y+col]==1:
                    q.append((x+row,y+col,c+1))
                    res=max(res,c+1)
                    grid[x+row][y+col]=2
                    fresh-=1
        if fresh!=0:
            return -1
        return res

        
