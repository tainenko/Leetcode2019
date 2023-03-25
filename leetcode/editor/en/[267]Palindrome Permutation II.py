# Given a string s, return all the palindromic permutations (without duplicates)
#  of it. 
# 
#  You may return the answer in any order. If s has no palindromic permutation, 
# return an empty list. 
# 
#  
#  Example 1: 
#  Input: s = "aabb"
# Output: ["abba","baab"]
#  
#  Example 2: 
#  Input: s = "abc"
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s consists of only lowercase English letters. 
#  
# 
#  Related Topics Hash Table String Backtracking 👍 808 👎 92


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from itertools import permutations


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        mid = ""
        partial = ""
        for k, v in count.items():
            partial += k * (v // 2)
            mid += k * (v % 2)

        if len(mid) > 1:
            return []

        res = []
        for half in set(permutations(partial)):
            word = "".join(half)
            res.append(f"{word}{mid}{word[::-1]}")

        return res

        # leetcode submit region end(Prohibit modification and deletion)
