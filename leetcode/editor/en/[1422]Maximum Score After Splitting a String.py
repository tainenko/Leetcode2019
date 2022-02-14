# Given a string s of zeros and ones, return the maximum score after splitting 
# the string into two non-empty substrings (i.e. left substring and right 
# substring). 
# 
#  The score after splitting a string is the number of zeros in the left 
# substring plus the number of ones in the right substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
#  
# 
#  Example 2: 
# 
#  
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 
# + 3 = 5
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1111"
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 500 
#  The string s consists of characters '0' and '1' only. 
#  
#  Related Topics String 👍 463 👎 23


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) == 2:
            return (s[0] == '0') + (s[1] == '1')
        res = [0] * len(s)
        cnt = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                cnt += 1
            res[i] += cnt
        cnt = 0
        for j in range(len(s) - 1, 0, -1):
            if s[j] == '1':
                cnt += 1
            res[j] += cnt
        print(res)
        return max(res)
# leetcode submit region end(Prohibit modification and deletion)
