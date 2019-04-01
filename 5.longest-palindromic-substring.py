class Solution:
    def longestPalindrome(self, s):
        s='$'.join(s)
        sub=''
        for i,c in enumerate(s):
            j=0
            while i-j>=0 and i+j<=len(s):
                if s[i-j]==s[i+j]:
                    j+=1
                    continue
                break
            if 2*j+i>len(sub):
                sub=s[i-j:i+j]
        return sub.replace('$','')