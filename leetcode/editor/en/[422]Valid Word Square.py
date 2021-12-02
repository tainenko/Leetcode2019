# Given an array of strings words, return true if it forms a valid word square. 
# 
# 
#  A sequence of strings forms a valid word square if the kᵗʰ row and column 
# read the same string, where 0 <= k < max(numRows, numColumns). 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abcd","bnrt","crmy","dtye"]
# Output: true
# Explanation:
# The 1ˢᵗ row and 1ˢᵗ column both read "abcd".
# The 2ⁿᵈ row and 2ⁿᵈ column both read "bnrt".
# The 3ʳᵈ row and 3ʳᵈ column both read "crmy".
# The 4ᵗʰ row and 4ᵗʰ column both read "dtye".
# Therefore, it is a valid word square.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["abcd","bnrt","crm","dt"]
# Output: true
# Explanation:
# The 1ˢᵗ row and 1ˢᵗ column both read "abcd".
# The 2ⁿᵈ row and 2ⁿᵈ column both read "bnrt".
# The 3ʳᵈ row and 3ʳᵈ column both read "crm".
# The 4ᵗʰ row and 4ᵗʰ column both read "dt".
# Therefore, it is a valid word square.
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["ball","area","read","lady"]
# Output: false
# Explanation:
# The 3ʳᵈ row reads "read" while the 3ʳᵈ column reads "lead".
# Therefore, it is NOT a valid word square.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 500 
#  1 <= words[i].length <= 500 
#  words[i] consists of only lowercase English letters. 
#  
#  Related Topics Array Matrix 👍 257 👎 154


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j > len(words) - 1 or i > len(words[j]) - 1 or words[i][j] != words[j][i]:
                    return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
