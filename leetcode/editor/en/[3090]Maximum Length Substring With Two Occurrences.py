# Given a string s, return the maximum length of a substring such that it 
# contains at most two occurrences of each character.
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "bcbbbcba" 
#  
# 
#  Output: 4 
# 
#  Explanation: The following substring has a length of 4 and contains at most 
# two occurrences of each character: 
# "bcbbbcba".
# 
#  Example 2: 
# 
#  
#  Input: s = "aaaa" 
#  
# 
#  Output: 2 
# 
#  Explanation: The following substring has a length of 2 and contains at most 
# two occurrences of each character: 
# "aaaa".
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 100 
#  s consists only of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 108 👎 8
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = collections.Counter()
        res = 0
        i, j = 0, 1
        cnt[s[i]] += 1
        while j < len(s):
            cnt[s[j]] += 1
            while cnt[s[j]] > 2:
                cnt[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return max(res, j - i)

# leetcode submit region end(Prohibit modification and deletion)
