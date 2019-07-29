'''
[840] Magic Squares In Grid

https://leetcode.com/problems/magic-squares-in-grid/description/

* algorithms
* Easy (35.68%)
* Source Code:       840.magic-squares-in-grid.py
* Total Accepted:    14K
* Total Submissions: 38.9K
* Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:


Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.


Note:


        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        0 <= grid[i][j] <= 15

'''


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid)
        height = len(grid[0])
        count = 0
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                if grid[i][j] == 5:
                    if grid[i - 1][j - 1] + grid[i + 1][j + 1] == grid[i - 1][j + 1] + grid[i + 1][j - 1] == \
                            grid[i - 1][j] + grid[i + 1][j] == grid[i][j - 1] + grid[i][j + 1] == 10 and sum(
                            grid[i - 1][j - 1:j + 2]) == sum(grid[i + 1][j - 1:j + 2]) == sum(
                            grid[i][j - 1:j + 2]) == grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1] == \
                            grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][
                        j + 1] == 15:
                        if grid[i - 1][j - 1] ^ grid[i - 1][j] ^ grid[i - 1][j + 1] ^ grid[i][j - 1] ^ grid[i][j] ^ \
                                grid[i][j + 1] ^ grid[i + 1][j - 1] ^ grid[i + 1][j] ^ grid[i + 1][
                            j + 1] == 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9:
                            count += 1
        return count
