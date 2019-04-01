class Solution:
    def lengthOfLongestSubstring(self, s):
        dct={}
        start=0
        count=0
        for i,c in enumerate(s):
            if c in dct and dct[c]>=start:
                start=dct[c]+1
            else:
                count = max(count, i - start + 1)
            dct[c]=i
        return count


