'''
[6] ZigZag Conversion

https://leetcode.com/problems/zigzag-conversion/description/

* algorithms
* Medium (31.87%)
* Source Code:       6.zigzag-conversion.py
* Total Accepted:    325.3K
* Total Submissions: 1M
* Testcase Example:  '"PAYPALISHIRING"\n3'

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:


string convert(string s, int numRows);

Example 1:


Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:


Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        mod=2*numRows-2
        res=['']*numRows
        for i in range(len(s)):
            if i%mod< numRows:
                res[i%mod]+=s[i]
            else:
                res[mod-i%mod]+=s[i]
        return ''.join(res)
        
