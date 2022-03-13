# You are given a string s and an integer array indices of the same length. The 
# string s will be shuffled such that the character at the iᵗʰ position moves to 
# indices[i] in the shuffled string. 
# 
#  Return the shuffled string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
#  
# 
#  
#  Constraints: 
# 
#  
#  s.length == indices.length == n 
#  1 <= n <= 100 
#  s consists of only lowercase English letters. 
#  0 <= indices[i] < n 
#  All values of indices are unique. 
#  
#  Related Topics Array String 👍 1264 👎 243


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None] * len(s)
        for char, idx in zip(s, indices):
            res[idx] = char
        return "".join(res)
# leetcode submit region end(Prohibit modification and deletion)
