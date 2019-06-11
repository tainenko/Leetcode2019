'''
[1002] Find Common Characters

https://leetcode.com/problems/find-common-characters/description/

* algorithms
* Easy (67.02%)
* Source Code:       1002.find-common-characters.py
* Total Accepted:    16K
* Total Submissions: 24.1K
* Testcase Example:  '["bella","label","roller"]'

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 


Example 1:


Input: ["bella","label","roller"]
Output: ["e","l","l"]



Example 2:


Input: ["cool","lock","cook"]
Output: ["c","o"]


 

Note:


        1 <= A.length <= 100
        1 <= A[i].length <= 100
        A[i][j] is a lowercase letter



ketainiande-MacBook-Pro:leetcode ketainian$ leetcode show 1002  -g -l  javascript
[1002] Find Common Characters

https://leetcode.com/problems/find-common-characters/description/

* algorithms
* Easy (67.02%)
* Source Code:       1002.find-common-characters.js
* Total Accepted:    16K
* Total Submissions: 24.1K
* Testcase Example:  '["bella","label","roller"]'

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 


Example 1:


Input: ["bella","label","roller"]
Output: ["e","l","l"]



Example 2:


Input: ["cool","lock","cook"]
Output: ["c","o"]


 

Note:


        1 <= A.length <= 100
        1 <= A[i].length <= 100
        A[i][j] is a lowercase letter

'''
from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res=Counter(A[0])
        for i in range(1,len(A)):
            res&=Counter(A[i])
        return res


    def commonChars2(self, A: List[str]) -> List[str]:
        dct = dict()
        for word in A:
            for letter in word:
                dct[letter] = dct.get(letter, 0) + 1
        res = []
        for key, value in dct.items():
            value //= 3
            while value > 0:
                res.append(key)
                value -= 1
        return res

