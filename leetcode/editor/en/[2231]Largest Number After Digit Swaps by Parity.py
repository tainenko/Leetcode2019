# You are given a positive integer num. You may swap any two digits of num that 
# have the same parity (i.e. both odd digits or both even digits). 
# 
#  Return the largest possible value of num after any number of swaps. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number 321
# 4.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412 
# is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of 
# different parities.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number 856
# 75.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that 87655
#  is the largest possible number.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10⁹ 
#  
# 
#  Related Topics Sorting Heap (Priority Queue) 👍 300 👎 210


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestInteger(self, num: int) -> int:
        odds = []
        evens = []
        nums = [int(n) for n in str(num)]
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        odds.sort(reverse=True)
        evens.sort(reverse=True)
        i = j = 0
        res = 0
        for idx, val in enumerate(nums):
            if val % 2 == 0:
                res = 10 * res + evens[j]
                j += 1
            else:
                res = 10 * res + odds[i]
                i += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
