# Given a string s, return the length of the longest substring that contains at 
# most two distinct characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of English letters. 
#  
#  Related Topics Hash Table String Sliding Window 👍 1541 👎 25


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        slide_window = defaultdict(int)
        res = 0
        idx = 0
        for i in range(len(s)):
            slide_window[s[i]] += 1
            while len(slide_window) > 2:
                slide_window[s[idx]] -= 1
                if slide_window[s[idx]] == 0:
                    slide_window.pop(s[idx])
                idx += 1
            res = max(res, i - idx + 1)
        return res

# leetcode submit region end(Prohibit modification and deletion)
