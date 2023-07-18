# You and a gang of thieves are planning on robbing a bank. You are given a 0-
# indexed integer array security, where security[i] is the number of guards on duty 
# on the iᵗʰ day. The days are numbered starting from 0. You are also given an 
# integer time. 
# 
#  The iᵗʰ day is a good day to rob the bank if: 
# 
#  
#  There are at least time days before and after the iᵗʰ day, 
#  The number of guards at the bank for the time days before i are non-
# increasing, and 
#  The number of guards at the bank for the time days after i are non-
# decreasing. 
#  
# 
#  More formally, this means day i is a good day to rob the bank if and only if 
# security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= 
# security[i + time - 1] <= security[i + time]. 
# 
#  Return a list of all days (0-indexed) that are good days to rob the bank. 
# The order that the days are returned in does not matter. 
# 
#  
#  Example 1: 
# 
#  
# Input: security = [5,3,3,3,5,6,2], time = 2
# Output: [2,3]
# Explanation:
# On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= 
# security[4].
# On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= 
# security[5].
# No other days satisfy this condition, so days 2 and 3 are the only good days 
# to rob the bank.
#  
# 
#  Example 2: 
# 
#  
# Input: security = [1,1,1,1,1], time = 0
# Output: [0,1,2,3,4]
# Explanation:
# Since time equals 0, every day is a good day to rob the bank, so return every 
# day.
#  
# 
#  Example 3: 
# 
#  
# Input: security = [1,2,3,4,5,6], time = 2
# Output: []
# Explanation:
# No day has 2 days before it that have a non-increasing number of guards.
# Thus, no day is a good day to rob the bank, so return an empty list.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= security.length <= 10⁵ 
#  0 <= security[i], time <= 10⁵ 
#  
# 
#  Related Topics Array Dynamic Programming Prefix Sum 👍 771 👎 41


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        dec = [0] * len(security)
        inc = [0] * len(security)

        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                dec[i] = dec[i - 1] + 1

        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                inc[i] = inc[i + 1] + 1

        return [i for i, (a, b) in enumerate(zip(inc, dec)) if a >= time and b >= time]
# leetcode submit region end(Prohibit modification and deletion)
