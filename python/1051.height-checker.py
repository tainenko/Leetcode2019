
'''
[1051] Height Checker

https://leetcode.com/problems/height-checker/description/

* algorithms
* Easy (70.44%)
* Source Code:       1051.height-checker.py
* Total Accepted:    6.2K
* Total Submissions: 8.9K
* Testcase Example:  '[1,1,4,2,1,3]'

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:


Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.


 

Note:


        1 <= heights.length <= 100
        1 <= heights[i] <= 100

'''
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        tmp=sorted(heights)
        count=0
        for i in range(len(heights)):
            if tmp[i]!=heights[i]:
                count+=1
        return count
        
