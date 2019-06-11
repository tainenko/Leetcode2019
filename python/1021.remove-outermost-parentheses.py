'''
[1021] Remove Outermost Parentheses

https://leetcode.com/problems/remove-outermost-parentheses/description/

* algorithms
* Easy (76.67%)
* Source Code:       1021.remove-outermost-parentheses.py
* Total Accepted:    21.4K
* Total Submissions: 27.9K
* Testcase Example:  '"(()())(())"'

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:


Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:


        S.length <= 10000
        S[i] is "(" or ")"
        S is a valid parentheses string

'''
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp=0
        res=''
        prev=0
        for i in range(len(S)):
            if S[i]=='(':
                tmp+=1
            else:
                tmp-=1
            if tmp==0:
                res+=S[prev+1:i]
                prev=i+1
        return res
