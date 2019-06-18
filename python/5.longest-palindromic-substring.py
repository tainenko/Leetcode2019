'''
[5] Longest Palindromic Substring  

https://leetcode.com/problems/longest-palindromic-substring/description/

* algorithms
* Medium (26.30%)
* Source Code:       5.longest-palindromic-substring.py
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
        if not s or len(s)<=1:
            return s
        T='^#'+'#'.join(s)+'#$'
        n=len(T)
        p=[0]*n
        id=wx=0
        R=C=0
        for i in range(1,n-1):
            if i<wx:
                p[i]=min(p[2*id-i],wx-i)
            while T[i-p[i]]==T[i+p[i]]:
                p[i]+=1
            if i+p[i]>wx:
                wx=i+p[i]
                id=i
            if p[i]>R:
                R=p[i]
                C=i
        return s[(C - R) // 2: (C + R) // 2-1]
