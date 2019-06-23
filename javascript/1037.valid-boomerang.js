/**
 * [1037] Valid Boomerang

https://leetcode.com/problems/valid-boomerang/description/

* algorithms
* Easy (37.62%)
* Source Code:       1037.valid-boomerang.js
* Total Accepted:    7.5K
* Total Submissions: 20K
* Testcase Example:  '[[1,1],[2,3],[3,2]]'

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:


Input: [[1,1],[2,3],[3,2]]
Output: true



Example 2:


Input: [[1,1],[2,2],[3,3]]
Output: false


 

Note:


        points.length == 3
        points[i].length == 2
        0 <= points[i][j] <= 100

 */
/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    let dx1=points[1][0]-points[0][0];
    let dx2=points[2][0]-points[0][0];
    let dy1=points[1][1]-points[0][1];
    let dy2=points[2][1]-points[0][1];

    return dx1*dy2!=dx2*dy1;
};
