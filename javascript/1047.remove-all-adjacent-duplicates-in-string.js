/**
 * [1047] Remove All Adjacent Duplicates In String

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

* algorithms
* Easy (62.57%)
* Source Code:       1047.remove-all-adjacent-duplicates-in-string.js
* Total Accepted:    11.2K
* Total Submissions: 17.8K
* Testcase Example:  '"abbaca"'

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:


Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


 

Note:


        1 <= S.length <= 20000
        S consists only of English lowercase letters.

 */
/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function(S) {
    let arr=S.split('');
    let i=0
    while(i < arr.length){
        if(arr[i]===arr[i+1]){
            arr.splice(i,2);
            if(i-1>=0){
                i--;
            }
            continue
        }
        i++;
    }
    return arr.join('');
};
