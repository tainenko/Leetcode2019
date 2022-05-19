# Write a program to count the number of days between two dates. 
# 
#  The two dates are given as strings, their format is YYYY-MM-DD as shown in 
# the examples. 
# 
#  
#  Example 1: 
#  Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
#  Example 2: 
#  Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#  
#  
#  Constraints: 
# 
#  
#  The given dates are valid dates between the years 1971 and 2100. 
#  
#  Related Topics Math String 👍 188 👎 823


# leetcode submit region begin(Prohibit modification and deletion)
from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((date.fromisoformat(date2) - date.fromisoformat(date1)).days)

# leetcode submit region end(Prohibit modification and deletion)
