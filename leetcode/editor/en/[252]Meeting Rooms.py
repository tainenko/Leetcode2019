# Given an array of meeting time intervals where intervals[i] = [starti, endi], 
# determine if a person could attend all meetings. 
# 
#  
#  Example 1: 
#  Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
#  Example 2: 
#  Input: intervals = [[7,10],[2,4]]
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  0 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti < endi <= 10⁶ 
#  
#  Related Topics Array Sorting 👍 1168 👎 60


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)
