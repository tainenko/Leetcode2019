# No-Zero integer is a positive integer that does not contain any 0 in its 
# decimal representation. 
# 
#  Given an integer n, return a list of two integers [A, B] where: 
# 
#  
#  A and B are No-Zero integers. 
#  A + B = n 
#  
# 
#  The test cases are generated so that there is at least one valid solution. 
# If there are many valid solutions you can return any of them. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: [1,1]
# Explanation: A = 1, B = 1. A + B = n and both A and B do not contain any 0 in 
# their decimal representation.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 11
# Output: [2,9]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 10⁴ 
#  
#  Related Topics Math 👍 263 👎 217


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if not ('0' in str(i) or '0' in str(n - i)):
                return [i, n - i]

# leetcode submit region end(Prohibit modification and deletion)
