# A 0-indexed array derived with length n is derived by computing the bitwise 
# XOR (⊕) of adjacent values in a binary array original of length n. 
# 
#  Specifically, for each index i in the range [0, n - 1]: 
# 
#  
#  If i = n - 1, then derived[i] = original[i] ⊕ original[0]. 
#  Otherwise, derived[i] = original[i] ⊕ original[i + 1]. 
#  
# 
#  Given an array derived, your task is to determine whether there exists a 
# valid binary array original that could have formed derived. 
# 
#  Return true if such an array exists or false otherwise. 
# 
#  
#  A binary array is an array containing only 0's and 1's 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: derived = [1,1,0]
# Output: true
# Explanation: A valid original array that gives derived is [0,1,0].
# derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
# derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
# derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
#  
# 
#  Example 2: 
# 
#  
# Input: derived = [1,1]
# Output: true
# Explanation: A valid original array that gives derived is [0,1].
# derived[0] = original[0] ⊕ original[1] = 1
# derived[1] = original[1] ⊕ original[0] = 1
#  
# 
#  Example 3: 
# 
#  
# Input: derived = [1,0]
# Output: false
# Explanation: There is no valid original array that gives derived.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == derived.length 
#  1 <= n <= 10⁵ 
#  The values in derived are either 0's or 1's 
#  
# 
#  Related Topics Array Bit Manipulation 👍 785 👎 50


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0
# leetcode submit region end(Prohibit modification and deletion)
