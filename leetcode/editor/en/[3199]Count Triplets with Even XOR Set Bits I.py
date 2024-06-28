# Given three integer arrays a, b, and c, return the number of triplets (a[i], 
# b[j], c[k]), such that the bitwise XOR of the elements of each triplet has an 
# even number of set bits.
# 
#  
#  Example 1: 
# 
#  
#  Input: a = [1], b = [2], c = [3] 
#  
# 
#  Output: 1 
# 
#  Explanation: 
# 
#  The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 002.
#  
# 
#  Example 2: 
# 
#  
#  Input: a = [1,1], b = [2,3], c = [1,5] 
#  
# 
#  Output: 4 
# 
#  Explanation: 
# 
#  Consider these four triplets: 
# 
#  
#  (a[0], b[1], c[0]): 1 XOR 3 XOR 1 = 0112 
#  (a[1], b[1], c[0]): 1 XOR 3 XOR 1 = 0112 
#  (a[0], b[0], c[1]): 1 XOR 2 XOR 5 = 1102 
#  (a[1], b[0], c[1]): 1 XOR 2 XOR 5 = 1102 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= a.length, b.length, c.length <= 100 
#  0 <= a[i], b[i], c[i] <= 100 
#  
# 
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        res = 0
        for i in a:
            for j in b:
                for k in c:
                    if bin(i ^ j ^ k).count('1') % 2 == 0:
                        res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
