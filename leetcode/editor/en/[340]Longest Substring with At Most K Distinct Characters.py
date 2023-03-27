# Given a string s and an integer k, return the length of the longest substring 
# of s that contains at most k distinct characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3. 
# 
#  Example 2: 
# 
#  
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  0 <= k <= 50 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 2601 👎 77


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        res = 0
        left = 0
        for idx, val in enumerate(s):
            cnt[val] += 1
            while len(cnt) > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            res = max(res, idx - left + 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
