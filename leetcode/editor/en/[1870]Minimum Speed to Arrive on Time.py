# You are given a floating-point number hour, representing the amount of time 
# you have to reach the office. To commute to the office, you must take n trains in 
# sequential order. You are also given an integer array dist of length n, where 
# dist[i] describes the distance (in kilometers) of the iᵗʰ train ride. 
# 
#  Each train can only depart at an integer hour, so you may need to wait in 
# between each train ride. 
# 
#  
#  For example, if the 1ˢᵗ train ride takes 1.5 hours, you must wait for an 
# additional 0.5 hours before you can depart on the 2ⁿᵈ train ride at the 2 hour mark.
#  
#  
# 
#  Return the minimum positive integer speed (in kilometers per hour) that all 
# the trains must travel at for you to reach the office on time, or -1 if it is 
# impossible to be on time. 
# 
#  Tests are generated such that the answer will not exceed 10⁷ and hour will 
# have at most two digits after the decimal point. 
# 
#  
#  Example 1: 
# 
#  
# Input: dist = [1,3,2], hour = 6
# Output: 1
# Explanation: At speed 1:
# - The first train ride takes 1/1 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 1 
# hour mark. The second train takes 3/1 = 3 hours.
# - Since we are already at an integer hour, we depart immediately at the 4 
# hour mark. The third train takes 2/1 = 2 hours.
# - You will arrive at exactly the 6 hour mark.
#  
# 
#  Example 2: 
# 
#  
# Input: dist = [1,3,2], hour = 2.7
# Output: 3
# Explanation: At speed 3:
# - The first train ride takes 1/3 = 0.33333 hours.
# - Since we are not at an integer hour, we wait until the 1 hour mark to 
# depart. The second train ride takes 3/3 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 2 
# hour mark. The third train takes 2/3 = 0.66667 hours.
# - You will arrive at the 2.66667 hour mark.
#  
# 
#  Example 3: 
# 
#  
# Input: dist = [1,3,2], hour = 1.9
# Output: -1
# Explanation: It is impossible because the earliest the third train can depart 
# is at the 2 hour mark.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == dist.length 
#  1 <= n <= 10⁵ 
#  1 <= dist[i] <= 10⁵ 
#  1 <= hour <= 10⁹ 
#  There will be at most two digits after the decimal point in hour. 
#  
# 
#  Related Topics Array Binary Search 👍 604 👎 81


# leetcode submit region begin(Prohibit modification and deletion)
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if ceil(hour) < len(dist):
            return -1

        l = 0
        r = 10000000
        while l < r - 1:
            mid = l + (r - l) // 2
            if self.canReach(dist, mid, hour):
                r = mid
            else:
                l = mid
        return l + 1

    def canReach(self, dist, speed, hour):
        total = 0
        for station in dist[:-1]:
            total += ceil(station / speed)
        total += dist[-1] / speed
        return total <= hour

# leetcode submit region end(Prohibit modification and deletion)
