# You are given a string s and two integers x and y. You can perform two types 
# of operations any number of times. 
# 
#  
#  Remove substring "ab" and gain x points. 
#  
# 
#  
#  For example, when removing "ab" from "cabxbae" it becomes "cxbae". 
#  
#  
#  Remove substring "ba" and gain y points.
#  
#  For example, when removing "ba" from "cabxbae" it becomes "cabxe". 
#  
#  
# 
# 
#  Return the maximum points you can gain after applying the above operations 
# on s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 
# points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 
# points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points 
# are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are 
# added to the score.
# Total score = 5 + 4 + 5 + 5 = 19. 
# 
#  Example 2: 
# 
#  
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  1 <= x, y <= 10⁴ 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics String Stack Greedy 👍 1887 👎 134


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        sub1 = "ab"
        sub2 = "ba"
        if x < y:
            x, y = y, x
            sub1, sub2 = sub2, sub1
        ans = 0
        high_stack = []
        for c in s:
            if high_stack and high_stack[-1] == sub1[0] and c == sub1[1]:
                high_stack.pop()
                ans += x
            else:
                high_stack.append(c)

        low_stack = []
        for c in high_stack:
            if low_stack and low_stack[-1] == sub2[0] and c == sub2[1]:
                low_stack.pop()
                ans += y
            else:
                low_stack.append(c)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
