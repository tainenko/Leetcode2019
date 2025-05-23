# Given the string s, return the size of the longest substring containing each 
# vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear 
# an even number of times. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each 
# of the vowels: e, i and o and zero of the vowels: a and u.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because 
# all vowels: a, e, i, o and u appear zero times.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 x 10^5 
#  s contains only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Bit Manipulation Prefix Sum 👍 2490 👎 139


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {0:-1}
        res = 0
        mask = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                mask ^= 1<<(ord(c) - ord('a'))
            if mask in d:
                j = d[mask]
                res = max(res, i - j)
            else:
                d[mask] = i
        return res

# leetcode submit region end(Prohibit modification and deletion)
