# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a 
# move consists of either replacing one occurrence of "XL" with "LX", or replacing 
# one occurrence of "RX" with "XR". Given the starting string start and the ending 
# string end, return True if and only if there exists a sequence of moves to 
# transform one string to the other. 
# 
#  
#  Example 1: 
# 
#  
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#  
# 
#  Example 2: 
# 
#  
# Input: start = "X", end = "L"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= start.length <= 10⁴ 
#  start.length == end.length 
#  Both start and end will only consist of characters in 'L', 'R', and 'X'. 
#  
# 
#  Related Topics Two Pointers String 👍 962 👎 792


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)
