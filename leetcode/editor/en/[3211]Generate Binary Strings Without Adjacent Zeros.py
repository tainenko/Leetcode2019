# You are given a positive integer n. 
# 
#  A binary string x is valid if all substrings of x of length 2 contain at 
# least one "1". 
# 
#  Return all valid strings with length n, in any order. 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 3 
#  
# 
#  Output: ["010","011","101","110","111"] 
# 
#  Explanation: 
# 
#  The valid strings of length 3 are: "010", "011", "101", "110", and "111". 
# 
#  Example 2: 
# 
#  
#  Input: n = 1 
#  
# 
#  Output: ["0","1"] 
# 
#  Explanation: 
# 
#  The valid strings of length 1 are: "0" and "1". 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 18 
#  
# 
#  Related Topics String Bit Manipulation Recursion 👍 147 👎 23


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]

        def helper(i):
            nonlocal res
            if i >= n:
                return res
            tmp = []
            for j in ["0", "1"]:
                for k in range(len(res)):
                    if j == "0" and res[k].endswith("0"):
                        continue
                    tmp.append(res[k] + j)
            res = tmp
            helper(i + 1)

        helper(1)
        return res

# leetcode submit region end(Prohibit modification and deletion)
