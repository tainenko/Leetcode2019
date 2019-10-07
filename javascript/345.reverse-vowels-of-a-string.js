/*
 * @lc app=leetcode id=345 lang=javascript
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (41.92%)
 * Total Accepted:    165.5K
 * Total Submissions: 394.5K
 * Testcase Example:  '"hello"'
 *
 * Write a function that takes a string as input and reverse only the vowels of
 * a string.
 * 
 * Example 1:
 * 
 * 
 * Input: "hello"
 * Output: "holle"
 * "eo"->"oe"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "leetcode"
 * Output: "leotcede"
 * "eeoe"->"eoee"
 * 
 * 
 * Input: "laetcode"
 * Output: "leotceda"
 * "aeoe"->"eoea"
 * 
 *  * Note:
 * The vowels does not include the letter "y".
 * 
 * 
 * 
 */
/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let left=0;
    let right=s.length - 1;
    const vowels=new Set(['a','e','i','o','u','A','E','I','O','U']);
    let res=""
    // Set
    // https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Set
    for(let i=0;i<s.length;i++){
        if(vowels.has(s.charAt(i))===false){
            res+=s.charAt(i);
        }
        else{
            while(vowels.has(s.charAt(right))===false){
                right--;
            }
            res+=s.charAt(right);
            right--;
        }
    }
    return res;
};
