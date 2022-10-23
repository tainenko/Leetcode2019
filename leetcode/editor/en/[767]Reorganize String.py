# Given a string s, rearrange the characters of s so that any two adjacent 
# characters are not the same. 
# 
#  Return any possible rearrangement of s or return "" if not possible. 
# 
#  
#  Example 1: 
#  Input: s = "aab"
# Output: "aba"
#  
#  Example 2: 
#  Input: s = "aaab"
# Output: ""
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Greedy Sorting Heap (Priority Queue) 
# Counting 👍 5524 👎 191


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = "#"
        cnt = Counter(s)
        stop = True
        while cnt:
            for v, _ in cnt.most_common():
                if v != res[-1]:
                    res += v
                    stop = False
                    cnt[v] -= 1
                    if not cnt[v]:
                        del cnt[v]
                    break
                stop = True
            if stop:
                return ""
        return res[1:] if not stop else ""

# leetcode submit region end(Prohibit modification and deletion)
