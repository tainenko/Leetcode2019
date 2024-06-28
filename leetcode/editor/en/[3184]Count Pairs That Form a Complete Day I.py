# Given an integer array hours representing times in hours, return an integer 
# denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a 
# complete day. 
# 
#  A complete day is defined as a time duration that is an exact multiple of 24 
# hours. 
# 
#  For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and 
# so on. 
# 
#  
#  Example 1: 
# 
#  
#  Input: hours = [12,12,30,24,24] 
#  
# 
#  Output: 2 
# 
#  Explanation: 
# 
#  The pairs of indices that form a complete day are (0, 1) and (3, 4). 
# 
#  Example 2: 
# 
#  
#  Input: hours = [72,48,24,3] 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= hours.length <= 100 
#  1 <= hours[i] <= 10⁹ 
#  
# 
#  Related Topics Array Hash Table Counting 👍 75 👎 5
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = collections.Counter()
        res = 0
        for h in hours:
            h %= 24
            if h == 0:
                res += cnt.get(0, 0)
            else:
                res += cnt.get(24 - h, 0)
            cnt[h] += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
