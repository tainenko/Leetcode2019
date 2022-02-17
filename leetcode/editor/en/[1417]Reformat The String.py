# You are given an alphanumeric string s. (Alphanumeric string is a string 
# consisting of lowercase English letters and digits). 
# 
#  You have to find a permutation of the string where no letter is followed by 
# another letter and no digit is followed by another digit. That is, no two 
# adjacent characters have the same type. 
# 
#  Return the reformatted string or return an empty string if it is impossible 
# to reformat the string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1
# c2", "0a1b2c", "0c2a1b" are also valid permutations.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by 
# digits.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by 
# characters.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of only lowercase English letters and/or digits. 
#  
#  Related Topics String 👍 373 👎 72


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformat(self, s: str) -> str:
        q1 = []
        q2 = []
        for c in s:
            if c.isdigit():
                q1.append(c)
            else:
                q2.append(c)
        if len(q2) > len(q1):
            q1, q2 = q2, q1
        if len(q1) - len(q2) > 1:
            return ""
        res = ""
        while q1:
            res += q1.pop()
            if not q2:
                break
            res += q2.pop()
        return res

# leetcode submit region end(Prohibit modification and deletion)
