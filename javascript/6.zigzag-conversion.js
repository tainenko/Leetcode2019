/**
 * [6] ZigZag Conversion

https://leetcode.com/problems/zigzag-conversion/description/

* algorithms
* Medium (31.87%)
* Source Code:       6.zigzag-conversion.js
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

 */
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if(numRows===1){
        return s;
    }
    let ret = new Array(numRows).fill('');
    let n = 2*numRows-2;
    let half = n/2+1;

    for(let i=0;i<s.length;i++){
        let j = i%n;
        if(j>numRows-1){
            j=n-j;
        }
        ret[j]+=s[i];
    }
    let res= '';
    for(let j=0;j<ret.length;j++){
        res+=ret[j];
    }
    return res;
};
