'''
[1071] Greatest Common Divisor of Strings

https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

* algorithms
* Easy (53.49%)
* Source Code:       1071.greatest-common-divisor-of-strings.py
* Total Accepted:    5.8K
* Total Submissions: 10.9K
* Testcase Example:  '"ABCABC"\n"ABC"'

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:


Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"


Example 2:


Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"


Example 3:


Input: str1 = "LEET", str2 = "CODE"
Output: ""


 

Note:


        1 <= str1.length <= 1000
        1 <= str2.length <= 1000
        str1[i] and str2[i] are English uppercase letters.

'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)<len(str2):
            str1,str2=str2,str1
        if str2  not in str1:
            return ""
        elif not str1.replace(str2,''):
            return str2
        return self.gcdOfStrings(str2,str1.replace(str2,'',1))