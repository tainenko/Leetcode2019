/**
 * [884] Uncommon Words from Two Sentences

https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

* algorithms
* Easy (60.78%)
* Source Code:       884.uncommon-words-from-two-sentences.js
* Total Accepted:    30.9K
* Total Submissions: 50.9K
* Testcase Example:  '"this apple is sweet"\n"this apple is sour"'

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 





Example 1:


Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]



Example 2:


Input: A = "apple apple", B = "banana"
Output: ["banana"]


 

Note:


        0 <= A.length <= 200
        0 <= B.length <= 200
        A and B both contain only spaces and lowercase letters.

 */
/**
 * @param {string} A
 * @param {string} B
 * @return {string[]}
 */
var uncommonFromSentences = function(A, B) {
    let unique = new Map();

    for(let word of A.split(' ')){
        let value = unique.has(word)? unique.get(word):0;
        unique.set(word,value+1);
    };

    for(let word of B.split(' ')){
        let value = unique.has(word)? unique.get(word):0;
        unique.set(word,value+1);
    };

    let res = new Array();

    for(let key of unique.keys()){
        if(unique.get(key) === 1){
            res.push(key);
        }
    }

    return res;
};
