# Given an array of meeting time intervals intervals where intervals[i] = [
# starti, endi], return the minimum number of conference rooms required.
#
#
#  Example 1:
#  Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
#  Example 2:
#  Input: intervals = [[7,10],[2,4]]
# Output: 1
#
#
#  Constraints:
#
#
#  1 <= intervals.length <= 10⁴
#  0 <= starti < endi <= 10⁶
#
#  Related Topics Array Two Pointers Greedy Sorting Heap (Priority Queue) 👍 490
# 2 👎 97


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ups = [(x[0], 1) for x in intervals]
        downs = [(x[1], -1) for x in intervals]
        intervals = sorted(ups + downs, key=lambda x: (x[0], x[1]))
        res = 0
        cnt = 0
        for interval in intervals:
            cnt += interval[1]
            res = max(cnt, res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
