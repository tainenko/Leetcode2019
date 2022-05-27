# A square triple (a,b,c) is a triple where a, b, and c are integers and a² + b²
#  = c². 
# 
#  Given an integer n, return the number of square triples such that 1 <= a, b, 
# c <= n. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).
#  
# 
#  Example 2: 
# 
#  
# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 250 
#  
#  Related Topics Math Enumeration 👍 193 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            for j in range(1, i):
                root1 = sqrt(i ** 2 + j ** 2)
                root2 = int(root1)
                if root1 == root2 and root2 <= n:
                    cnt += 1
        return cnt * 2
# leetcode submit region end(Prohibit modification and deletion)
