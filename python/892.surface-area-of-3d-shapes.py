'''
[892] Surface Area of 3D Shapes

https://leetcode.com/problems/surface-area-of-3d-shapes/description/

* algorithms
* Easy (56.19%)
* Source Code:       892.surface-area-of-3d-shapes.py
* Total Accepted:    11.9K
* Total Submissions: 21.2K
* Testcase Example:  '[[2]]'

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 











Example 1:


Input: [[2]]
Output: 10



Example 2:


Input: [[1,2],[3,4]]
Output: 34



Example 3:


Input: [[1,0],[0,2]]
Output: 16



Example 4:


Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32



Example 5:


Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


 

Note:


        1 <= N <= 50
        0 <= grid[i][j] <= 50

'''
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width=len(grid)
        height=len(grid[0])
        total=0
        for i in range(width):
            for j in range(height):
                if grid[i][j]==0:
                    continue
                total+=grid[i][j]*4+2
                if i>0:
                    total-=min(grid[i-1][j],grid[i][j])
                if i<width-1:
                    total-=min(grid[i+1][j],grid[i][j])
                if j>0:
                    total -= min(grid[i][j-1], grid[i][j])
                if j<height-1:
                    total -= min(grid[i][j+1],grid[i][j])
        return total
