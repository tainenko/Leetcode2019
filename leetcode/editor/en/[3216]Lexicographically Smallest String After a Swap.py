# Given a string s containing only digits, return the lexicographically 
# smallest string that can be obtained after swapping adjacent digits in s with the same 
# parity at most once. 
# 
#  Digits have the same parity if both are odd or both are even. For example, 5 
# and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not. 
# 
#  
#  Example 1: 
# 
#  
#  Input: s = "45320" 
#  
# 
#  Output: "43520" 
# 
#  Explanation: 
# 
#  s[1] == '5' and s[2] == '3' both have the same parity, and swapping them 
# results in the lexicographically smallest string. 
# 
#  Example 2: 
# 
#  
#  Input: s = "001" 
#  
# 
#  Output: "001" 
# 
#  Explanation: 
# 
#  There is no need to perform a swap because s is already the 
# lexicographically smallest. 
# 
#  
#  Constraints: 
# 
#  
#  2 <= s.length <= 100 
#  s consists only of digits. 
#  
# 
#  Related Topics String Greedy 👍 49 👎 12


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getSmallestString(self, s: str) -> str:
        idx = 0
        for i in range(len(s) - 1):
            if s[i] > s[i + 1] and (int(s[i]) % 2 == int(s[i + 1]) % 2):
                idx = i
                break
        else:
            return s
        return s[:idx] + s[idx + 1] + s[idx] + s[idx + 2:]
# leetcode submit region end(Prohibit modification and deletion)
