# You are given two integers red and blue representing the count of red and 
# blue colored balls. You have to arrange these balls to form a triangle such that 
# the 1ˢᵗ row will have 1 ball, the 2ⁿᵈ row will have 2 balls, the 3ʳᵈ row will have 
# 3 balls, and so on. 
# 
#  All the balls in a particular row should be the same color, and adjacent 
# rows should have different colors. 
# 
#  Return the maximum height of the triangle that can be achieved. 
# 
#  
#  Example 1: 
# 
#  
#  Input: red = 2, blue = 4 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  
# 
#  The only possible arrangement is shown above. 
# 
#  Example 2: 
# 
#  
#  Input: red = 2, blue = 1 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  The only possible arrangement is shown above. 
# 
#  Example 3: 
# 
#  
#  Input: red = 1, blue = 1 
#  
# 
#  Output: 1 
# 
#  Example 4: 
# 
#  
#  Input: red = 10, blue = 1 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  The only possible arrangement is shown above. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= red, blue <= 100 
#  
# 
#  👍 66 👎 10


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.help(red, blue, 1), self.help(blue, red, 1))

    def help(self, red, blue, cnt):
        if red < cnt:
            return cnt - 1
        return self.help(blue, red - cnt, cnt + 1)
# leetcode submit region end(Prohibit modification and deletion)
