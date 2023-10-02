# Given a time represented in the format "HH:MM", form the next closest time by 
# reusing the current digits. There is no limit on how many times a digit can be 
# reused. 
# 
#  You may assume the given input string is always valid. For example, "01:34", 
# "12:09" are all valid. "1:34", "12:9" are all invalid. 
# 
#  
#  Example 1: 
# 
#  
# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, 
# which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
#  
# 
#  Example 2: 
# 
#  
# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is 
# smaller than the input time numerically.
#  
# 
#  
#  Constraints: 
# 
#  
#  time.length == 5 
#  time is a valid time in the form "HH:MM". 
#  0 <= HH < 24 
#  0 <= MM < 60 
#  
# 
#  Related Topics String Enumeration 👍 709 👎 1041


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]
        order = sorted(nums)
        mi = order[0]
        for pos in range(3, -1, -1):
            if pos == 3:
                upper = 10
            elif pos == 2:
                upper = 6
            elif pos == 1:
                if nums[0] == 2:
                    upper = 4
                else:
                    upper = 10
            else:
                upper = 3
            candidate = [num for num in nums if nums[pos] < num < upper]
            if not candidate:
                continue
            nums[pos] = min(candidate)
            for i in range(pos + 1, 4):
                nums[i] = mi
            return f"{nums[0]}{nums[1]}:{nums[2]}{nums[3]}"
        return f"{mi}{mi}:{mi}{mi}"

        # leetcode submit region end(Prohibit modification and deletion)
