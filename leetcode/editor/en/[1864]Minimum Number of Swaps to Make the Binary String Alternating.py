# Given a binary string s, return the minimum number of character swaps to make 
# it alternating, or -1 if it is impossible. 
# 
#  The string is called alternating if no two adjacent characters are equal. 
# For example, the strings "010" and "1010" are alternating, while the string "0100" 
# is not. 
# 
#  Any two characters may be swapped, even if they are not adjacent. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "111000"
# Output: 1
# Explanation: Swap positions 1 and 4: "111000" -> "101010"
# The string is now alternating.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating, no swaps are needed.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1110"
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] is either '0' or '1'. 
#  
# 
#  Related Topics String Greedy 👍 443 👎 27


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        res = 0
        if zeros == ones:
            for i in range(0, len(s), 2):
                if s[i] == "0":
                    res += 1
            return min(res, len(s) // 2 - res)
        elif zeros == ones + 1:
            for i in range(0, len(s), 2):
                if s[i] == "1":
                    res += 1
            return res
        elif ones == zeros + 1:
            for i in range(0, len(s), 2):
                if s[i] == "0":
                    res += 1
            return res
        return -1

# leetcode submit region end(Prohibit modification and deletion)
