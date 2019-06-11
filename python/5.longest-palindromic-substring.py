'''
[5] Longest Palindromic Substring  

https://leetcode.com/problems/longest-palindromic-substring/description/

* algorithms
* Medium (26.30%)
* Source Code:       5.longest-palindromic-substring.0.py
* Total Accepted:    461.1K
* Total Submissions: 1.8M
* Testcase Example:  '"babad"'

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:


Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.


Example 2:


Input: "cbbd"
Output: "bb"

'''
class Solution:
    def longestPalindrome(self, s):
        s='$'.join(s)
        sub=''
        for i,c in enumerate(s):
            j=1
            while i-j>=0 and i+j<len(s):
                if s[i-j]==s[i+j]:
                    j+=1
                    continue
                break
            if 2*j+i>len(sub):
                sub=s[i-j:i+j+1]
        return sub.replace('$','')