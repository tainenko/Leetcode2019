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
        idx1 = 0
        idx2 = 0
        while idx1 <= len(start) and idx2 <= len(end):
            while idx1 < len(start):
                if start[idx1] in ["L", "R"]:
                    break
                idx1 += 1

            while idx2 < len(end):
                if end[idx2] in ["L", "R"]:
                    break
                idx2 += 1

            if idx1 == len(start) or idx2 == len(end):
                break

            if start[idx1] != end[idx2]:
                return False

            if start[idx1] == "L" and idx1 < idx2:
                return False
            if start[idx1] == "R" and idx1 > idx2:
                return False

            idx1 += 1
            idx2 += 1
        if idx1 < len(start) and start[idx1] in ["L", "R"]:
            return False
        if idx2 < len(end) and end[idx2] in ["L", "R"]:
            return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
