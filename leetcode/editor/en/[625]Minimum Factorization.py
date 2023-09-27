# Given a positive integer num, return the smallest positive integer x whose 
# multiplication of each digit equals num. If there is no answer or the answer is 
# not fit in 32-bit signed integer, return 0. 
# 
#  
#  Example 1: 
#  Input: num = 48
# Output: 68
#  
#  Example 2: 
#  Input: num = 15
# Output: 35
#  
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2³¹ - 1 
#  
# 
#  Related Topics Math Greedy 👍 125 👎 110


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num <= 1:
            return num
        nums = []
        for i in range(9, 1, -1):
            if not num:
                break
            while num:
                if num % i == 0:
                    nums.append(i)
                    num //= i
                else:
                    break
        if num != 1:
            return 0
        res = 0
        for i in nums[::-1]:
            res = res * 10 + i
        return res if res <= 2147483647 else 0
# leetcode submit region end(Prohibit modification and deletion)
