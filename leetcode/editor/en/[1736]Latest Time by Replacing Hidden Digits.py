# You are given a string time in the form of hh:mm, where some of the digits in 
# the string are hidden (represented by ?). 
# 
#  The valid times are those inclusively between 00:00 and 23:59. 
# 
#  Return the latest valid time you can get from time by replacing the hidden 
# digits. 
# 
#  
#  Example 1: 
# 
#  
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the 
# latest minute ending with the digit '0' is 50.
#  
# 
#  Example 2: 
# 
#  
# Input: time = "0?:3?"
# Output: "09:39"
#  
# 
#  Example 3: 
# 
#  
# Input: time = "1?:22"
# Output: "19:22"
#  
# 
#  
#  Constraints: 
# 
#  
#  time is in the format hh:mm. 
#  It is guaranteed that you can produce a valid time from the given string. 
#  
#  Related Topics String Greedy 👍 212 👎 124


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(':')
        if hour[1] == '?':
            digit = '3' if hour[0] in ('2', '?') else '9'
            hour = hour[0] + digit
        if hour[0] == '?':
            digit = '2' if int(hour[1]) < 4 else '1'
            hour = digit + hour[1]
        if minute[0] == '?':
            minute = '5' + minute[1]
        if minute[1] == '?':
            minute = minute[0] + '9'
        return f"{hour}:{minute}"

# leetcode submit region end(Prohibit modification and deletion)
