# You are given two strings s1 and s2 of equal length. A string swap is an 
# operation where you choose two indices in a string (not necessarily different) and 
# swap the characters at these indices. 
# 
#  Return true if it is possible to make both strings equal by performing at 
# most one string swap on exactly one of the strings. Otherwise, return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of 
# s2 to make "bank".
#  
# 
#  Example 2: 
# 
#  
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
#  
# 
#  Example 3: 
# 
#  
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation 
# is required.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s1.length, s2.length <= 100 
#  s1.length == s2.length 
#  s1 and s2 consist of only lowercase English letters. 
#  
#  Related Topics Hash Table String Counting 👍 494 👎 18


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        while left < len(s1):
            if s1[left] != s2[left]:
                break
            left += 1
        if left == len(s1):
            return True
        while right >= 0:
            if s1[right] != s2[right]:
                break
            right -= 1
        return s1 == s2[:left] + s2[right] + s2[left + 1:right] + s2[left] + s2[right + 1:]
# leetcode submit region end(Prohibit modification and deletion)
