# You are given a binary string s and an integer k. 
# 
#  A binary string satisfies the k-constraint if either of the following 
# conditions holds: 
# 
#  
#  The number of 0's in the string is at most k. 
#  The number of 1's in the string is at most k. 
#  
# 
#  Return an integer denoting the number of substrings of s that satisfy the k-
# constraint. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "10101", k = 1 
#  
# 
#  Output: 12 
# 
#  Explanation: 
# 
#  Every substring of s except the substrings "1010", "10101", and "0101" 
# satisfies the k-constraint. 
# 
#  Example 2: 
# 
#  
#  Input: s = "1010101", k = 2 
#  
# 
#  Output: 25 
# 
#  Explanation: 
# 
#  Every substring of s except the substrings with a length greater than 5 
# satisfies the k-constraint. 
# 
#  Example 3: 
# 
#  
#  Input: s = "11111", k = 1 
#  
# 
#  Output: 15 
# 
#  Explanation: 
# 
#  All substrings of s satisfy the k-constraint. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 50 
#  1 <= k <= s.length 
#  s[i] is either '0' or '1'. 
#  
# 
#  Related Topics String Sliding Window 👍 55 👎 6


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = 0

        for j in range(1, len(s) + 1):
            for i in range(len(s) - j + 1):
                if i + j > len(s):
                    continue
                if s[i:i + j].count('0') > k and s[i:i + j].count('1') > k:
                    continue
                result += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
