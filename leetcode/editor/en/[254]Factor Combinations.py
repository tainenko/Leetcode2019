# Numbers can be regarded as the product of their factors. 
# 
#  
#  For example, 8 = 2 x 2 x 2 = 2 x 4. 
#  
# 
#  Given an integer n, return all possible combinations of its factors. You may 
# return the answer in any order. 
# 
#  Note that the factors should be in the range [2, n - 1]. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1
# Output: []
#  
# 
#  Example 2: 
# 
#  
# Input: n = 12
# Output: [[2,6],[3,4],[2,2,3]]
#  
# 
#  Example 3: 
# 
#  
# Input: n = 37
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁷ 
#  
#  Related Topics Array Backtracking 👍 827 👎 43


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        cur = []
        self.helper(n, cur, res)
        return res

    def helper(self, n, cur, res):
        if n == 1:
            return
        bound = int(math.floor(math.sqrt(n)))
        for i in range(2, bound + 1):
            if len(cur) != 0 and i < cur[-1]:
                continue
            if n % i == 0:
                cur.append(i)
                res.append(cur + [n / i])
                if math.sqrt(n / i) >= i:
                    self.helper(n / i, cur, res)
                cur.pop()
        return

# leetcode submit region end(Prohibit modification and deletion)
