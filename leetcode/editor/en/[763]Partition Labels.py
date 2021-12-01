# You are given a string s. We want to partition the string into as many parts 
# as possible so that each letter appears in at most one part. 
# 
#  Return a list of integers representing the size of these parts. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits s into less parts.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "eccbbbbdec"
# Output: [10]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of lowercase English letters. 
#  
#  Related Topics Hash Table Two Pointers String Greedy 👍 5852 👎 237


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
# leetcode submit region end(Prohibit modification and deletion)
