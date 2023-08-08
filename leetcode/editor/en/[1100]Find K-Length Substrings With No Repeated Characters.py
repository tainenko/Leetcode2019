# Given a string s and an integer k, return the number of substrings in s of 
# length k with no repeated characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno',
# 'etcod','tcode'.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is 
# not possible to find any substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 525 👎 11


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
