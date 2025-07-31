# You are given an integer eventTime denoting the duration of an event. You are 
# also given two integer arrays startTime and endTime, each of length n. 
# 
#  These represent the start and end times of n non-overlapping meetings that 
# occur during the event between time t = 0 and time t = eventTime, where the iᵗʰ 
# meeting occurs during the time [startTime[i], endTime[i]]. 
# 
#  You can reschedule at most one meeting by moving its start time while 
# maintaining the same duration, such that the meetings remain non-overlapping, to 
# maximize the longest continuous period of free time during the event. 
# 
#  Return the maximum amount of free time possible after rearranging the 
# meetings. 
# 
#  Note that the meetings can not be rescheduled to a time outside the event 
# and they should remain non-overlapping. 
# 
#  Note: In this version, it is valid for the relative ordering of the meetings 
# to change after rescheduling one meeting. 
# 
#  
#  Example 1: 
# 
#  
#  Input: eventTime = 5, startTime = [1,3], endTime = [2,5] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  
# 
#  Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the 
# time [0, 2]. 
# 
#  Example 2: 
# 
#  
#  Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10] 
#  
# 
#  Output: 7 
# 
#  Explanation: 
# 
#  
# 
#  Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the 
# time [0, 7]. 
# 
#  Example 3: 
# 
#  
#  Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10] 
#  
# 
#  Output: 6 
# 
#  Explanation: 
# 
#  
# 
#  Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the 
# time [1, 7]. 
# 
#  Example 4: 
# 
#  
#  Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5] 
#  
# 
#  Output: 0 
# 
#  Explanation: 
# 
#  There is no time during the event not occupied by meetings. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= eventTime <= 10⁹ 
#  n == startTime.length == endTime.length 
#  2 <= n <= 10⁵ 
#  0 <= startTime[i] < endTime[i] <= eventTime 
#  endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2]. 
#  
# 
#  Related Topics Array Greedy Enumeration 👍 450 👎 25


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        first, second, third = 0, 0, 0
        startTime.append(eventTime)
        endTime.append(eventTime)
        pre = 0
        for start, end in zip(startTime, endTime):
            free = start - pre
            if free > first:
                first, second, third = free, first, second
            elif free > second:
                second, third = free, second
            elif free > third:
                third = free
            pre = end

        pre = 0
        ans = 0
        for i in range(len(startTime) - 1):
            left = startTime[i] - pre
            right = startTime[i + 1] - endTime[i]
            move_length = endTime[i] - startTime[i]
            ans = max(ans, left + right)
            if max(left, right) < first and move_length <= first:
                ans = max(ans, left + right + move_length)
            elif max(left, right) < second and move_length <= second:
                ans = max(ans, left + right + move_length)
            elif move_length <= third:
                ans = max(ans, left + right + move_length)
            pre = endTime[i]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
