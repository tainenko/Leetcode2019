'''
[917] Reverse Only Letters

https://leetcode.com/problems/reverse-only-letters/description/

* algorithms
* Easy (56.00%)
* Source Code:       917.reverse-only-letters.py
* Total Accepted:    30.3K
* Total Submissions: 54K
* Testcase Example:  '"ab-cd"'

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 











Example 1:


Input: "ab-cd"
Output: "dc-ba"



Example 2:


Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"



Example 3:


Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


 


Note:


        S.length <= 100
        33 <= S[i].ASCIIcode <= 122 
        S doesn't contain \ or "

'''


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        left = 0
        right = len(S) - 1
        while left < right:
            while left < len(S) and not S[left].isalpha():
                left += 1
            while right >= 0 and not S[right].isalpha():
                right -= 1

            if left < right:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return ''.join(S)
