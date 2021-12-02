# Given a string s, return true if a permutation of the string could form a 
# palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "code"
# Output: false
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aab"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "carerac"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5000 
#  s consists of only lowercase English letters. 
#  
#  Related Topics Hash Table String Bit Manipulation 👍 754 👎 64


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        flag = False
        for k, v in count.items():
            if v % 2 == 0:
                continue
            if not flag:
                flag = True
            else:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
