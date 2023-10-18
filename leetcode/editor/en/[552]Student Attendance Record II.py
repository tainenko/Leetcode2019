# An attendance record for a student can be represented as a string where each 
# character signifies whether the student was absent, late, or present on that day.
#  The record only contains the following three characters: 
# 
#  
#  'A': Absent. 
#  'L': Late. 
#  'P': Present. 
#  
# 
#  Any student is eligible for an attendance award if they meet both of the 
# following criteria: 
# 
#  
#  The student was absent ('A') for strictly fewer than 2 days total. 
#  The student was never late ('L') for 3 or more consecutive days. 
#  
# 
#  Given an integer n, return the number of possible attendance records of 
# length n that make a student eligible for an attendance award. The answer may be 
# very large, so return it modulo 10⁹ + 7. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# 
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be 
# fewer than 2).
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 3
#  
# 
#  Example 3: 
# 
#  
# Input: n = 10101
# Output: 183236316
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁵ 
#  
# 
#  Related Topics Dynamic Programming 👍 1680 👎 248


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkRecord(self, n):
        MOD = 1_000_000_007
        p = 1
        l = 1
        a = 1
        ap = 0
        al = 0
        ll = 0
        all = 0
        for _ in range(n - 1):
            p, l, a, ap, al, ll, all = (p + l + ll) % MOD, p, (p + l + ll) % MOD, (a + ap + al + all) % MOD, (
                        a + ap) % MOD, l, al

        return (p + l + a + ap + al + ll + all) % MOD

# leetcode submit region end(Prohibit modification and deletion)
